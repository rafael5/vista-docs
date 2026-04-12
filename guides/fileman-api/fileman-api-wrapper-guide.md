# Building a FileMan Database Server API Wrapper
## A Developer Guide for Go and Python Clients

*VA FileMan 22.2 — Database Server (DBS) API — External Application Integration*

---

## Table of Contents

1. [Overview and Architecture](#overview-and-architecture)
2. [How External Clients Reach FileMan](#how-external-clients-reach-fileman)
3. [The Transport Layer: VistA Link / RPC Broker](#the-transport-layer-vista-link--rpc-broker)
4. [Core FileMan DBS Calls You Will Wrap](#core-fileman-dbs-calls-you-will-wrap)
5. [Python Wrapper Implementation](#python-wrapper-implementation)
6. [Go Wrapper Implementation](#go-wrapper-implementation)
7. [Data Conventions and Type Mapping](#data-conventions-and-type-mapping)
8. [Error Handling and Status Codes](#error-handling-and-status-codes)
9. [Worked Examples: Read and Write Patterns](#worked-examples-read-and-write-patterns)
10. [Security and Context Setup](#security-and-context-setup)
11. [Testing Strategy](#testing-strategy)
12. [Deployment Considerations](#deployment-considerations)

---

## Overview and Architecture

VA FileMan does not expose a network port or REST endpoint natively. It is a MUMPS
database engine that runs inside the M runtime (YottaDB or Cache). External applications
reach it through a **Remote Procedure Call (RPC) broker** — a TCP socket server that
accepts marshalled M routine calls and returns results.

The standard broker is the **VistA Broker** (RPC Broker, package XWB), originally
developed for Delphi/CPRS GUI clients. Any application that can speak the RPC wire
protocol can call FileMan DBS routines as if it were a native M caller.

```
External App (Go/Python)
        │
        │  TCP socket (RPC Broker wire protocol)
        ▼
VistA RPC Broker (XWB package)
        │
        │  M DO/$$  calls inside YottaDB/Cache
        ▼
FileMan DBS API (GETS^DIQ, FILE^DIE, FIND^DIC, ...)
        │
        ▼
M Globals (^DPT, ^PS, ^OR, ^TIU, ...)
```

Your wrapper library sits between your application code and the TCP connection.
It handles:
- TCP session management and authentication
- RPC request serialisation (FileMan wire format)
- Response deserialisation
- FileMan-specific type conversions (dates, pointers, multiples)
- Error surface normalisation

---

## How External Clients Reach FileMan

### Option A — VistA RPC Broker (XWB)

The **standard** integration path. The broker is a persistent M listener (`XWBTCPL`)
running on port 9200 (or site-configured port). Each connection authenticates with
a Kernel access/verify code pair.

The wire protocol is a text-based, length-prefixed format. The open-source
Python library **VistA Python** (`vistapython` / `ViViaN`) and the legacy Delphi
`TRPCBroker` component document the full wire format.

Reference: `XWB*8.0` package, routine `XWBPRS` (parser), `XWBCALL` (dispatcher).

### Option B — FMQL (FileMan Query Language)

**FMQL** is a REST/JSON service that wraps FileMan read operations in a
graph-query API. Run as a separate web server against a VistA instance.
Suitable for read-heavy analytics clients; not a write path.

Source: `https://github.com/caregraf/FMQL`

### Option C — VistA Web API / eHMP / MVDM

The **VA's MVDM** project exposes a JSON REST API (Node.js + npm `nodevista`) that
wraps common FileMan operations. Suitable if your target environment has MVDM
deployed.

Source: `https://github.com/vistadataproject/nodeVISTA`

### Option D — Direct YottaDB Embedded Call-In (local only)

If your process runs **on the same server** as YottaDB, you can call M routines
directly via YottaDB's C call-in interface, eliminating the TCP layer entirely.
Available for C, Go (via cgo), Python (via `yottadb` PyPI package).

YottaDB Python API: `pip install yottadb`
YottaDB Go API: `go get lang.yottadb.com/go/yottadb`

This guide covers both the **RPC Broker (Options A)** path for remote apps and
the **YottaDB embedded (Option D)** path for co-located services.

---

## Core FileMan DBS Calls You Will Wrap

These are the DBS (Database Server) API entry points your wrapper needs to expose.
DBS calls are silent — no terminal I/O — and return results in M arrays.

### Read

| FileMan Entry Point | Purpose | Your Wrapper Method |
|---|---|---|
| `GETS^DIQ(file,ien,fields,"","result")` | Get fields for one entry | `get_entry(file, ien, fields)` |
| `$$GET1^DIQ(file,ien,field,"","","")` | Get a single field value | `get_field(file, ien, field)` |
| `FIND^DIC(file,"","B","value","","","result")` | Search by cross-ref | `find(file, index, value)` |
| `$$FIND1^DIC(file,"","B","value","")` | Find single IEN | `find_one(file, index, value)` |
| `LIST^DIC(file,"","B","value","result")` | Get a sorted list | `list_entries(file, from, to)` |

### Write

| FileMan Entry Point | Purpose | Your Wrapper Method |
|---|---|---|
| `FILE^DIE("","fda","errors")` | File (create or update) fields | `file(fda)` |
| `UPDATE^DIE("","fda","errors")` | Update with audit + key check | `update(fda)` |
| `CHK^DIE(file,ien,field,value,"result")` | Validate value without filing | `validate_field(file, ien, field, value)` |

### Schema Introspection

| FileMan Entry Point | Purpose | Your Wrapper Method |
|---|---|---|
| `FIELD^DID(file,field,"","result")` | Get field DD attributes | `get_field_def(file, field)` |
| `FILE^DID(file,"","result")` | Get file DD attributes | `get_file_def(file)` |
| `$$ROOT^DILFD(file,"","")` | Get file global root | `get_global_root(file)` |

---

## Python Wrapper Implementation

### Prerequisites

```bash
# For RPC Broker path:
pip install vistapython   # or install from https://github.com/caregraf/vista-rpc-python

# For YottaDB embedded path:
pip install yottadb       # requires YottaDB installed and YOTTADB env set
```

### Connection Abstraction

Define a connection interface so you can swap between RPC Broker and YottaDB
embedded without changing calling code.

```python
# fileman/connection.py
from abc import ABC, abstractmethod
from typing import Any

class FileManConnection(ABC):
    """Abstract transport: subclass for RPC Broker or YottaDB embedded."""

    @abstractmethod
    def call(self, routine: str, args: list[str]) -> str:
        """Call an M entry point, return raw result string."""
        ...

    @abstractmethod
    def close(self) -> None:
        ...
```

### RPC Broker Connection

```python
# fileman/broker_connection.py
import socket
import struct
from fileman.connection import FileManConnection

class BrokerConnection(FileManConnection):
    """
    Speaks the VistA RPC Broker wire protocol (XWB*8.0).

    Wire format (simplified):
      [NS]<len:5><RPC name><LIT|REF args...>[EOT]
    Full spec: XWB8_0_UM.PDF, Appendix A.
    """

    TIMEOUT = 30
    EOT = b"\x04"

    def __init__(self, host: str, port: int, access: str, verify: str):
        self._host = host
        self._port = port
        self._sock: socket.socket | None = None
        self._connect_and_authenticate(access, verify)

    def _connect_and_authenticate(self, access: str, verify: str) -> None:
        self._sock = socket.create_connection(
            (self._host, self._port), timeout=self.TIMEOUT
        )
        # XWB handshake: send TCPConnect, then hello packet, then signon RPC
        self._send_connect_packet()
        self._signon(access, verify)

    def _send_connect_packet(self) -> None:
        # TCPConnect handshake — sends hostname + port as literal args
        import socket as _s
        hostname = _s.gethostname()[:24]
        packet = self._build_rpc("TCPConnect", [hostname, "0", "9200"])
        self._sock.sendall(packet)
        self._recv_response()   # discard "accept" response

    def _signon(self, access: str, verify: str) -> None:
        # XUS SIGNON — Kernel authentication RPC
        response = self.call("XUS SIGNON", [access + ";" + verify])
        if not response.startswith("0"):
            raise PermissionError(f"FileMan signon failed: {response!r}")

    def _build_rpc(self, name: str, args: list[str]) -> bytes:
        """Encode an RPC call in XWB wire format."""
        # Each arg: type byte (0=literal, 1=reference) + 3-digit length + value
        encoded_args = ""
        for arg in args:
            encoded_args += f"\x00{len(arg):03d}{arg}"
        # RPC header: [NS] + 5-digit total length + rpc name + \x0f + args + EOT
        body = f"\x0f{len(name):03d}{name}5{len(encoded_args):04d}{encoded_args}"
        header = f"[NS]{len(body):05d}"
        return (header + body).encode("ascii") + self.EOT

    def call(self, routine: str, args: list[str]) -> str:
        packet = self._build_rpc(routine, args)
        self._sock.sendall(packet)
        return self._recv_response()

    def _recv_response(self) -> str:
        """Read until EOT, return decoded string."""
        buf = b""
        while not buf.endswith(self.EOT):
            chunk = self._sock.recv(4096)
            if not chunk:
                raise ConnectionError("Broker closed connection unexpectedly")
            buf += chunk
        return buf.rstrip(self.EOT).decode("ascii", errors="replace")

    def close(self) -> None:
        if self._sock:
            try:
                self.call("BYE", [])
            except Exception:
                pass
            self._sock.close()
            self._sock = None
```

### YottaDB Embedded Connection

```python
# fileman/ydb_connection.py
import yottadb
from fileman.connection import FileManConnection

class YDBConnection(FileManConnection):
    """
    Call FileMan DBS routines via YottaDB call-in.
    Requires: YOTTADB env, yottadb Python package, M environment initialised
    with DUZ / DUZ(0) set for the calling process.
    """

    def __init__(self, duz: str, duz_zero: str = "@"):
        """
        duz      — VistA user IEN (NEW PERSON file #200)
        duz_zero — access level; "@" = programmer (full access)
        """
        # Set Kernel context globals that FileMan checks
        yottadb.set("DUZ", [], duz)
        yottadb.set("DUZ", ["0"], duz_zero)
        yottadb.set("U", [], "^")   # output device for Classic calls (ignore)

    def call(self, routine: str, args: list[str]) -> str:
        """
        Call a single-return-value M extrinsic via $$routine^package.
        For multi-value DBS calls (GETS^DIQ etc.), use the higher-level
        FileManClient methods which manipulate globals directly via yottadb.get/set.
        """
        # Simple extrinsic wrapper: set up input, call routine, read output
        result = yottadb.ci(routine, args)
        return str(result) if result is not None else ""

    def get_global(self, gvn: str, subscripts: list[str]) -> str:
        return yottadb.get(gvn, subscripts) or ""

    def set_global(self, gvn: str, subscripts: list[str], value: str) -> None:
        yottadb.set(gvn, subscripts, value)

    def kill_global(self, gvn: str, subscripts: list[str]) -> None:
        yottadb.delete(gvn, subscripts, yottadb.YDB_DEL_TREE)

    def close(self) -> None:
        pass   # YottaDB embedded — no socket to close
```

### FileMan Client

The `FileManClient` wraps the DBS API calls and presents a clean Python API.

```python
# fileman/client.py
import logging
from dataclasses import dataclass, field
from typing import Any
from fileman.connection import FileManConnection

log = logging.getLogger(__name__)


@dataclass
class FileManEntry:
    """A retrieved FileMan entry — file number, IEN, field values."""
    file: str
    ien: str
    fields: dict[str, str]           # field# → internal value
    external: dict[str, str]         # field# → external (display) value


@dataclass
class FDA:
    """
    FileMan Data Array — the structure passed to FILE^DIE / UPDATE^DIE.

    fda[file_number][iens][field_number] = value

    For new entries, IENS uses a temporary placeholder like "+1,".
    For existing entries, IENS is the IEN followed by a comma: "23,".
    For sub-file entries: "sub_ien,parent_ien," e.g. "1,23,".
    """
    data: dict[str, dict[str, dict[str, str]]] = field(default_factory=dict)

    def set(self, file: str, iens: str, field_num: str, value: str) -> None:
        self.data.setdefault(file, {}).setdefault(iens, {})[field_num] = value

    def get(self, file: str, iens: str, field_num: str) -> str | None:
        return self.data.get(file, {}).get(iens, {}).get(field_num)


class FileManError(Exception):
    """Raised when FileMan returns an error array (DIERR global)."""
    def __init__(self, errors: dict[str, str]):
        self.errors = errors
        super().__init__(str(errors))


class FileManClient:
    """
    High-level Python client for VA FileMan DBS API.

    Works with both BrokerConnection and YDBConnection.
    For RPC Broker: DBS calls are wrapped as VistA RPCs (requires custom
    FileMan RPC wrappers registered in the RPC file #8994 on the server).
    For YDB embedded: calls M routines directly.
    """

    def __init__(self, conn: FileManConnection):
        self._conn = conn

    # -----------------------------------------------------------------------
    # READ
    # -----------------------------------------------------------------------

    def get_entry(
        self,
        file: str,
        ien: str,
        fields: str = "*",
        flags: str = "EIN",
    ) -> FileManEntry:
        """
        Retrieve field values for a single entry via GETS^DIQ.

        fields — semicolon-separated field numbers, or "*" for all
        flags  — "E" = return external values, "I" = internal, "N" = no nulls

        Returns FileManEntry with both internal and external values.
        """
        result_node = f"FMQRY{id(self)}"
        # In YDB embedded mode: set up and call GETS^DIQ directly
        if hasattr(self._conn, "set_global"):
            self._gets_ydb(file, ien, fields, flags, result_node)
        else:
            raw = self._conn.call("GETS^DIQ", [file, ien, fields, flags, result_node])
            self._check_dierr()

        entry = self._read_gets_result(result_node, file, ien)
        if hasattr(self._conn, "kill_global"):
            self._conn.kill_global(result_node, [])
        return entry

    def _gets_ydb(
        self, file: str, ien: str, fields: str, flags: str, result_node: str
    ) -> None:
        import yottadb
        # GETS^DIQ(file#,ien,fields,flags,,result_array)
        yottadb.ci("GETS^DIQ", [file, ien + ",", fields, flags, "", result_node])
        self._check_dierr_ydb()

    def _read_gets_result(
        self, result_node: str, file: str, ien: str
    ) -> FileManEntry:
        """Walk the result array and build a FileManEntry."""
        internal: dict[str, str] = {}
        external: dict[str, str] = {}
        if hasattr(self._conn, "get_global"):
            # YDB path — iterate result_node(file,ien,field) nodes
            import yottadb
            sub = [file, ien + ","]
            field_key = yottadb.subscript_next(result_node, sub + [""])
            while field_key:
                val = self._conn.get_global(result_node, sub + [field_key])
                ext = self._conn.get_global(result_node, sub + [field_key, "E"])
                internal[field_key] = val
                if ext:
                    external[field_key] = ext
                field_key = yottadb.subscript_next(result_node, sub + [field_key])
        return FileManEntry(file=file, ien=ien, fields=internal, external=external)

    def get_field(self, file: str, ien: str, field: str) -> str:
        """Return a single field value (external format) via $$GET1^DIQ."""
        result = self._conn.call("$$GET1^DIQ", [file, ien + ",", field, "E"])
        return result.strip()

    def find_one(self, file: str, index: str = "B", value: str = "") -> str | None:
        """
        Return the IEN of the first entry matching value on index,
        or None if not found. Wraps $$FIND1^DIC.
        """
        result = self._conn.call("$$FIND1^DIC", [file, "", index, value, ""])
        ien = result.strip()
        return ien if ien and ien != "0" else None

    def find(
        self,
        file: str,
        index: str = "B",
        value: str = "",
        max_results: int = 200,
    ) -> list[str]:
        """
        Return a list of IENs matching value on index. Wraps FIND^DIC.
        Returns up to max_results entries.
        """
        result_node = f"FMFND{id(self)}"
        self._conn.call(
            "FIND^DIC",
            [file, "", index, value, str(max_results), "", "", result_node],
        )
        iens: list[str] = []
        if hasattr(self._conn, "get_global"):
            import yottadb
            idx = yottadb.subscript_next(result_node, [""])
            while idx:
                iens.append(self._conn.get_global(result_node, [idx]))
                idx = yottadb.subscript_next(result_node, [idx])
            self._conn.kill_global(result_node, [])
        return iens

    # -----------------------------------------------------------------------
    # WRITE
    # -----------------------------------------------------------------------

    def file(self, fda: FDA) -> dict[str, str]:
        """
        File field values using FILE^DIE (no audit, no key check).
        Returns a dict mapping temp IENS "+1," → newly assigned IEN.
        """
        return self._call_die("FILE^DIE", fda)

    def update(self, fda: FDA) -> dict[str, str]:
        """
        File field values using UPDATE^DIE (with audit + key validation).
        Returns a dict mapping temp IENS → newly assigned IEN (for new entries).
        """
        return self._call_die("UPDATE^DIE", fda)

    def _call_die(self, entry_point: str, fda: FDA) -> dict[str, str]:
        """Serialise FDA, call DIE entry point, check errors, return IEN map."""
        fda_node = f"FMFDA{id(self)}"
        err_node = f"FMERR{id(self)}"

        self._write_fda(fda_node, fda)
        self._conn.call(entry_point, ["", fda_node, err_node])
        self._check_errors(err_node)

        ien_map = self._read_ien_map(fda_node, fda)
        self._kill_nodes(fda_node, err_node)
        return ien_map

    def _write_fda(self, fda_node: str, fda: FDA) -> None:
        """Set FDA global nodes for M to read."""
        if not hasattr(self._conn, "set_global"):
            raise NotImplementedError("FDA write requires YDB embedded connection")
        for file, iens_map in fda.data.items():
            for iens, fields in iens_map.items():
                for field_num, value in fields.items():
                    self._conn.set_global(fda_node, [file, iens, field_num], value)

    def _read_ien_map(self, fda_node: str, fda: FDA) -> dict[str, str]:
        """
        After FILE^DIE, new IENs are placed back in the FDA:
        FDA(file,"+1,") = new_ien
        """
        result: dict[str, str] = {}
        if not hasattr(self._conn, "get_global"):
            return result
        for file, iens_map in fda.data.items():
            for iens in iens_map:
                if iens.startswith("+"):
                    new_ien = self._conn.get_global(fda_node, [file, iens])
                    if new_ien:
                        result[iens] = new_ien
        return result

    def validate_field(
        self, file: str, ien: str, field: str, value: str
    ) -> tuple[bool, str]:
        """
        Validate a value against a field's INPUT transform without filing.
        Returns (valid: bool, error_message: str).
        """
        result_node = f"FMCHK{id(self)}"
        self._conn.call("CHK^DIE", [file, ien + ",", field, value, result_node])
        error = self._conn.call("$$GET1^DIQ", [result_node, "1,", ".01", "E"])
        if error.strip():
            return False, error.strip()
        return True, ""

    # -----------------------------------------------------------------------
    # SCHEMA
    # -----------------------------------------------------------------------

    def get_field_def(self, file: str, field: str) -> dict[str, str]:
        """Retrieve data dictionary attributes for a field via FIELD^DID."""
        result_node = f"FMDD{id(self)}"
        self._conn.call("FIELD^DID", [file, field, "", result_node])
        attrs: dict[str, str] = {}
        if hasattr(self._conn, "get_global"):
            import yottadb
            attr = yottadb.subscript_next(result_node, [""])
            while attr:
                attrs[attr] = self._conn.get_global(result_node, [attr])
                attr = yottadb.subscript_next(result_node, [attr])
            self._conn.kill_global(result_node, [])
        return attrs

    # -----------------------------------------------------------------------
    # INTERNAL HELPERS
    # -----------------------------------------------------------------------

    def _check_errors(self, err_node: str) -> None:
        if not hasattr(self._conn, "get_global"):
            return
        import yottadb
        count = self._conn.get_global(err_node, ["DIERR"])
        if count and count != "0":
            errors: dict[str, str] = {}
            i = yottadb.subscript_next(err_node + "DIERR", [""])
            while i:
                msg = self._conn.get_global(err_node + "DIERR", [i, "TEXT", "1"])
                errors[i] = msg
                i = yottadb.subscript_next(err_node + "DIERR", [i])
            raise FileManError(errors)

    def _check_dierr_ydb(self) -> None:
        if not hasattr(self._conn, "get_global"):
            return
        count = self._conn.get_global("DIERR", [])
        if count and count != "0":
            raise FileManError({"1": "FileMan reported an error (check DIERR global)"})

    def _kill_nodes(self, *nodes: str) -> None:
        for node in nodes:
            if hasattr(self._conn, "kill_global"):
                self._conn.kill_global(node, [])
```

### Usage Example (Python)

```python
from fileman.ydb_connection import YDBConnection
from fileman.client import FileManClient, FDA

# YDB embedded — process running on the VistA server
conn = YDBConnection(duz="1", duz_zero="@")
fm = FileManClient(conn)

# READ: get patient name and DOB
patient = fm.get_entry(file="2", ien="100", fields=".01;.03")
print(patient.external[".01"])   # "SMITH,JOHN"
print(patient.external[".03"])   # "JAN 15,1960"

# LOOKUP: find patient IEN by name
ien = fm.find_one(file="2", index="B", value="SMITH,JOHN")

# WRITE: create a new entry in a custom file
fda = FDA()
fda.set(file="99001", iens="+1,", field_num=".01", value="TEST ENTRY")
fda.set(file="99001", iens="+1,", field_num="1", value="some value")
new_iens = fm.file(fda)
print(new_iens)   # {"+1,": "23"}  — new entry got IEN 23

# VALIDATE: check a value before filing
valid, msg = fm.validate_field(file="2", ien="100", field=".03", value="T")
```

---

## Go Wrapper Implementation

### Module setup

```bash
mkdir fileman-go && cd fileman-go
go mod init github.com/yourorg/fileman
```

### Connection interface

```go
// fileman/connection.go
package fileman

// Connection is the transport abstraction.
// Implement BrokerConn for TCP RPC Broker or YDBConn for YottaDB embedded.
type Connection interface {
    // Call invokes an M entry point and returns the raw result string.
    Call(routine string, args []string) (string, error)
    Close() error
}
```

### YottaDB embedded connection (Go via cgo)

```go
// fileman/ydb_conn.go
package fileman

// #cgo CFLAGS: -I/usr/local/lib/yottadb
// #cgo LDFLAGS: -L/usr/local/lib/yottadb -lyottadb
// #include "libyottadb.h"
import "C"
import (
    "fmt"
    lang_yottadb "lang.yottadb.com/go/yottadb"
)

// YDBConn calls FileMan DBS routines via YottaDB's Go API.
// The process must be co-located with YottaDB; YOTTADB env must be set.
type YDBConn struct {
    duz     string
    duzZero string
}

func NewYDBConn(duz, duzZero string) (*YDBConn, error) {
    c := &YDBConn{duz: duz, duzZero: duzZero}
    // Set Kernel context globals
    if err := lang_yottadb.SetValE(lang_yottadb.NOTTP, nil, duz, "DUZ"); err != nil {
        return nil, fmt.Errorf("set DUZ: %w", err)
    }
    if err := lang_yottadb.SetValE(lang_yottadb.NOTTP, nil, duzZero, "DUZ", "0"); err != nil {
        return nil, fmt.Errorf("set DUZ(0): %w", err)
    }
    return c, nil
}

func (c *YDBConn) Call(routine string, args []string) (string, error) {
    // For simple extrinsic functions ($$FIND1^DIC, $$GET1^DIQ, etc.)
    result, err := lang_yottadb.CallMT(lang_yottadb.NOTTP, nil, 0, routine, args...)
    if err != nil {
        return "", fmt.Errorf("M call %s: %w", routine, err)
    }
    return result, nil
}

func (c *YDBConn) GetGlobal(varname string, subs ...string) (string, error) {
    val, err := lang_yottadb.ValE(lang_yottadb.NOTTP, nil, varname, subs...)
    if err != nil {
        return "", err
    }
    return val, nil
}

func (c *YDBConn) SetGlobal(value, varname string, subs ...string) error {
    return lang_yottadb.SetValE(lang_yottadb.NOTTP, nil, value, varname, subs...)
}

func (c *YDBConn) KillGlobal(varname string, subs ...string) error {
    return lang_yottadb.DeleteE(lang_yottadb.NOTTP, nil, lang_yottadb.YDB_DEL_TREE,
        varname, subs...)
}

func (c *YDBConn) Close() error { return nil }
```

### RPC Broker connection (Go TCP)

```go
// fileman/broker_conn.go
package fileman

import (
    "fmt"
    "net"
    "strings"
    "time"
)

// BrokerConn speaks the VistA XWB RPC Broker wire protocol over TCP.
type BrokerConn struct {
    host string
    port int
    conn net.Conn
}

const brokerEOT = "\x04"

func NewBrokerConn(host string, port int, access, verify string) (*BrokerConn, error) {
    c := &BrokerConn{host: host, port: port}
    conn, err := net.DialTimeout("tcp",
        fmt.Sprintf("%s:%d", host, port), 30*time.Second)
    if err != nil {
        return nil, fmt.Errorf("dial broker: %w", err)
    }
    c.conn = conn
    if err := c.handshake(access, verify); err != nil {
        conn.Close()
        return nil, err
    }
    return c, nil
}

func (c *BrokerConn) handshake(access, verify string) error {
    hostname, _ := getHostname()
    if _, err := c.Call("TCPConnect", []string{hostname, "0", "9200"}); err != nil {
        return fmt.Errorf("TCPConnect: %w", err)
    }
    resp, err := c.Call("XUS SIGNON", []string{access + ";" + verify})
    if err != nil {
        return fmt.Errorf("signon RPC: %w", err)
    }
    if !strings.HasPrefix(resp, "0") {
        return fmt.Errorf("signon rejected: %q", resp)
    }
    return nil
}

// buildPacket encodes an RPC call in XWB wire format.
func buildPacket(name string, args []string) []byte {
    var argStr strings.Builder
    for _, a := range args {
        argStr.WriteString(fmt.Sprintf("\x00%03d%s", len(a), a))
    }
    body := fmt.Sprintf("\x0f%03d%s5%04d%s", len(name), name, argStr.Len(), argStr.String())
    header := fmt.Sprintf("[NS]%05d", len(body))
    return []byte(header + body + brokerEOT)
}

func (c *BrokerConn) Call(routine string, args []string) (string, error) {
    packet := buildPacket(routine, args)
    if _, err := c.conn.Write(packet); err != nil {
        return "", fmt.Errorf("write: %w", err)
    }
    return c.recv()
}

func (c *BrokerConn) recv() (string, error) {
    var buf []byte
    tmp := make([]byte, 4096)
    for {
        n, err := c.conn.Read(tmp)
        if n > 0 {
            buf = append(buf, tmp[:n]...)
        }
        if err != nil || (len(buf) > 0 && buf[len(buf)-1] == brokerEOT[0]) {
            break
        }
    }
    return strings.TrimRight(string(buf), brokerEOT), nil
}

func (c *BrokerConn) Close() error {
    c.Call("BYE", []string{}) //nolint:errcheck
    return c.conn.Close()
}

func getHostname() (string, error) {
    // truncate to 24 chars per XWB spec
    h, err := net.LookupAddr("127.0.0.1")
    if err != nil || len(h) == 0 {
        return "localhost", nil
    }
    s := strings.TrimSuffix(h[0], ".")
    if len(s) > 24 {
        s = s[:24]
    }
    return s, nil
}
```

### FileMan Client (Go)

```go
// fileman/client.go
package fileman

import (
    "fmt"
    "strconv"
)

// Entry holds field values retrieved by GETS^DIQ.
type Entry struct {
    File     string
    IEN      string
    Fields   map[string]string // field# → internal value
    External map[string]string // field# → external (display) value
}

// FDA (FileMan Data Array) represents values to file via FILE^DIE / UPDATE^DIE.
// FDA[file][iens][field] = value
// IENS for new entries: "+1,"; existing: "23,"
type FDA map[string]map[string]map[string]string

func (f FDA) Set(file, iens, field, value string) {
    if f[file] == nil {
        f[file] = make(map[string]map[string]string)
    }
    if f[file][iens] == nil {
        f[file][iens] = make(map[string]string)
    }
    f[file][iens][field] = value
}

// FileManError carries error messages from the DIERR array.
type FileManError struct {
    Errors map[string]string
}

func (e *FileManError) Error() string {
    return fmt.Sprintf("FileMan error: %v", e.Errors)
}

// Client wraps FileMan DBS calls over a Connection.
type Client struct {
    conn YDBConn // use interface if supporting both transports
    seq  int     // unique node suffix for temp globals
}

func NewClient(conn YDBConn) *Client {
    return &Client{conn: conn}
}

func (c *Client) nextNode(prefix string) string {
    c.seq++
    return fmt.Sprintf("%s%d", prefix, c.seq)
}

// GetField returns a single field value (external format) via $$GET1^DIQ.
func (c *Client) GetField(file, ien, field string) (string, error) {
    result, err := c.conn.Call("$$GET1^DIQ",
        []string{file, ien + ",", field, "E", "", ""})
    if err != nil {
        return "", err
    }
    return result, nil
}

// FindOne returns the IEN of the first entry matching value on index B
// (or another named cross-reference). Returns "" if not found.
func (c *Client) FindOne(file, index, value string) (string, error) {
    result, err := c.conn.Call("$$FIND1^DIC",
        []string{file, "", index, value, ""})
    if err != nil {
        return "", err
    }
    ien := result
    if ien == "0" || ien == "" {
        return "", nil
    }
    return ien, nil
}

// GetEntry retrieves fields for one entry via GETS^DIQ.
// fields: semicolon-separated field numbers, e.g. ".01;.03;1"
// Use "*" for all fields.
func (c *Client) GetEntry(file, ien, fields string) (*Entry, error) {
    resultNode := c.nextNode("^||FMQRY")
    _, err := c.conn.Call("GETS^DIQ",
        []string{file, ien + ",", fields, "EIN", "", resultNode})
    if err != nil {
        return nil, fmt.Errorf("GETS^DIQ: %w", err)
    }
    entry, err := c.readGETSResult(resultNode, file, ien)
    c.conn.KillGlobal(resultNode) //nolint:errcheck
    return entry, err
}

func (c *Client) readGETSResult(node, file, ien string) (*Entry, error) {
    entry := &Entry{
        File:     file,
        IEN:      ien,
        Fields:   make(map[string]string),
        External: make(map[string]string),
    }
    // Iterate result(file, ien+",", field)
    // YottaDB Go API: SubNextE to walk subscripts
    var fieldSub string
    for {
        next, err := lang_yottadb_SubNextE(node, file, ien+",", fieldSub)
        if err != nil || next == "" {
            break
        }
        val, _ := c.conn.GetGlobal(node, file, ien+",", next)
        ext, _ := c.conn.GetGlobal(node, file, ien+",", next, "E")
        entry.Fields[next] = val
        if ext != "" {
            entry.External[next] = ext
        }
        fieldSub = next
    }
    return entry, nil
}

// File creates or updates entries using FILE^DIE (no audit).
// Returns a map of temporary IENS → new IEN for created entries.
func (c *Client) File(fda FDA) (map[string]string, error) {
    return c.callDIE("FILE^DIE", fda)
}

// Update creates or updates entries using UPDATE^DIE (with audit + key check).
func (c *Client) Update(fda FDA) (map[string]string, error) {
    return c.callDIE("UPDATE^DIE", fda)
}

func (c *Client) callDIE(entryPoint string, fda FDA) (map[string]string, error) {
    fdaNode := c.nextNode("^||FMFDA")
    errNode := c.nextNode("^||FMERR")

    if err := c.writeFDA(fdaNode, fda); err != nil {
        return nil, err
    }
    if _, err := c.conn.Call(entryPoint,
        []string{"", fdaNode, errNode}); err != nil {
        return nil, fmt.Errorf("%s: %w", entryPoint, err)
    }
    if err := c.checkErrors(errNode); err != nil {
        c.conn.KillGlobal(fdaNode)  //nolint:errcheck
        c.conn.KillGlobal(errNode)  //nolint:errcheck
        return nil, err
    }
    ienMap := c.readIENMap(fdaNode, fda)
    c.conn.KillGlobal(fdaNode) //nolint:errcheck
    c.conn.KillGlobal(errNode) //nolint:errcheck
    return ienMap, nil
}

func (c *Client) writeFDA(node string, fda FDA) error {
    for file, ienMap := range fda {
        for iens, fields := range ienMap {
            for field, value := range fields {
                if err := c.conn.SetGlobal(value, node, file, iens, field); err != nil {
                    return fmt.Errorf("write FDA node: %w", err)
                }
            }
        }
    }
    return nil
}

func (c *Client) readIENMap(node string, fda FDA) map[string]string {
    result := make(map[string]string)
    for file, ienMap := range fda {
        for iens := range ienMap {
            if len(iens) > 0 && iens[0] == '+' {
                if newIEN, err := c.conn.GetGlobal(node, file, iens); err == nil && newIEN != "" {
                    result[iens] = newIEN
                }
            }
        }
    }
    return result
}

func (c *Client) checkErrors(errNode string) error {
    count, err := c.conn.GetGlobal(errNode, "DIERR")
    if err != nil || count == "" || count == "0" {
        return nil
    }
    n, _ := strconv.Atoi(count)
    errors := make(map[string]string, n)
    for i := 1; i <= n; i++ {
        idx := strconv.Itoa(i)
        msg, _ := c.conn.GetGlobal(errNode, "DIERR", idx, "TEXT", "1")
        errors[idx] = msg
    }
    return &FileManError{Errors: errors}
}

// lang_yottadb_SubNextE is a placeholder — use the real yottadb.SubNextE API.
func lang_yottadb_SubNextE(gvn string, subs ...string) (string, error) {
    return lang_yottadb.SubNextE(lang_yottadb.NOTTP, nil, gvn, subs...)
}
```

### Usage Example (Go)

```go
package main

import (
    "fmt"
    "log"

    "github.com/yourorg/fileman"
)

func main() {
    // YDB embedded — co-located with YottaDB
    conn, err := fileman.NewYDBConn("1", "@")
    if err != nil {
        log.Fatal(err)
    }
    defer conn.Close()

    fm := fileman.NewClient(*conn)

    // READ: get patient name
    entry, err := fm.GetEntry("2", "100", ".01;.03")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(entry.External[".01"])  // "SMITH,JOHN"
    fmt.Println(entry.External[".03"])  // "JAN 15,1960"

    // LOOKUP
    ien, err := fm.FindOne("2", "B", "SMITH,JOHN")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("IEN:", ien)

    // WRITE: create a new entry
    fda := make(fileman.FDA)
    fda.Set("99001", "+1,", ".01", "TEST ENTRY")
    fda.Set("99001", "+1,", "1", "some value")

    newIENs, err := fm.File(fda)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Created IEN: %s\n", newIENs["+1,"])
}
```

---

## Data Conventions and Type Mapping

### FileMan Dates

FileMan dates are stored internally as `YYYMMDD` (year offset from 1700, not 1900).
**Never parse manually.** Always convert via `%DT` or `$$DT^XLFDT`.

```python
# Python: convert FileMan internal date → Python datetime
def fm_date_to_datetime(fm_date: str) -> datetime:
    """Convert FileMan internal date (e.g. '3240115') to datetime."""
    year = int(fm_date[:3]) + 1700
    month = int(fm_date[3:5])
    day = int(fm_date[5:7])
    return datetime(year, month, day)

def datetime_to_fm_date(dt: datetime) -> str:
    """Convert datetime to FileMan internal date."""
    return f"{dt.year - 1700}{dt.month:02d}{dt.day:02d}"
```

```go
// Go: convert FileMan internal date → time.Time
func FMDateToTime(fmDate string) (time.Time, error) {
    if len(fmDate) < 7 {
        return time.Time{}, fmt.Errorf("invalid FM date: %q", fmDate)
    }
    century, _ := strconv.Atoi(fmDate[:3])
    year := century + 1700
    month, _ := strconv.Atoi(fmDate[3:5])
    day, _ := strconv.Atoi(fmDate[5:7])
    return time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.UTC), nil
}
```

### Pointer Fields

Pointer fields store an IEN — not the human-readable value. When calling
`GETS^DIQ` with the `"E"` flag, FileMan resolves pointers and returns the
external (display) value. Store the **external** value for display; store
the **IEN** for programmatic operations.

```python
# The "E" subscript in the result array is the external value
internal_ien = patient.fields[".05"]    # "42"   (pointer to MARITAL STATUS file)
external_val = patient.external[".05"]  # "MARRIED"
```

### IENS (Internal Entry Number String)

The IENS encodes a path through nested levels of a FileMan file:

```
Simple entry in file 2:       "100,"        → IEN 100 in file 2
Sub-file entry:               "3,100,"      → sub-IEN 3 of parent 100
New entry placeholder:        "+1,"
New sub-entry placeholder:    "+1,100,"
```

Always include the trailing comma.

### Multiple-valued fields (Sub-files)

To read a multiple, pass the sub-file number in `GETS^DIQ`:

```python
# Read all entries in the ADDRESS sub-file (file 2, field .11x)
# The sub-file number for PATIENT ADDRESSes is 2.11
result = fm.get_entry(file="2", ien="100", fields=".11:*")
```

To write a new sub-entry:

```python
fda = FDA()
fda.set(file="2.11", iens="+1,100,", field_num=".01", value="HOME")
fda.set(file="2.11", iens="+1,100,", field_num="1.1", value="123 MAIN ST")
fm.file(fda)
```

---

## Error Handling and Status Codes

FileMan returns errors in a `DIERR` array. The structure is:

```mumps
DIERR          = number of errors
DIERR(n)       = error code
DIERR(n,"TEXT",1) = error message text
DIERR(n,"TEXT",2) = continuation line (if any)
```

Common error codes:

| DIERR Code | Meaning |
|---|---|
| 1 | Field not found |
| 2 | File not found |
| 4 | Invalid value for field |
| 5 | Required field missing |
| 7 | Key uniqueness violation |
| 501 | Insufficient access (file or field security) |

Your wrapper should always check `DIERR` after any write call and raise/return
a typed error. Read calls set `^TMP("DIERR",$J)` on error — check this too.

---

## Worked Examples: Read and Write Patterns

### Pattern 1: Patient Lookup by Name

```python
# Find patient by name, retrieve demographic fields
ien = fm.find_one(file="2", index="B", value="SMITH,JOHN")
if ien is None:
    raise ValueError("Patient not found")

patient = fm.get_entry(
    file="2",
    ien=ien,
    fields=".01;.02;.03;.05;.09",   # name, sex, DOB, marital, ssn
)
print(f"Name:  {patient.external['.01']}")
print(f"DOB:   {patient.external['.03']}")
print(f"Sex:   {patient.external['.02']}")
```

### Pattern 2: Create a New Entry

```python
fda = FDA()
# "+1," = placeholder for new IEN in file 99001
fda.set("99001", "+1,", ".01", "MY NEW RECORD")
fda.set("99001", "+1,", "1",   "active")
fda.set("99001", "+1,", "2",   "3260407")  # FileMan date: Apr 7 2026

new_iens = fm.file(fda)    # {"+1,": "42"}
new_ien = new_iens["+1,"]
print(f"Created record IEN: {new_ien}")
```

### Pattern 3: Update an Existing Entry

```python
# Update field 1 of IEN 42 — use "42," (IEN + comma)
fda = FDA()
fda.set("99001", "42,", "1", "inactive")
fm.update(fda)   # UPDATE^DIE: audits the change, enforces keys
```

### Pattern 4: List Entries in a Range

```python
# Find all patients whose names start with "SMITH"
iens = fm.find(file="2", index="B", value="SMITH", max_results=50)
for ien in iens:
    name = fm.get_field(file="2", ien=ien, field=".01")
    print(f"IEN {ien}: {name}")
```

### Pattern 5: Read a Multiple (Sub-file)

```python
# Read all PHARMACY PATIENT (#55) entries for patient IEN 100
# Sub-file 55.03 = medication profile entries
med_iens = fm.find(file="55.03", index="B", value="")
for sub_ien in med_iens:
    drug_name = fm.get_field(file="55.03", ien=sub_ien, field=".01")
    print(drug_name)
```

---

## Security and Context Setup

FileMan checks two variables at runtime to determine what the caller is allowed to do:

| Variable | Meaning | Value |
|---|---|---|
| `DUZ` | User IEN in NEW PERSON file (#200) | e.g. `"1"` |
| `DUZ(0)` | Access level | `"@"` = programmer (unrestricted) |

For application servers, set `DUZ` to the service account's IEN in file 200 and set
`DUZ(0)` to the minimum required access codes for the files you're reading/writing.

**Never use `DUZ(0)="@"` in production application code.** Programmer mode bypasses
all FileMan security. Use it only for DBA tools.

File-level access codes are strings like `"RN"` (read) or `"WN"` (write+read). Each
VistA site assigns these in the File (#1) data dictionary. Your service account's
access codes are stored in the NEW PERSON file — consult your VistA DBA.

---

## Testing Strategy

### Unit tests — no VistA required

Implement a `FakeConnection` that returns canned M array responses. Test all
type conversion logic (dates, pointers, IENS) and error handling against the
fake.

```python
# tests/test_client.py
class FakeConnection(FileManConnection):
    def __init__(self, responses: dict[str, str]):
        self._responses = responses
        self._globals: dict[str, str] = {}

    def call(self, routine, args):
        key = f"{routine}:{':'.join(args)}"
        return self._responses.get(key, "")

    def get_global(self, gvn, subs):
        return self._globals.get(gvn + str(subs), "")

    def set_global(self, gvn, subs, value):
        self._globals[gvn + str(subs)] = value

    def kill_global(self, gvn, subs):
        prefix = gvn + str(subs)
        for k in list(self._globals):
            if k.startswith(prefix):
                del self._globals[k]

    def close(self): pass
```

### Integration tests — real YottaDB

Mark tests that require a running VistA instance with `@pytest.mark.network`.
Run against a FOIA VistA or GT.M development instance.

```python
@pytest.mark.network
def test_get_patient_entry(fm_client):
    # Requires FOIA VistA with known patient data
    entry = fm_client.get_entry("2", "1", ".01")
    assert entry.external[".01"]  # should have a name value
```

### Go integration tests

```go
//go:build integration
// +build integration

func TestGetEntry(t *testing.T) {
    conn, err := fileman.NewYDBConn("1", "@")
    require.NoError(t, err)
    fm := fileman.NewClient(*conn)

    entry, err := fm.GetEntry("2", "1", ".01")
    require.NoError(t, err)
    assert.NotEmpty(t, entry.External[".01"])
}
```

---

## Deployment Considerations

### YottaDB embedded (co-located service)

- Process must have `YOTTADB`, `gtmroutines`, `gtmgbldir` env vars set.
- The M routines directory must include `_DI*` (FileMan), `_XU*` (Kernel), and
  your application routines in `gtmroutines`.
- Run as a system account with read permission on the global directory (`.gld`/`.dat`).
- One process per connection — YottaDB's STM threading model means you need a
  process-per-goroutine or process-per-thread architecture, or use the async YDB API.

### RPC Broker (remote service)

- Broker default port: 9200. Firewall rules apply.
- Each connection creates a dedicated M job on the server — pool connections.
- Use TLS termination (stunnel or VistA TLS patch `XWB*8.0*10707`) for production.
- The XWB broker is stateful: `DUZ` is set once at signon; RPCs run in that context.
- Implement connection health checks — brokers can timeout after idle periods.

### Capability wrapper vs direct FileMan RPC

If you are deploying the RPC Broker path, you have two choices:

1. **Custom FileMan RPCs on the M side** — write M wrapper routines that accept
   parameters, call DBS APIs, pack results, and register the wrappers as RPCs in
   the REMOTE PROCEDURE (#8994) file. Your Go/Python client calls these named RPCs.

2. **Generic "EXECUTE" RPC** — some VistA configurations allow an `XWB DIRECT EXECUTE`
   RPC that runs arbitrary M code. This requires programmer access on the account and
   should be restricted to trusted internal services only.

Option 1 is recommended: it gives you auditability, access control per-RPC via Kernel
keys, and prevents client-side M injection.

### Concurrency

FileMan is not thread-safe at the M global level. For high-throughput Go/Python
services:
- **YDB embedded:** use a worker pool with one YDB connection per goroutine/thread.
  YottaDB's `YDBPOSIX` API provides async global operations for read-heavy workloads.
- **RPC Broker:** each TCP connection maps to an M job; the broker handles serialisation
  within each job. Maintain a connection pool sized to the site's M job limit
  (typically 50–200 concurrent jobs per VistA instance).

---

## References

- VA FileMan 22.2 DBS API Reference — `~/data/vista-docs/guides/va_fileman_guide.md`
- YottaDB Go Wrapper — `lang.yottadb.com/go/yottadb`
- YottaDB Python Wrapper — `pypi.org/project/yottadb`
- VistA RPC Broker (XWB) documentation — VDL package XWB
- FMQL — `github.com/caregraf/FMQL`
- nodeVISTA / MVDM — `github.com/vistadataproject/nodeVISTA`
- FOIA VistA (test instance) — `github.com/OSEHRA/VistA`
