---
layout: page
title: Module - Systems | Class - JEBool
sidebar: sidebar
permalink: /JEBool.html
---

# 📦 JEBool

> Engine-safe boolean wrapper using a flyweight pattern over Python primitive boolean values.

---

## 🔹 Overview

**`JEBool` is a JarEngine class responsible for providing a controlled, engine-safe boolean type with enforced instance reuse inside the `systems` module.**

It provides:

* Immutable boolean representation
* Flyweight instance caching (`True` / `False`)
* Engine-level type abstraction over Python `bool`

---

## 🔹 Purpose

The purpose of `JEBool` is to:

* Standardize boolean handling inside JarEngine
* Prevent raw Python boolean usage in engine systems
* Reduce memory usage via flyweight pattern
* Guarantee strict identity-based boolean instances

It is **not** a general-purpose boolean replacement system, but a **controlled internal engine primitive abstraction**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── systems
│     ├── bool.py
│     │     └── JEBool
└── ...
```

`JEBool` is part of the low-level **systems layer**, acting as a primitive abstraction used across engine modules such as input, events, and constants.

---

## 🔹 Class Relationships

### Uses

* [`JEInternBaseClass`](JEInternBaseClass.md)📎
* Python built-in `bool`

---

## 🔹 Data Model

| Field                 | Type   | Description                        |
|-----------------------|--------|------------------------------------|
| `_bool`               | `bool` | Internal boolean value             |
| `_instances`          | `dict` | Flyweight instance cache           |
| `__instance_policy__` | `str`  | Defines flyweight behavior         |
| `__instance_limit__`  | `int`  | Limits instances to 2 (True/False) |

---

## 🔹 Public API

### Constructor

| Signature       | Description                                  |
|-----------------|----------------------------------------------|
| `JEBool(value)` | Creates or returns a cached boolean instance |

---

### Accessors

| Method / Property | Returns | Description               |
|-------------------|---------|---------------------------|
| `data`            | `bool`  | Returns raw boolean value |
| `__bool__()`      | `bool`  | Python truth evaluation   |

---

### Mutators

None — `JEBool` is immutable after creation.

---

### Core Methods

| Method       | Description                         |
|--------------|-------------------------------------|
| `__new__()`  | Implements flyweight instance reuse |
| `__init__()` | Initializes internal boolean value  |

---

### Utility Methods

| Method         | Description                       |
|----------------|-----------------------------------|
| `__deepcopy__` | Returns self (preserves identity) |

---

## 🔹 Lifecycle

```text
JEBool(value)
   │
   ▼
__new__ (flyweight check)
   │
   ▼
Instance reuse or creation
   │
   ▼
__init__ (only once per instance)
   │
   ▼
Runtime usage
   │
   ▼
No destruction (cached forever)
```

---

## 🔹 Internal Behavior

`JEBool` enforces a **strict flyweight pattern**:

* Only two instances exist globally:

  * one for `True`
  * one for `False`
* `__new__` checks `_instances` before allocating
* repeated constructions return existing objects
* `__init__` is guarded by `_initialized` to avoid reinitialization

This ensures:

* identity consistency (`is` comparisons possible)
* reduced memory overhead
* deterministic boolean behavior across the engine

---

## 🔹 Execution Flow

```text
JEBool(value)
   │
   ▼
Convert to Python bool
   │
   ▼
Check cache (_instances)
   │
   ├── Exists → return cached instance
   └── Not exists → create instance
   │
   ▼
Initialize (once)
   │
   ▼
Return engine boolean object
```

---

## 🔹 Usage

### Basic Example

```python
a = JEBool(1)
b = JEBool(0)

print(bool(a))  # True
print(bool(b))  # False
```

---

### Realistic Example

```python
is_running = JEBool(True)

if is_running:
    print("Engine is running")
```

---

### Integration with Engine Constants

```python
from JarEngine import JETrue, JEFalse

if JETrue:
    print("Enabled system")
```

---

## 🔹 Design Decisions

* Flyweight pattern ensures only two boolean instances exist
* Prevents duplication of primitive engine values
* Forces consistent type usage across engine systems
* Avoids Python primitive leakage in core architecture
* Deepcopy returns self to preserve identity integrity

---

## 🔹 Performance Notes

* O(1) lookup for instance retrieval
* Zero allocation after initial creation
* Constant-time boolean evaluation
* Memory footprint reduced to 2 global instances
* Ideal for high-frequency checks (input, update loops)

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Shared mutable class-level cache (_instances)
- Designed for single-threaded game loop usage
```

---

## 🔹 Limitations

* Only supports two states (True / False)
* Not extensible beyond binary logic
* Global cache may introduce shared-state constraints
* Not suitable for multi-threaded environments

---

## 🔹 Edge Cases

* Multiple `JEBool(True)` calls always return same instance
* `__init__` is bypassed on reused instances
* `deepcopy()` does not create new objects
* Boolean conversion always returns native Python `bool`

---

## 🔹 Current State

⚠️ Fully functional low-level engine primitive.

### Implemented

* Flyweight boolean system
* Identity-based instance reuse
* Engine-safe boolean abstraction
* Integration with constants system

### Planned

* Possible integration with typed logic system
* Extension into symbolic boolean expressions (optional future feature)

---

## 🔹 Debugging

* Use `dump()` from `JEInternBaseClass`
* Inspect `_instances` cache directly
* Validate identity with `is` operator
* Check boolean conversion via `bool(obj)`

---

## 🔹 Example Output

```text
True
False
Engine is running
```

---

## 🔹 Related Classes

* [`JEInternBaseClass`](JEInternBaseClass.md)📎
* [`JEEventCode`](JEEventCode.md)📎
* [`JEKeyCode`](JEKeyCode.md)📎

---

## 🔹 Notes

`JEBool` is a foundational primitive in JarEngine’s type system.
It ensures that even basic boolean logic is handled in a controlled, deterministic, and engine-consistent way rather than relying on raw Python primitives.
