---
layout: page
title: Module - Systems | Class - JEImmutable
sidebar: sidebar
permalink: /JEImmutable.html
---

# 📦 JEImmutable

> Technical reference for the `JEImmutable` of JarEngine.

---

## 🔹 Overview

**`JEImmutable` is a JarEngine class responsible for providing a deep-frozen immutable wrapper over arbitrary Python data structures inside the `systems` module.**

It provides:

* Deep freezing of complex structures
* Safe immutable storage layer
* Controlled reconstruction of original data
* Functional-style data operations over immutable state

---

## 🔹 Purpose

The purpose of `JEImmutable` is to:

* Enforce immutability on runtime data
* Prevent unintended mutation of engine-critical values
* Provide a safe snapshot-like data container
* Offer functional utilities over frozen data

It is **not** a persistent identity-preserving container, but a **safe immutable data snapshot system**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── systems
│     ├── immutable.py
│     │     └── JEImmutable
└── ...
```

`JEImmutable` belongs to the low-level systems layer and is used as a **data safety abstraction** across engine components.

---

## 🔹 Class Relationships

### Uses

* `_freeze`
* `_unfreeze`
* [`JEInternBaseClass`](JEInternBaseClass.md)📎
* Python `deepcopy`

---

## 🔹 Data Model

| Field            | Type      | Description                          |
|------------------|-----------|--------------------------------------|
| `_frozen`        | `Any`     | Fully frozen internal representation |
| `_original_type` | `type[T]` | Original type of input value         |

---

## 🔹 Public API

### Constructor

| Signature            | Description                                      |
|----------------------|--------------------------------------------------|
| `JEImmutable(value)` | Creates an immutable snapshot of the given value |

---

### Accessors

| Method / Property | Returns   | Description                                      |
|-------------------|-----------|--------------------------------------------------|
| `data`            | `T`       | Reconstructed mutable copy (not identity-stable) |
| `frozen`          | `Any`     | Raw frozen internal representation               |
| `type`            | `type[T]` | Original type of stored value                    |

---

### Mutators

None — `JEImmutable` is fully immutable by design.

---

### Core Methods

| Method     | Description                       |
|------------|-----------------------------------|
| `map()`    | Applies function to each element  |
| `filter()` | Filters elements using predicate  |
| `any()`    | Checks if any element is truthy   |
| `all()`    | Checks if all elements are truthy |
| `count()`  | Counts occurrences                |
| `index()`  | Finds index of value              |

---

### Conversion Methods

| Method      | Description                           |
|-------------|---------------------------------------|
| `to_list()` | Converts data to list                 |
| `to_dict()` | Converts data to dict (if applicable) |
| `keys()`    | Returns mapping keys                  |
| `values()`  | Returns mapping values                |
| `items()`   | Returns mapping items                 |
| `get()`     | Safe key access                       |

---

### Utility Methods

| Method     | Description                   |
|------------|-------------------------------|
| `clone()`  | Creates a new immutable copy  |
| `__str__`  | Human-readable representation |
| `__repr__` | Debug representation          |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Deep Freeze (_freeze)
   │
   ▼
Immutable Storage (_frozen)
   │
   ▼
On-demand Reconstruction (data)
   │
   ▼
Optional cloning (clone)
```

---

## 🔹 Internal Behavior

`JEImmutable` works by converting input data into a **fully frozen recursive structure**:

* Primitive types are kept as-is
* Lists → tuples
* Sets → frozensets
* Dicts → frozenset of key/value pairs
* Complex objects → deep-copied fallback

Accessing `.data` triggers **reconstruction**, meaning:

* A new mutable copy is created each time
* Identity is not preserved
* Changes do not affect internal state

This design ensures:

* strict immutability guarantee
* safe sharing across systems
* predictable state snapshots

---

## 🔹 Execution Flow

```text
JEImmutable(value)
   │
   ▼
Type capture
   │
   ▼
Recursive freeze (_freeze)
   │
   ▼
Store frozen representation
   │
   ▼
Runtime usage via:
   ├── data (rebuild)
   ├── frozen (direct access)
   └── utilities (map/filter/etc.)
```

---

## 🔹 Usage

### Basic Example

```python
data = JEImmutable([1, 2, 3])

print(data.data)   # [1, 2, 3]
print(data.frozen) # immutable internal form
```

---

### Realistic Example

```python
snapshot = JEImmutable({
    "x": 10,
    "y": 20,
    "hp": 100
})

if snapshot.get("hp") > 0:
    print("Entity alive")
```

---

## 🔹 Design Decisions

* Immutability enforced through deep structural freezing
* Reconstruction model avoids direct mutation risk
* Separation between internal frozen state and external data view
* Functional-style utilities (map/filter/any/all)
* Supports heterogeneous data structures (list, dict, set, primitives)

---

## 🔹 Performance Notes

* `_freeze` is O(n) recursive traversal
* `.data` reconstruction creates a new object each call
* Optimal for snapshot systems, not hot-path loops
* Best used in:

  * history tracking
  * rollback systems
  * debugging tools
  * state saving

---

## 🔹 Thread Safety

```text
Thread-safe: Yes (read-only after construction)

Notes:
- Internal state is immutable
- Reconstruction produces new objects
- Safe for concurrent reads
```

---

## 🔹 Limitations

* `.data` is not identity stable (new object each call)
* Expensive for large nested structures
* Not optimized for real-time ECS loops
* Some methods assume sequence-like or mapping-like data

---

## 🔹 Edge Cases

* Non-iterable objects fallback to `deepcopy`
* Mixed structures may lose type fidelity
* `keys()/values()/items()` raise errors if not mapping
* `.index()` requires sequence-compatible data

---

## 🔹 Current State

⚠️ Fully functional immutable snapshot system.

### Implemented

* Deep freeze system
* Recursive structure handling
* Functional utilities (map/filter/any/all)
* Mapping helpers (dict-like support)
* Clone mechanism

### Planned

* Zero-copy immutable views
* Optional persistent structural sharing
* Integration with ECS history system
* Memory-optimized frozen graph representation

---

## 🔹 Debugging

* Use `dump()` from `JEInternBaseClass`
* Inspect `.frozen` for raw internal state
* Compare `.data` outputs for changes
* Validate type consistency via `.type`

---

## 🔹 Related Classes

* [`JEInternBaseClass`](JEInternBaseClass.md)📎
* [`JEBool`](JEBool.md)📎
* [`JEEntity`](JEEntity.md)📎
* [`JEGame`](JEGame.md)📎

---

## 🔹 Notes

`JEImmutable` is designed as a **state safety boundary system** for JarEngine.

It is particularly useful for:

* rollback systems
* replay systems
* debugging snapshots
* deterministic simulation states
