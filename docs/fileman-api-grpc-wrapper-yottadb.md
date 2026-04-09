# VA FileMan API Wrapper — YottaDB Implementation Guide

**Building the FileMan gRPC Gateway on YottaDB**

*Version 1.0 — April 2026*
*Audience: Implementation engineers deploying the FileMan API wrapper on a VistA system running YottaDB*

*Part of the VA FileMan External API Wrapper series. See the [Comprehensive Specification](fileman-api-wrapper-specification.md) for architecture, API surface, wire protocol, and security design.*

---

## Overview

This guide covers the complete, practical implementation of the FileMan API wrapper gRPC Gateway on a VistA system running YottaDB. It assumes:

- YottaDB is already installed with a working VistA instance
- FileMan 22.2 routines (`DI*` namespace) are installed and operational in the YottaDB global directory
- The reader is familiar with the two-layer gRPC architecture described in the [Comprehensive Specification](fileman-api-wrapper-specification.md) §6 and §19

For the InterSystems IRIS implementation, see [fileman-api-grpc-wrapper-iris.md](fileman-api-grpc-wrapper-iris.md).

YottaDB is an open-source, high-performance M/MUMPS runtime and database engine that has become the primary platform for open-source VistA deployments. It is fully compatible with ANSI Standard M and with the GT.M runtime from which it was forked. All FileMan DBS API entry points run without modification on YottaDB.

---

## Table of Contents

1. [YottaDB Architecture Fundamentals](#1-yottadb-architecture-fundamentals)
2. [Prerequisites and Environment Setup](#2-prerequisites-and-environment-setup)
3. [Connection Mechanism 1: YottaDB C Binding](#3-connection-mechanism-1-yottadb-c-binding-recommended-for-grpc-gateway)
4. [Connection Mechanism 2: YottaDB Python Binding](#4-connection-mechanism-2-yottadb-python-binding)
5. [Connection Mechanism 3: YottaDB Go Binding](#5-connection-mechanism-3-yottadb-go-binding)
6. [Implementing the YDBRuntime for the gRPC Gateway](#6-implementing-the-ydbruntime-for-the-grpc-gateway)
7. [Error Handling on YottaDB](#7-error-handling-on-yottadb)
8. [Testing on YottaDB](#8-testing-on-yottadb)
9. [Deployment Checklist](#9-deployment-checklist)

---

## 1. YottaDB Architecture Fundamentals

Understanding how YottaDB organizes its runtime is essential before implementing the wrapper. YottaDB's model differs from IRIS in several important ways.

### Global Directory and Database Files

YottaDB does not use namespaces. Instead, it uses a **global directory** (a `.gld` file) that maps global name prefixes to physical database files (`.dat` files). For example:

| Global Root | Database File | Notes |
|---|---|---|
| `^DPT(` | `patient.dat` | PATIENT file data |
| `^PS(` | `pharmacy.dat` | DRUG file data |
| `^DD(` | `fileman.dat` | Data Dictionary |
| `^OR(` | `orders.dat` | ORDER data |
| `*` (default) | `vista.dat` | All unmapped globals |

The global directory is specified by the `gtmgbldir` (or `ydb_gbldir`) environment variable. The wrapper process inherits the global directory from its environment — no code change is needed. This is simpler than IRIS's namespace model: global name resolution is automatic once the environment is configured.

### M Routine Search Path

YottaDB locates M source and object routines through the `gtmroutines` (or `ydb_routines`) environment variable, which is an ordered list of directories. FileMan routines (`DI*`) must be in one of these directories. The call-in interface requires YottaDB to find the routine object files at call time — if `gtmroutines` is misconfigured, FileMan calls fail with `%GTM-E-ZLINKFILE` errors.

### The YottaDB Process Model

Unlike IRIS, which uses a single shared M engine that all embedded connections attach to, **each YottaDB call-in connection is an independent M process**. The process has its own:
- Local symbol table (local variables like `DUZ`, `DT` are per-process)
- M stack
- Lock table partition

Global storage (`^DPT`, `^DD`, etc.) is shared across all M processes via the database files, protected by YottaDB's journal and locking infrastructure.

For the gRPC Gateway, this means each concurrent gRPC worker thread that calls `ydb_init()` has its own isolated M process context. There is no license-per-process constraint as with IRIS — YottaDB is open-source with no per-connection licensing. The practical concurrency limit is CPU and I/O throughput of the database files.

### Multi-Threaded Call-In

YottaDB 1.34+ supports multi-threaded call-in: each thread calls `ydb_init()` independently and gets its own YottaDB channel. Threads share the same global database files (via the global directory) but have completely isolated local symbol tables. This is the correct model for the gRPC Gateway: one `ydb_init()` call per gRPC worker goroutine/thread at startup, `ydb_exit()` at shutdown.

---

## 2. Prerequisites and Environment Setup

### YottaDB Version

YottaDB r1.34 or later is recommended. The multi-threaded call-in mechanism and the Python binding (`yottadb` PyPI package) require r1.30+.

### Required Components

| Component | Source | Purpose |
|---|---|---|
| `libyottadb.so` + `libyottadb.h` | YottaDB installation | C binding for embedded call-in |
| `yottadb` PyPI package | `pip install yottadb` | Python binding |
| `lang.yottadb.com/go/yottadb` | Go module | Go binding |
| FileMan routines (`DI*`) | VistA KIDS build or DSV | FileMan DBS entry points |
| Global directory (`.gld`) | VistA installation | Maps globals to database files |

### Environment Variables

| Variable | Value | Purpose |
|---|---|---|
| `ydb_dist` (or `YOTTADB`) | `/usr/local/lib/yottadb/r134` | YottaDB installation directory |
| `gtmroutines` (or `ydb_routines`) | `$ydb_dist/libyottadbutil.so /path/to/vista/routines` | M routine object search path |
| `gtmgbldir` (or `ydb_gbldir`) | `/path/to/vista/mumps.gld` | Global directory |
| `ydb_ci` | `/path/to/fileman_callin.ci` | Call-in table (§3) |
| `LD_LIBRARY_PATH` | `$ydb_dist` | Locates `libyottadb.so` |

Unlike IRIS, YottaDB has no concept of `$NAMESPACE` — once the environment variables are set, all global access resolves through the global directory automatically.

### Verify YottaDB is Operational

```bash
# Confirm YottaDB is installed and accessible
$ydb_dist/ydb -run %XCMD 'WRITE $$DT^XLFDT(),!'
# Should print a 7-digit FileMan date, e.g.: 3260409

# Confirm the global directory is valid
$ydb_dist/mupip info -region DEFAULT
```

The `$$DT^XLFDT()` call verifies that both YottaDB and the Kernel routines (XU package) are installed and reachable via `gtmroutines`.

---

## 3. Connection Mechanism 1: YottaDB C Binding (Recommended for gRPC Gateway)

The YottaDB C binding (`libyottadb.h`) is the primary mechanism for the gRPC Gateway. It provides sub-millisecond call latency, no network overhead, and direct access to the M runtime without spawning a separate process.

### The `libyottadb.h` API

Link against `$ydb_dist/libyottadb.so`. The key functions are:

**Session management:**

| Function | Signature | Purpose |
|---|---|---|
| `ydb_init` | `int ydb_init(void)` | Initialize the YottaDB runtime for the calling thread |
| `ydb_exit` | `int ydb_exit(void)` | Shut down the YottaDB runtime for the calling thread |
| `ydb_ci` | `int ydb_ci(const char *rtn, ...)` | Call an M routine via call-in table |
| `ydb_cip` | `int ydb_cip(ci_name_descriptor *rtn, ...)` | Call via pre-parsed descriptor (faster for repeated calls) |

**Global operations:**

| Function | Signature | Purpose |
|---|---|---|
| `ydb_get_s` | `int ydb_get_s(ydb_buffer_t *varname, int nsubs, ydb_buffer_t *subsarray, ydb_buffer_t *retval)` | Get a global/local node value |
| `ydb_set_s` | `int ydb_set_s(ydb_buffer_t *varname, int nsubs, ydb_buffer_t *subsarray, ydb_buffer_t *value)` | Set a global/local node value |
| `ydb_delete_s` | `int ydb_delete_s(ydb_buffer_t *varname, int nsubs, ydb_buffer_t *subsarray, int deltype)` | Kill node (`YDB_DEL_NODE`) or tree (`YDB_DEL_TREE`) |
| `ydb_subscript_next_s` | `int ydb_subscript_next_s(ydb_buffer_t *varname, int nsubs, ydb_buffer_t *subsarray, ydb_buffer_t *retval)` | Forward subscript iteration (`$ORDER`) |
| `ydb_subscript_previous_s` | same pattern | Backward `$ORDER` |
| `ydb_data_s` | `int ydb_data_s(ydb_buffer_t *varname, int nsubs, ydb_buffer_t *subsarray, unsigned int *retval)` | `$DATA` — node existence and descendant check |
| `ydb_lock_s` | `int ydb_lock_s(uint64_t timeout, int count, ...)` | Incremental LOCK |
| `ydb_unlock_all` | `int ydb_unlock_all(void)` | Release all locks held by this process |

The `ydb_buffer_t` structure carries a string value:

```c
typedef struct {
    unsigned int  len_alloc;  // allocated buffer size
    unsigned int  len_used;   // actual data length
    char         *buf_addr;   // pointer to string data
} ydb_buffer_t;
```

### Setting the FileMan Security Context

Before any FileMan call, set `DUZ`, `DUZ(0)`, and `DT` in the M local symbol table:

```c
#include "libyottadb.h"

// Set DUZ = "1"
ydb_buffer_t duz_var = {3, 3, "DUZ"};
ydb_buffer_t duz_val = {1, 1, "1"};
ydb_set_s(&duz_var, 0, NULL, &duz_val);

// Set DUZ(0) = "@"  (programmer access)
ydb_buffer_t zero_sub = {1, 1, "0"};
ydb_buffer_t at_val   = {1, 1, "@"};
ydb_set_s(&duz_var, 1, &zero_sub, &at_val);

// Set DT = current FileMan date via Kernel
// Use ydb_ci to call $$DT^XLFDT() and capture the result,
// then ydb_set_s to store it in DT.
ydb_buffer_t dt_var = {2, 2, "DT"};
char dt_buf[16];
ydb_buffer_t dt_val = {16, 7, dt_buf};  // 7 chars, e.g. "3260409"
// ... call $$DT^XLFDT() via ydb_ci to populate dt_buf, then:
ydb_set_s(&dt_var, 0, NULL, &dt_val);
```

`DUZ(0)="@"` is programmer access (unrestricted). For production sessions, set `DUZ(0)` to the actual access codes from the service account's `NEW PERSON` (#200) entry.

### The Call-In Table

YottaDB call-in requires a **call-in table** — a text file declaring each M entry point, its return type, and its argument types. Set `ydb_ci` environment variable to the path of this file.

```
# fileman_callin.ci — FileMan DBS call-in table for YottaDB
#
# Format: alias: return_type label^routine(direction:type, ...)
# I = input, O = output, IO = input/output
# ydb_char_t* = null-terminated string; ydb_string_t = length+pointer string

GETSDIQ:     void              GETS^DIQ(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
FIND1DIC:    ydb_char_t*       $$FIND1^DIC(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
GET1DIQ:     ydb_char_t*       $$GET1^DIQ(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
FILEDIE:     void              FILE^DIE(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
UPDATEDIE:   void              UPDATE^DIE(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
FINDDICT:    void              FIND^DIC(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
LISTDIC:     void              LIST^DIC(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
CHKDIE:      ydb_char_t*       CHK^DIE(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
FIELDID:     void              FIELD^DID(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
FILEID:      void              FILE^DID(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
ROOTDILFD:   ydb_char_t*       $$ROOT^DILFD(I:ydb_char_t*, I:ydb_char_t*, I:ydb_char_t*)
DTXLFDT:     ydb_char_t*       $$DT^XLFDT()
ENDIK:       void              EN^DIK(I:ydb_char_t*, I:ydb_char_t*)
```

The alias names (e.g., `GETSDIQ`, `FIND1DIC`) are the strings passed to `ydb_ci()`. The `$$` prefix in the entry point indicates an extrinsic function; YottaDB's call-in table uses this prefix to distinguish functions from procedures.

### Calling `GETS^DIQ` via `ydb_ci`

```c
char result_buf[32];
result_buf[0] = '\0';

// Arguments in declaration order (not reversed as with IRIS):
// GETS^DIQ(file, iens, fields, flags, msg_node, result_node)
int status = ydb_ci(
    "GETSDIQ",
    "2",        // file number
    "100,",     // IENS
    ".01;.03",  // fields
    "EIN",      // flags
    "",         // msg_node (empty)
    "^||FMQRY"  // result_node
);

if (status != YDB_OK) {
    // Retrieve error message
    ydb_buffer_t msg = {256, 0, malloc(256)};
    ydb_message(status, &msg);
    // Handle error...
}
```

Unlike the IRIS C binding, arguments are passed **in declaration order** (not reversed). This is a critical difference: the IRIS binding uses a push-invoke model (arguments pushed last-to-first); YottaDB `ydb_ci` uses a variadic C call with arguments in forward order.

### Calling `$$FIND1^DIC` via `ydb_ci`

```c
char ien_result[32] = {0};

// $$FIND1^DIC(file, screen, index, value, flags)
// Return value is written to ien_result (ydb_char_t* return type)
int status = ydb_ci(
    "FIND1DIC",
    ien_result,   // output: receives the returned IEN string
    "2",          // file
    "",           // screen (empty)
    "B",          // index
    "SMITH,JOHN", // lookup value
    ""            // flags
);
// ien_result now contains the IEN string ("100") or "0" if not found
```

### Reading the Result Array After `GETS^DIQ`

After calling `GETSDIQ`, results are in `^||FMQRY`. Traverse with `ydb_subscript_next_s` and `ydb_get_s`:

```c
// Walk ^||FMQRY(file, iens, field) subscripts:
ydb_buffer_t gbl = {8, 8, "^||FMQRY"};

// Build subscript array: ["2", "100,", ""]  (empty = start before first)
char sub0[8] = "2", sub1[8] = "100,", sub2[64] = "";
ydb_buffer_t subs[3] = {
    {8, 1, sub0},
    {8, 4, sub1},
    {64, 0, sub2}   // current field subscript: start with ""
};

// Iterate fields:
char next_field[64];
ydb_buffer_t next = {64, 0, next_field};

while (1) {
    int rc = ydb_subscript_next_s(&gbl, 3, subs, &next);
    if (rc == YDB_ERR_NODEEND) break;      // no more subscripts
    if (rc != YDB_OK) { /* handle error */ break; }

    // Update current subscript for next iteration
    memcpy(subs[2].buf_addr, next.buf_addr, next.len_used);
    subs[2].len_used = next.len_used;

    // Get internal value at ^||FMQRY("2","100,",field)
    char val_buf[256];
    ydb_buffer_t value = {256, 0, val_buf};
    ydb_get_s(&gbl, 3, subs, &value);
    // val_buf[0..value.len_used] = internal value

    // Get external value at ^||FMQRY("2","100,",field,"E")
    char ext_sub[2] = "E";
    ydb_buffer_t subs4[4] = { subs[0], subs[1], subs[2], {2, 1, ext_sub} };
    char ext_buf[256];
    ydb_buffer_t ext_val = {256, 0, ext_buf};
    ydb_get_s(&gbl, 4, subs4, &ext_val);
    // ext_buf = external (display) value
}

// Clean up: KILL ^||FMQRY and all descendants
ydb_delete_s(&gbl, 0, NULL, YDB_DEL_TREE);
```

### Writing via `FILE^DIE`

Build the FDA global nodes with `ydb_set_s`, then call `FILE^DIE`:

```c
// Build ^||FMFDA(file, iens, field) = value
ydb_buffer_t fda_var = {8, 8, "^||FMFDA"};

// ^||FMFDA("2","+1,",".01") = "NEW PATIENT NAME"
ydb_buffer_t fda_subs[3] = {
    {2, 1, "2"},
    {4, 3, "+1,"},
    {4, 3, ".01"}
};
ydb_buffer_t name_val = {16, 16, "NEW PATIENT NAME"};
ydb_set_s(&fda_var, 3, fda_subs, &name_val);

// Call FILE^DIE("", "^||FMFDA", "^||FMERR")
int status = ydb_ci("FILEDIE", "", "^||FMFDA", "^||FMERR");

if (status != YDB_OK) { /* handle transport-level error */ }

// Check DIERR:
ydb_buffer_t err_var   = {8, 8, "^||FMERR"};
ydb_buffer_t dierr_sub = {5, 5, "DIERR"};
char count_buf[8];
ydb_buffer_t count = {8, 0, count_buf};

int rc = ydb_get_s(&err_var, 1, &dierr_sub, &count);
if (rc == YDB_OK && count.len_used > 0 && count.buf_addr[0] != '0') {
    // Read error text: ^||FMERR("DIERR",1,"TEXT",1)
    ydb_buffer_t err_subs[4] = {
        {5, 5, "DIERR"}, {1, 1, "1"}, {4, 4, "TEXT"}, {1, 1, "1"}
    };
    char msg_buf[512];
    ydb_buffer_t msg = {512, 0, msg_buf};
    ydb_get_s(&err_var, 4, err_subs, &msg);
    // msg.buf_addr contains the DIERR text
}

// New IEN is written back to ^||FMFDA("2","+1,") by FILE^DIE
char ien_buf[16];
ydb_buffer_t ien = {16, 0, ien_buf};
ydb_get_s(&fda_var, 2, (ydb_buffer_t[]){ {2,1,"2"}, {4,3,"+1,"} }, &ien);
// ien.buf_addr contains the newly assigned IEN

// Clean up
ydb_delete_s(&fda_var, 0, NULL, YDB_DEL_TREE);
ydb_delete_s(&err_var, 0, NULL, YDB_DEL_TREE);
```

---

## 4. Connection Mechanism 2: YottaDB Python Binding

For a Python-implemented gRPC Gateway, the `yottadb` PyPI package provides the most ergonomic path.

### Installation

```bash
pip install yottadb
```

The `yottadb` module uses `ctypes` to call `libyottadb.so` directly. It requires `ydb_dist`, `gtmroutines`, `gtmgbldir`, and `ydb_ci` to be set in the environment before `import yottadb`.

### Setting the FileMan Security Context

```python
import yottadb as ydb

# Set DUZ = "1"
ydb.set("DUZ", value="1")

# Set DUZ(0) = "@"  (programmer access)
ydb.set("DUZ", subsarray=("0",), value="@")

# Set DT = current FileMan date
dt_val = ydb.ci("DTXLFDT")   # calls $$DT^XLFDT() via call-in table
ydb.set("DT", value=dt_val)
```

YottaDB's Python binding treats both local variables and globals uniformly — `ydb.set("DUZ", ...)` sets a local variable in the M symbol table; `ydb.set("^DPT", subsarray=("100","0"), value="Smith")` sets a global node. Locals and globals are distinguished by the `^` prefix.

### Calling FileMan DBS Routines

```python
import yottadb as ydb

# GETS^DIQ — procedure call (no return value)
# Call-in table alias: GETSDIQ
ydb.ci(
    "GETSDIQ",
    "2",        # file number
    "100,",     # IENS
    ".01;.03",  # fields
    "EIN",      # flags
    "",         # msg_node
    "^||FMQRY"  # result_node
)

# Read back result using ydb.get
internal_value = ydb.get("^||FMQRY", subsarray=("2", "100,", ".01"))
external_value = ydb.get("^||FMQRY", subsarray=("2", "100,", ".01", "E"))

# Iterate all fields returned for the entry:
sub = ""
while True:
    try:
        sub = ydb.subscript_next("^||FMQRY", subsarray=("2", "100,", sub))
    except ydb.YDBNodeEnd:
        break
    val = ydb.get("^||FMQRY", subsarray=("2", "100,", sub))
    try:
        ext = ydb.get("^||FMQRY", subsarray=("2", "100,", sub, "E"))
    except ydb.YDBError:
        ext = None
    # process val, ext...

# Clean up temporary global
ydb.delete_tree("^||FMQRY")
```

### Extrinsic Function Calls

```python
# $$FIND1^DIC — returns IEN as string via call-in table alias FIND1DIC
ien = ydb.ci("FIND1DIC", "2", "", "B", "SMITH,JOHN", "")
# ien is "100" if found, "0" if not found

# $$GET1^DIQ — single field value
value = ydb.ci("GET1DIQ", "2", "100,", ".01", "E", "", "")
```

### Writing via `FILE^DIE`

```python
import yottadb as ydb

# Build the FDA global
ydb.set("^||FMFDA", subsarray=("2", "+1,", ".01"), value="NEW PATIENT NAME")
ydb.set("^||FMFDA", subsarray=("2", "+1,", ".03"), value="3260409")  # FileMan date

# Call FILE^DIE
ydb.ci("FILEDIE", "", "^||FMFDA", "^||FMERR")

# Check for DIERR errors
try:
    count = ydb.get("^||FMERR", subsarray=("DIERR",))
    if count and int(count) > 0:
        msg = ydb.get("^||FMERR", subsarray=("DIERR", "1", "TEXT", "1"))
        raise FileManError(msg)
except ydb.YDBError:
    pass  # DIERR node not set = no errors

# Read back new IEN (written back into FDA node by FILE^DIE)
new_ien = ydb.get("^||FMFDA", subsarray=("2", "+1,"))

# Clean up
ydb.delete_tree("^||FMFDA")
ydb.delete_tree("^||FMERR")
```

### Word-Processing Field Handling

```python
# Stage WP content as a local global
ydb.set("^||FMWP", subsarray=("1", "0"), value="First line of the note.")
ydb.set("^||FMWP", subsarray=("2", "0"), value="Second line of the note.")

# Set the FDA node to the WP global root
ydb.set("^||FMFDA", subsarray=("8925", "42,", "1901"), value="^||FMWP")

ydb.ci("UPDATEDIE", "", "^||FMFDA", "^||FMERR")
# ... check errors, clean up
```

---

## 5. Connection Mechanism 3: YottaDB Go Binding

For a Go-implemented gRPC Gateway, the YottaDB Go binding provides idiomatic Go types.

### Installation

```bash
go get lang.yottadb.com/go/yottadb
```

The Go binding wraps `libyottadb.so` using `cgo`. It requires the same environment variables as the C binding.

### Setting the FileMan Security Context

```go
import "lang.yottadb.com/go/yottadb"

tptoken := yottadb.NOTTP
var errstr yottadb.BufferT

// Set DUZ = "1"
var duz yottadb.KeyT
duz.Varnm.SetValStr(tptoken, &errstr, "DUZ")
duz.Alloc(0)
duz.Valsym.SetValStr(tptoken, &errstr, "1")
_ = duz.SetST(tptoken, &errstr)

// Set DUZ(0) = "@"
var duzZero yottadb.KeyT
duzZero.Varnm.SetValStr(tptoken, &errstr, "DUZ")
duzZero.Subary.SetElemStr(tptoken, &errstr, 0, "0")
duzZero.Alloc(1)
duzZero.Valsym.SetValStr(tptoken, &errstr, "@")
_ = duzZero.SetST(tptoken, &errstr)
```

### Calling FileMan DBS Routines

```go
// GETS^DIQ via call-in
err := yottadb.CallMT(
    tptoken, &errstr, 0,   // tptoken, errstr, timeout
    "GETSDIQ",             // call-in alias
    "2",                   // file
    "100,",                // IENS
    ".01;.03",             // fields
    "EIN",                 // flags
    "",                    // msg_node
    "^||FMQRY",            // result_node
)
if err != nil { /* handle */ }

// Read result
var resultKey yottadb.KeyT
resultKey.Varnm.SetValStr(tptoken, &errstr, "^||FMQRY")
resultKey.Subary.SetElemStr(tptoken, &errstr, 0, "2")
resultKey.Subary.SetElemStr(tptoken, &errstr, 1, "100,")
resultKey.Subary.SetElemStr(tptoken, &errstr, 2, ".01")
resultKey.Alloc(3)
val, err := resultKey.ValST(tptoken, &errstr)
// val contains internal value for field .01

// Clean up
var cleanup yottadb.KeyT
cleanup.Varnm.SetValStr(tptoken, &errstr, "^||FMQRY")
cleanup.Alloc(0)
_ = cleanup.DeleteST(tptoken, &errstr, yottadb.YDB_DEL_TREE)
```

### Extrinsic Function Calls

```go
// $$FIND1^DIC
var ien string
err = yottadb.CallMT(tptoken, &errstr, 0, "FIND1DIC",
    &ien,         // output: receives IEN
    "2",          // file
    "",           // screen
    "B",          // index
    "SMITH,JOHN", // value
    "",           // flags
)
// ien = "100" if found, "0" if not found
```

---

## 6. Implementing the `YDBRuntime` for the gRPC Gateway

The gRPC Gateway's `MRuntime` interface must be implemented by a `YDBRuntime` struct. This table maps each interface operation to the YottaDB C binding function(s) that implement it.

| MRuntime Method | YottaDB C Binding | Notes |
|---|---|---|
| `Init(duz, duzZero)` | `ydb_init()` + `ydb_set_s("DUZ", ...)` + `ydb_set_s("DUZ", ["0"], ...)` + `ydb_set_s("DT", ...)` | Called once per thread; sets process-level symbol table |
| `CallProcedure(routine, args)` | `ydb_ci(alias, args...)` | For `GETS^DIQ`, `FILE^DIE`, `UPDATE^DIE`, `EN^DIK` — uses call-in table |
| `CallFunction(routine, args)` | `ydb_ci(alias, &result, args...)` | For `$$FIND1^DIC`, `$$GET1^DIQ`, `$$ROOT^DILFD` — return value as first arg |
| `GetGlobal(node, subscripts)` | `ydb_get_s(&varname, n, subs, &retval)` | Read a global or local node value |
| `SetGlobal(value, node, subscripts)` | `ydb_set_s(&varname, n, subs, &value)` | Write a global or local node value |
| `KillGlobal(node, subscripts)` | `ydb_delete_s(&varname, n, subs, YDB_DEL_TREE)` | Kill the node and all descendants |
| `NextSubscript(node, subscripts, current)` | `ydb_subscript_next_s(&varname, n, subs, &result)` | Returns `YDB_ERR_NODEEND` when iteration is complete |
| `Eval(expr)` | Not applicable — use `ydb_set_s` for symbol table setup | YottaDB has no equivalent of `IRISEvalA`; context is set via direct API calls |
| `Close()` | `ydb_exit()` | Releases the calling thread's YottaDB channel |

**Key difference from IRISRuntime:** YottaDB has no `Eval` equivalent that executes arbitrary M expressions in the call-in context. All context setup (`DUZ`, `DT`) must be done via `ydb_set_s`. If an M expression must be evaluated at runtime, define a thin M wrapper routine and call it via `ydb_ci`.

### Concurrency and Threading

Unlike IRIS, YottaDB imposes no per-connection license limit. The gRPC Gateway can create one YottaDB channel per goroutine/thread with no artificial pool ceiling. The practical upper bound is set by the system's file descriptor limits and the database journal I/O capacity:

```
// YottaDB: no license limit
// Practical pool size: number of CPU cores × 2-4
pool_size = min(runtime.NumCPU() * 4, max_concurrent_grpc_requests)
```

Each pooled `YDBRuntime` instance calls `ydb_init()` once at startup. `DT` must be refreshed at session start each day (FileMan uses `DT` in date validation):

```c
// Refresh DT at the start of each request or once per day:
char dt_buf[16] = {0};
ydb_ci("DTXLFDT", dt_buf);   // calls $$DT^XLFDT()
ydb_buffer_t dt_var = {2, 2, "DT"};
ydb_buffer_t dt_val = {16, (unsigned int)strlen(dt_buf), dt_buf};
ydb_set_s(&dt_var, 0, NULL, &dt_val);
```

### Transaction Support

YottaDB provides ACID transaction support via `ydb_tp_s()`. For FileMan writes that must be atomic across multiple `FILE^DIE` calls:

```c
int fileman_write_tp(uint64_t tptoken, ydb_buffer_t *errstr, void *tpfnparm) {
    // Call FILE^DIE for multiple entries within this transaction
    ydb_ci("FILEDIE", "", "^||FMFDA1", "^||FMERR");
    ydb_ci("FILEDIE", "", "^||FMFDA2", "^||FMERR");
    return YDB_OK;  // commit; return YDB_TP_ROLLBACK to abort
}

// Invoke the transaction:
ydb_tp_s(fileman_write_tp, NULL, "BATCH", 0, NULL);
```

**Note:** FileMan cross-reference triggers execute inside the M runtime during `FILE^DIE`. If a trigger fires a notification or kills a cross-reference node, those changes are also enclosed in the YottaDB transaction and will roll back on abort.

---

## 7. Error Handling on YottaDB

### YottaDB Return Codes

All `ydb_*` C binding functions return an integer status code:

| Return Code | Meaning |
|---|---|
| `YDB_OK` (0) | Success |
| `YDB_ERR_NODEEND` | `$ORDER` or `$QUERY` reached end of subscript range — signals loop termination, not an error |
| `YDB_ERR_GVUNDEF` | Global node does not exist (`$DATA` would return 0) |
| `YDB_ERR_UNDEF` | Local variable is undefined |
| `YDB_ERR_CALLINAFTERXIT` | `ydb_ci` called after `ydb_exit()` — programming error |
| negative integer | Other M or YottaDB error — call `ydb_message()` to retrieve the text |

When a non-`YDB_OK`, non-`YDB_ERR_NODEEND` code is returned:

```c
ydb_buffer_t msg_buf = {512, 0, malloc(512)};
ydb_message(status, &msg_buf);
// msg_buf.buf_addr contains the error message string
// e.g., "%YDB-E-UNDEF, Undefined local variable: DUZ"
```

### FileMan DIERR on YottaDB

FileMan errors returned by `FILE^DIE` or `UPDATE^DIE` are placed in the error node global (e.g., `^||FMERR`). The DIERR structure is set by FileMan M code and is identical across YottaDB and IRIS:

```
^||FMERR("DIERR")           = count of errors
^||FMERR("DIERR",1,"TEXT",1) = first error message text
^||FMERR("DIERR",1,"CODE")   = FileMan error code
```

Read with `ydb_get_s`:

```c
ydb_buffer_t err_var = {8, 8, "^||FMERR"};
ydb_buffer_t dierr   = {5, 5, "DIERR"};
char count_buf[8] = {0};
ydb_buffer_t count = {8, 0, count_buf};

int rc = ydb_get_s(&err_var, 1, &dierr, &count);
if (rc == YDB_OK && count.len_used > 0 && count.buf_addr[0] != '0') {
    ydb_buffer_t err_path[4] = {
        {5,5,"DIERR"}, {1,1,"1"}, {4,4,"TEXT"}, {1,1,"1"}
    };
    char msg_buf[512] = {0};
    ydb_buffer_t msg = {512, 0, msg_buf};
    ydb_get_s(&err_var, 4, err_path, &msg);
    // msg_buf = human-readable FileMan validation message
}
```

### M Errors vs. FileMan Errors

- **YottaDB M runtime errors** — non-`YDB_OK` return from `ydb_ci` or `ydb_get_s`. Examples: `YDB_ERR_UNDEF` (DUZ not set), `YDB_ERR_ROUTINEUNKNOWN` (FileMan routine not found). These are configuration or programming errors. Map to `TransportError`.
- **FileMan validation errors** — `ydb_ci` returns `YDB_OK` but `DIERR` is set. These indicate failed INPUT transform validation, KEY uniqueness violation, or insufficient access codes. Map to `ValidationError`, `AccessDeniedError`, etc.
- **`YDB_ERR_NODEEND`** — not an error; signals end-of-subscripts during iteration. Never propagate to the gRPC layer.

---

## 8. Testing on YottaDB

### Verifying the Call-In Connection

```python
import yottadb as ydb
import os

# Confirm environment
assert os.environ.get("ydb_dist"), "ydb_dist not set"
assert os.environ.get("gtmgbldir"), "gtmgbldir not set"
assert os.environ.get("ydb_ci"), "ydb_ci not set"

# Confirm Kernel is accessible and returns a valid FM date
dt = ydb.ci("DTXLFDT")
assert len(dt) == 7 and dt.isdigit(), f"Expected 7-digit FM date, got: {dt}"
```

### Verifying FileMan Availability

```python
# Confirm FIND1^DIC is accessible by looking up file 1 for "FILE"
ien = ydb.ci("FIND1DIC", "1", "", "B", "FILE", "")
assert ien == "1", f"Expected IEN 1 for FILE file, got: {ien}"
```

### End-to-End Read Test

```python
# Retrieve the name of the PATIENT file (IEN 2 in FILE file #1)
ydb.ci("GETSDIQ", "1", "2,", ".01", "E", "", "^||FMTEST")
name = ydb.get("^||FMTEST", subsarray=("1", "2,", ".01", "E"))
assert name == "PATIENT", f"Expected 'PATIENT', got: {name}"
ydb.delete_tree("^||FMTEST")
```

### End-to-End Write Test (Against a Test File)

```python
# This test requires a dedicated test FileMan file in the 99000-99999 range.
# The file must be defined in the global directory and have FileMan DD entries.

ydb.set("^||FMTEST_FDA", subsarray=("99001", "+1,", ".01"), value="TEST RECORD YDB")
ydb.ci("FILEDIE", "", "^||FMTEST_FDA", "^||FMTEST_ERR")

try:
    count = ydb.get("^||FMTEST_ERR", subsarray=("DIERR",))
    assert not (count and int(count) > 0), "FILE^DIE returned DIERR errors"
except ydb.YDBError:
    pass  # no DIERR node = success

new_ien = ydb.get("^||FMTEST_FDA", subsarray=("99001", "+1,"))
assert new_ien and int(new_ien) > 0, f"Expected new IEN, got: {new_ien}"

ydb.delete_tree("^||FMTEST_FDA")
ydb.delete_tree("^||FMTEST_ERR")
```

---

## 9. Deployment Checklist

| Step | Action | Verify |
|---|---|---|
| 1 | YottaDB installed | `$ydb_dist/ydb --version` shows r1.34+ |
| 2 | FileMan routines installed | `$ydb_dist/ydb -run %XCMD 'WRITE $$DT^XLFDT(),!'` returns 7-digit date |
| 3 | `ydb_dist` env var set | Points to YottaDB installation directory |
| 4 | `gtmgbldir` env var set | Points to valid `.gld` global directory file |
| 5 | `gtmroutines` env var set | Includes path to FileMan routine objects (`DI*.o`) |
| 6 | `ydb_ci` env var set | Points to `fileman_callin.ci` call-in table |
| 7 | `LD_LIBRARY_PATH` includes `$ydb_dist` | `ldconfig -p \| grep libyottadb` finds the library |
| 8 | Service account `DUZ` provisioned | NEW PERSON file (#200) has the service account entry |
| 9 | Global root verified | `ydb_ci("ROOTDILFD", "2", "", "")` returns `^DPT(` |
| 10 | DIERR handling tested | Write test with invalid data produces `ValidationError`, not uncaught exception |

---

*This guide is part of the VA FileMan External API Wrapper documentation series. All FileMan API entry points and calling conventions are sourced from the VA FileMan 22.2 documentation set at `~/data/vista-docs/publish/infrastructure/di--fileman/`.*
