# VA FileMan API Wrapper — InterSystems IRIS Implementation Guide

**Building the FileMan gRPC Gateway on InterSystems IRIS**

*Version 1.0 — April 2026*
*Audience: Implementation engineers deploying the FileMan API wrapper on a VistA system running InterSystems IRIS*

*Part of the VA FileMan External API Wrapper series. See the [Comprehensive Specification](fileman-api-wrapper-specification.md) for architecture, API surface, wire protocol, and security design.*

---

## Overview

This guide covers the complete, practical implementation of the FileMan API wrapper gRPC Gateway on a VistA system running InterSystems IRIS. It assumes:

- IRIS is already installed and running with a working VistA instance
- FileMan 22.2 routines (`DI*` namespace) are installed and operational
- The reader is familiar with the two-layer gRPC architecture described in the [Comprehensive Specification](fileman-api-wrapper-specification.md) §6 and §19

For the YottaDB implementation, see [fileman-api-grpc-wrapper-yottadb.md](fileman-api-grpc-wrapper-yottadb.md).

The VA FileMan Technical Manual documents that the KIDS build distribution for FileMan 22.2 assumes installation on a Caché system (`technical-manual.md`, line 4167), and Caché is IRIS's predecessor — every production VA VistA deployment runs on IRIS or Caché. This guide therefore reflects the primary production target.

---

## Table of Contents

1. [IRIS Architecture Fundamentals](#1-iris-architecture-fundamentals)
2. [Prerequisites and Environment Setup](#2-prerequisites-and-environment-setup)
3. [Connection Mechanism 1: IRIS C Binding](#3-connection-mechanism-1-iris-c-binding-recommended-for-grpc-gateway)
4. [Connection Mechanism 2: IRIS Python Binding](#4-connection-mechanism-2-iris-python-binding)
5. [Connection Mechanism 3: IRIS TCP SuperServer](#5-connection-mechanism-3-iris-tcp-superserver)
6. [Implementing the IRISRuntime for the gRPC Gateway](#6-implementing-the-irisruntime-for-the-grpc-gateway)
7. [Error Handling on IRIS](#7-error-handling-on-iris)
8. [Testing on IRIS](#8-testing-on-iris)
9. [Deployment Checklist](#9-deployment-checklist)

---

## 1. IRIS Architecture Fundamentals

Before implementing anything, it is essential to understand how IRIS organizes its M runtime relative to what YottaDB developers expect.

### Namespaces

IRIS organizes all globals and routines into **namespaces**. A namespace is a named scope with its own global database mappings. A typical VA VistA IRIS installation uses:

| Namespace | Purpose |
|---|---|
| `%SYS` | IRIS system internals — do not use for application globals |
| `VISTA` (or site-specific, e.g. `VEHU`) | The VistA application namespace — FileMan routines and most globals live here |
| `USER` | Default user login namespace — generally not used for VistA data |

Every call to FileMan DBS routines must execute in the VistA application namespace. The wrapper must set `$NAMESPACE` to the correct namespace immediately after session initialization and before any M routine call. Failing to do this is the single most common IRIS integration error — routines and globals in the wrong namespace are simply not found, producing opaque errors that look like missing routines.

### Globals and Global Mappings

IRIS supports **global mapping** — a global root like `^DPT(` can be mapped from the application namespace to a separate data namespace on a different database file. This is a standard VA deployment pattern: routines live in one database, data lives in another. The mapping is transparent to M code and to the wrapper — `^DPT(100,0)` resolves correctly regardless of which physical database it is mapped to. The wrapper does not need to handle this explicitly as long as it operates in the correct namespace.

### The IRIS Interprocess Communication Model

In IRIS, every connected process is an M job. The embedded call-in mechanism (`irisdb.h`) creates a process that is a fully participating M job — it has its own local symbol table, its own `$JOB` value, and its own lock table. This is identical to YottaDB call-in semantics. The IRIS TCP SuperServer creates a separate M job per connection, exactly as the RPC Broker does.

---

## 2. Prerequisites and Environment Setup

### IRIS Version

IRIS 2022.1 or later is recommended. The `irisdb.h` C binding and the `intersystems-irispython` Python package require IRIS 2019.1+. IRIS for Health (IRIS-specific builds with FHIR acceleration) is compatible with this wrapper — the FileMan DBS API is identical.

### Required IRIS Components

| Component | Package | Purpose |
|---|---|---|
| `irisdb.h` + `libirisdb.so` | IRIS development kit | C binding for embedded call-in |
| `intersystems-irispython` | PyPI | Python binding for embedded and TCP paths |
| `%SYSTEM.Process` | IRIS system class | Process management, namespace switching |
| `%Library.Routine` | IRIS system class | M routine invocation from ObjectScript |
| FileMan routines (`DI*`) | VistA KIDS build | The FileMan DBS entry points |

### Environment Variables

| Variable | Value | Purpose |
|---|---|---|
| `IRISDIR` | `/usr/irissys` (or site path) | IRIS installation root |
| `ISC_CPF_FILE` | path to `iris.cpf` | IRIS configuration parameter file |
| `LD_LIBRARY_PATH` | `$IRISDIR/bin` | Locates `libirisdb.so` |
| `PATH` | includes `$IRISDIR/bin` | Locates `iris` CLI |

Unlike YottaDB, IRIS does not use a global directory file (`.gld`). Global database bindings are defined in the `iris.cpf` configuration file and managed by the IRIS system manager. The wrapper process inherits these bindings automatically.

### Verify IRIS is Running

```
iris list          # list running IRIS instances
iris status IRIS   # check status of instance named IRIS
```

The IRIS instance must be running before the wrapper process starts. The C call-in mechanism does not start IRIS — it attaches to a running instance.

---

## 3. Connection Mechanism 1: IRIS C Binding (Recommended for gRPC Gateway)

This is the primary mechanism for the gRPC Gateway service. It provides sub-millisecond call latency, no network overhead, and full access to the M runtime.

### The `irisdb.h` Header

The IRIS C binding is declared in `$IRISDIR/dev/iris-callin/irisdb.h`. Link against `$IRISDIR/bin/libirisdb.so` (Linux) or `libirisdb.dll` (Windows). The key functions are:

**Session management:**

| Function | Signature | Purpose |
|---|---|---|
| `IRISStart` | `int IRISStart(unsigned int flags, int tout, char *prinp, char *prout)` | Initialize IRIS session; attach to running instance |
| `IRISSecureStart` | `int IRISSecureStart(IRIS_ASTRP username, IRIS_ASTRP password, IRIS_ASTRP exename, unsigned int flags, int tout, char *prinp, char *prout)` | Authenticated session start |
| `IRISEnd` | `int IRISEnd(int force)` | Terminate IRIS session |
| `IRISAbort` | `int IRISAbort(void)` | Abort current M operation |

**Namespace management:**

| Function | Signature | Purpose |
|---|---|---|
| `IRISEvalA` | `int IRISEvalA(IRIS_ASTRP result, char *expr)` | Evaluate M expression; use to switch namespace |

To switch to the VistA namespace after `IRISStart`:
```
IRISEvalA(&result, "SET $NAMESPACE=\"VISTA\"")
```
This must be called once per session, before any FileMan routine call.

**Global operations:**

| Function | Signature | Purpose |
|---|---|---|
| `IRISGlobalGet` | `int IRISGlobalGet(int narg, ...)` | Get a global node value |
| `IRISGlobalSet` | `int IRISGlobalSet(int narg, ...)` | Set a global node value |
| `IRISGlobalKill` | `int IRISGlobalKill(int narg, ...)` | Kill a global node (and descendants) |
| `IRISGlobalOrder` | `int IRISGlobalOrder(int narg, int dir, ...)` | Iterate subscripts (`$ORDER` equivalent) |
| `IRISGlobalData` | `int IRISGlobalData(int narg, ...)` | Check existence and descendant status |

**M routine calls:**

| Function | Signature | Purpose |
|---|---|---|
| `IRISPushStr` | `int IRISPushStr(int len, char *str)` | Push a string argument onto the M stack |
| `IRISPushInt` | `int IRISPushInt(int num)` | Push an integer argument |
| `IRISDoFun` | `int IRISDoFun(unsigned int flags, int narg)` | Invoke a DO (procedure) call |
| `IRISExStrCallA` | `int IRISExStrCallA(IRIS_ASTRP result, int narg, IRIS_ASTRP routine)` | Call `$$routine` extrinsic function |
| `IRISInvokeFunctionA` | `int IRISInvokeFunctionA(IRIS_ASTRP result, int narg, IRIS_ASTRP routine)` | Invoke a named M function |

### Calling a FileMan DBS Procedure (e.g., `GETS^DIQ`)

`GETS^DIQ` is a procedure call (DO), not an extrinsic function. The calling sequence is:

```
1. IRISPushStr(len, result_node)   // push arg: result array root
2. IRISPushStr(len, "")            // push arg: msg_node (empty = default)
3. IRISPushStr(len, flags)         // push arg: "EIN"
4. IRISPushStr(len, fields)        // push arg: ".01;.03;1"
5. IRISPushStr(len, iens)          // push arg: "100,"
6. IRISPushStr(len, file)          // push arg: "2"
7. IRISDoFun(IRIS_DO_TAG_ROUTINE, 6)  // DO GETS^DIQ with 6 args
```

Arguments are pushed in **reverse order** (last argument first). `IRISDoFun` takes the count of pushed arguments and the entry point descriptor.

### Calling a FileMan Extrinsic Function (e.g., `$$FIND1^DIC`)

```
1. IRISPushStr(len, "")            // flags (empty)
2. IRISPushStr(len, value)         // lookup value
3. IRISPushStr(len, "B")           // index
4. IRISPushStr(len, "")            // screen (empty)
5. IRISPushStr(len, file)          // file number
6. IRISExStrCallA(&result, 5, "FIND1^DIC")
// result.len and result.str contain the returned IEN string
```

### Reading the Result Array After `GETS^DIQ`

After calling `GETS^DIQ`, results are in a global named by the `result_node` parameter (e.g., `^||FMQRY`). Traverse with `IRISGlobalOrder`:

```
// Walk result_node(file, iens, field) subscripts:
// 1. Get first field subscript under result_node(file, iens)
IRISPushStr(len, "")           // starting subscript (empty = first)
IRISPushStr(len, iens)         // e.g. "100,"
IRISPushStr(len, file)         // e.g. "2"
IRISPushStr(len, result_node)  // global name
IRISGlobalOrder(4, 1, &nextField)  // direction 1 = forward

// 2. Get value at result_node(file, iens, fieldNum)
IRISPushStr(len, fieldNum)
IRISPushStr(len, iens)
IRISPushStr(len, file)
IRISPushStr(len, result_node)
IRISGlobalGet(4, &value)

// 3. Get external value at result_node(file, iens, fieldNum, "E")
IRISPushStr(len, "E")
IRISPushStr(len, fieldNum)
IRISPushStr(len, iens)
IRISPushStr(len, file)
IRISPushStr(len, result_node)
IRISGlobalGet(5, &extValue)

// 4. Repeat IRISGlobalOrder with nextField as the new starting point
//    until nextField is empty (end of subscripts)
```

### Setting the FileMan Security Context

Before any FileMan call, set `DUZ` and `DUZ(0)` in the M symbol table:

```
IRISEvalA(&result, "SET DUZ=1,DUZ(0)=\"@\",DT=$$DT^XLFDT()")
```

`DT` (today's date in FileMan format) is also required — FileMan uses it in date validation and in setting timestamps. `$$DT^XLFDT()` is the Kernel function that returns the current date in FileMan internal format. Set all three in a single `IRISEvalA` call on session initialization.

**Important:** `DUZ(0)="@"` is programmer access (unrestricted). For production application sessions, set `DUZ(0)` to the actual access codes of the service account's `NEW PERSON` entry in file 200.

### Cleaning Up Temporary Globals

After reading results from a DBS call, kill the temporary global to prevent global storage accumulation:

```
IRISGlobalKill(1, result_node)   // KILL ^||FMQRY and all descendants
```

---

## 4. Connection Mechanism 2: IRIS Python Binding

For a Python-implemented gRPC Gateway, the `intersystems-irispython` package provides the most ergonomic path.

### Installation

```bash
pip install intersystems-irispython
```

This installs the `iris` module. Unlike the C binding, this package supports both embedded (in-process, for co-located servers) and TCP (remote) modes, switchable by configuration.

### Embedded Mode Setup

```python
import iris

# Connect embedded (in-process, co-located with IRIS)
iris.IRIS()   # uses environment variables to locate IRIS instance
```

The `iris.IRIS()` constructor reads `IRISDIR` and the instance configuration to attach to the running IRIS process. No explicit `IRISStart()` call is required.

### Namespace and Security Context

```python
import iris

# Switch to VistA namespace
iris.system.Process.SetNamespace("VISTA")

# Set FileMan security context in M symbol table
iris.system.Process.SetMVar("DUZ", "1")
iris.system.Process.SetMVarSubscript("DUZ", "0", "@")   # programmer access
# Set DT (today's date in FileMan format)
dt_val = iris.system.Process.EvalM("$$DT^XLFDT()")
iris.system.Process.SetMVar("DT", dt_val)
```

### Calling FileMan DBS Routines

```python
import iris

# GETS^DIQ — returns field values into a global node
# Call as a procedure (DO):
iris.system.Process.RunM(
    "GETS^DIQ",
    "2",           # file number
    "100,",        # IENS
    ".01;.03",     # fields
    "EIN",         # flags
    "",            # msg node (empty)
    "^||FMQRY"    # result node
)

# Read back result using iris.gref (global reference)
result = iris.gref("^||FMQRY")

# Get field .01 internal value:
internal_value = result["2", "100,", ".01"]

# Get field .01 external value:
external_value = result["2", "100,", ".01", "E"]

# Iterate all fields returned:
subscript = ""
while True:
    subscript = result.order(["2", "100,", subscript])
    if subscript == "":
        break
    val = result["2", "100,", subscript]
    ext = result["2", "100,", subscript, "E"]
    # process val, ext...

# Clean up temporary global
result.kill()
```

### Extrinsic Function Calls

```python
# $$FIND1^DIC — returns IEN as string
ien = iris.system.Process.CallM("FIND1^DIC", "2", "", "B", "SMITH,JOHN", "")
# ien is a string: "100" if found, "0" if not found

# $$GET1^DIQ — single field value
value = iris.system.Process.CallM("GET1^DIQ", "2", "100,", ".01", "E", "", "")
```

### Writing via FILE^DIE

```python
import iris

# Build the FDA global
fda = iris.gref("^||FMFDA")
fda["2", "+1,", ".01"] = "NEW PATIENT NAME"
fda["2", "+1,", ".03"] = "3260409"   # April 9, 2026 in FileMan date format

# Call FILE^DIE
err_node = "^||FMERR"
iris.system.Process.RunM("FILE^DIE", "", "^||FMFDA", err_node)

# Check for errors
err = iris.gref(err_node)
dierr_count = err["DIERR"]
if dierr_count and int(dierr_count) > 0:
    msg = err["DIERR", "1", "TEXT", "1"]
    raise FileManError(msg)

# Read back new IEN (FILE^DIE places it in the FDA node)
new_ien = fda["2", "+1,"]   # populated by FileMan after successful file

# Clean up
fda.kill()
err.kill()
```

### Word-Processing Field Handling

WP fields require a two-step write: populate a staging global, then reference it in the FDA.

```python
# Stage WP content in a global
wp_data = iris.gref("^||FMWP")
wp_data["1", "0"] = "First line of the note."
wp_data["2", "0"] = "Second line of the note."

# Set the FDA node to the WP global root
fda = iris.gref("^||FMFDA")
fda["8925", "42,", "1901"] = "^||FMWP"  # field 1901 = TEXT in TIU DOCUMENT

iris.system.Process.RunM("UPDATE^DIE", "", "^||FMFDA", "^||FMERR")
# ... check errors, clean up
```

---

## 5. Connection Mechanism 3: IRIS TCP SuperServer

For deployments where the gRPC Gateway runs on a different host from IRIS, use the TCP SuperServer path. IRIS listens on port 1972 by default.

### Python TCP Connection

```python
import iris

# Connect via TCP to remote IRIS
iris.IRIS(hostname="vista-server.hospital.va.gov", port=1972,
          namespace="VISTA", username="_SYSTEM", password="SYS")
```

The `iris.IRIS()` TCP mode wraps the IRIS JDBC/ODBC wire protocol. All `iris.system.Process` and `iris.gref` calls work identically over TCP — the same code runs in both embedded and TCP mode.

**Latency note:** TCP mode adds one network round-trip per M call. A `GETS^DIQ` call that takes 0.1 ms in embedded mode may take 2–5 ms over LAN. For high-throughput applications, prefer the embedded mode (§4) or the C binding (§3). TCP mode is appropriate for development workstations, test environments, and low-throughput management tools.

### Authentication over TCP

The TCP SuperServer uses IRIS's own authentication, not Kernel access/verify codes. For production use, create a dedicated IRIS service account with a strong password. Set this account's privileges to access only the VistA namespace. Then, separately, set the FileMan `DUZ` in the M symbol table to the appropriate NEW PERSON IEN as described in §4.

---

## 6. Implementing the `IRISRuntime` for the gRPC Gateway

The gRPC Gateway's `MRuntime` interface has the following operations the `IRISRuntime` must implement. This table maps each interface operation to the IRIS C binding function(s) that implement it.

| MRuntime Method | IRIS C Binding | Notes |
|---|---|---|
| `Init(namespace, duz, duzZero)` | `IRISStart()` + `IRISEvalA("SET $NAMESPACE=...")` + `IRISEvalA("SET DUZ=...,DUZ(0)=...,DT=...")` | Called once per connection; establishes namespace and security context |
| `CallProcedure(routine, args)` | `IRISPushStr()` × n + `IRISDoFun()` | For procedure calls: `GETS^DIQ`, `FILE^DIE`, `UPDATE^DIE`, `EN^DIK` |
| `CallFunction(routine, args)` | `IRISPushStr()` × n + `IRISExStrCallA()` | For extrinsic functions: `$$FIND1^DIC`, `$$GET1^DIQ`, `$$CANDO^DIAC1` |
| `GetGlobal(node, subscripts)` | `IRISPushStr()` × n + `IRISGlobalGet()` | Read a global node value |
| `SetGlobal(value, node, subscripts)` | `IRISPushStr()` × n + `IRISGlobalSet()` | Write a global node value |
| `KillGlobal(node, subscripts)` | `IRISPushStr()` × n + `IRISGlobalKill()` | Kill a global tree |
| `NextSubscript(node, subscripts, current)` | `IRISPushStr()` × n + `IRISGlobalOrder(n, 1, &next)` | Forward subscript iteration (`$ORDER`) |
| `Eval(expr)` | `IRISEvalA(&result, expr)` | Evaluate arbitrary M expression; used sparingly for context setup |
| `Close()` | `IRISEnd(0)` | Release IRIS session |

### Connection Pool

Because each IRIS session consumes an IRIS license unit and has its own M process context (symbol table, lock table), the gRPC Gateway must maintain a pool of pre-initialized `IRISRuntime` instances. The pool size is bounded by:

```
pool_size = min(available_iris_license_units, max_concurrent_grpc_requests)
```

Typical VA IRIS deployments have 200–500 license units. Reserve headroom for CPRS sessions, VistALink, and other consumers. A safe initial pool size is 20–50 for a dedicated FileMan wrapper service.

Each pooled connection holds a permanent M process with `$NAMESPACE`, `DUZ`, and `DT` already set. When a gRPC request arrives, a connection is checked out, used for the duration of the request, and returned. `DT` must be refreshed at the start of each working day — the simplest approach is to call `IRISEvalA("SET DT=$$DT^XLFDT()")` at the start of each request.

---

## 7. Error Handling on IRIS

### IRIS Return Codes

All `IRISGlobalGet`, `IRISGlobalSet`, `IRISDoFun`, and `IRISExStrCallA` functions return an integer status code:

| Return Code | Meaning |
|---|---|
| `IRIS_OK` (0) | Success |
| `IRIS_CONBROKEN` | Connection to IRIS lost — must reinitialize |
| `IRIS_ERRUNIMPLEMENTED` | Function not available in this IRIS version |
| `IRIS_ERROR` | M error occurred — call `IRISGetError()` for details |

When `IRIS_ERROR` is returned, call `IRISGetError(len, &message)` to retrieve the IRIS error message. IRIS error messages follow the `%SYSTEM.Error` format: `<ERR>:<detail>`, e.g. `<UNDEFINED>DUZ+1^DICRW`. These must be translated into the wrapper's `FileManError` hierarchy before returning to the gRPC layer.

### FileMan DIERR on IRIS

FileMan errors land in the `DIERR` global node after `FILE^DIE` or `UPDATE^DIE`. The wrapper reads these with `IRISGlobalGet` exactly as on YottaDB:

```
// Check DIERR count in error node
IRISPushStr(len, "DIERR")
IRISPushStr(len, err_node)
IRISGlobalGet(2, &count)

if count > 0:
    // Read first error text:
    IRISPushStr(len, "1")
    IRISPushStr(len, "TEXT")
    IRISPushStr(len, "1")
    IRISPushStr(len, "DIERR")
    IRISPushStr(len, err_node)
    IRISGlobalGet(5, &msg)
    // map msg to typed FileManError subclass
```

The DIERR structure is identical to YottaDB — it is set by FileMan M code, which runs identically on both runtimes.

### M Errors vs. FileMan Errors

Distinguish carefully between two error types:

- **M runtime errors** (undefined variable, routine not found, etc.) — returned as `IRIS_ERROR` from the C binding. These indicate a configuration problem: wrong namespace, missing FileMan routine, or missing `DUZ`/`DT` context. They are programming errors, not user errors.
- **FileMan validation errors** — returned in the `DIERR` array after a DBS call completes without M-level error. These indicate that the filed data failed a FileMan INPUT transform, KEY uniqueness check, or access code check. They are expected application-layer errors.

The wrapper must handle both classes, translating M errors to `TransportError` and FileMan errors to the appropriate `ValidationError`, `AccessDeniedError`, etc.

---

## 8. Testing on IRIS

### Verifying the IRIS Connection

Before testing any FileMan operations, verify the basic call-in works:

```python
import iris
iris.IRIS()
iris.system.Process.SetNamespace("VISTA")
result = iris.system.Process.EvalM("$$DT^XLFDT()")
assert len(result) == 7, f"Expected 7-digit FM date, got: {result}"
```

This tests: namespace switch works, Kernel routines are accessible, and the date function returns a valid FileMan date.

### Verifying FileMan Availability

```python
# Check that FILE^DICN (the FileMan add-entry routine) is accessible
# by looking up file 1 (the FILE file) for the file named "FILE"
ien = iris.system.Process.CallM("FIND1^DIC", "1", "", "B", "FILE", "")
assert ien == "1", f"Expected IEN 1 for FILE file, got: {ien}"
```

### End-to-End Read Test

```python
# Retrieve the name of the PATIENT file from file #1 (FILE file)
iris.system.Process.RunM("GETS^DIQ", "1", "2,", ".01", "E", "", "^||FMTEST")
test = iris.gref("^||FMTEST")
name = test["1", "2,", ".01", "E"]
assert name == "PATIENT", f"Expected 'PATIENT', got: {name}"
test.kill()
```

### End-to-End Write Test (Against a Test File)

```python
# This test requires a dedicated test FileMan file in the 99000-99999 range
# to avoid touching production data. The file must be defined on the
# target IRIS instance.

fda = iris.gref("^||FMTEST_FDA")
fda["99001", "+1,", ".01"] = "TEST RECORD IRIS"
iris.system.Process.RunM("FILE^DIE", "", "^||FMTEST_FDA", "^||FMTEST_ERR")

err = iris.gref("^||FMTEST_ERR")
assert not err["DIERR"], "FILE^DIE returned DIERR errors"

new_ien = fda["99001", "+1,"]
assert new_ien and int(new_ien) > 0, f"Expected new IEN, got: {new_ien}"

fda.kill()
err.kill()
```

---

## 9. Deployment Checklist

| Step | Action | Verify |
|---|---|---|
| 1 | IRIS instance running | `iris status IRIS` returns RUNNING |
| 2 | FileMan routines installed | `$$DT^XLFDT()` returns 7-digit date in VISTA namespace |
| 3 | `IRISDIR` env var set | Points to IRIS installation root |
| 4 | `LD_LIBRARY_PATH` includes `$IRISDIR/bin` | `ldconfig -p \| grep libirisdb` finds the library |
| 5 | VistA namespace name confirmed | `iris.system.Process.SetNamespace()` succeeds without error |
| 6 | Service account `DUZ` provisioned | NEW PERSON file (#200) has the service account entry |
| 7 | IRIS license units available | `System > License > License Key` shows available units |
| 8 | Pool size configured | Set to ≤ available license units minus headroom for other IRIS consumers |
| 9 | Global mapping verified | `$$ROOT^DILFD("2","","")` returns `^DPT(` in VISTA namespace |
| 10 | DIERR handling tested | Write test with invalid data produces `ValidationError`, not uncaught exception |

---

*This guide is part of the VA FileMan External API Wrapper documentation series. All FileMan API entry points and calling conventions are sourced from the VA FileMan 22.2 documentation set at `~/data/vista-docs/publish/infrastructure/di--fileman/`.*
