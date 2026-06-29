---
layout: page
title: Module - Systems | Class - JEContainer
sidebar: sidebar
permalink: /JEContainer.html
---

# 📦 JEContainer

> Technical reference for the `JEContainer` of JarEngine.

---

## 🔹 Overview

**`JEContainer` is a JarEngine class responsible for managing typed collections of engine objects with controlled insertion, retrieval, and lifecycle linkage inside the `systems` module.**

It provides:

* Type-restricted storage of engine objects
* Safe retrieval by multiple identifiers (name, id, instance, type)
* Automatic key collision handling
* Parent-child linkage for contained objects

---

## 🔹 Purpose

The purpose of `JEContainer` is to:

* Provide a strongly typed object storage system for engine entities
* Ensure only valid `JEInternBaseClass` objects are stored
* Offer flexible lookup mechanisms without exposing raw dictionaries
* Maintain deterministic object ownership inside the engine

It is **not** a generic Python container, but a **typed engine-managed object registry with enforced constraints**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── systems
│     ├── container.py
│     │     └── JEContainer
└── ...
```

`JEContainer` is part of the core systems layer and is used as a **generic object registry for engine-managed runtime elements**.

---

## 🔹 Class Relationships

### Uses

* [`JEInternBaseClass`](JEInternBaseClass.md)📎
* [`JEBool`](JEBool.md)📎
* [`JTKExternError`](JTKExternError.md)📎
* Python `dict`

---

## 🔹 Data Model

| Field             | Type           | Description                                |
|-------------------|----------------|--------------------------------------------|
| `_data`           | `dict[str, T]` | Internal storage mapping keys to objects   |
| `_allowed_type`   | `type[T]`      | Allowed base class type for stored objects |
| `_allow_subclass` | `JEBool`       | Defines whether subclasses are accepted    |

---

## 🔹 Public API

### Constructor

| Signature                                   | Description                                          |
|---------------------------------------------|------------------------------------------------------|
| `JEContainer(allowed_type, allow_subclass)` | Creates a typed container restricted to a base class |

---

### Accessors

| Method          | Returns        | Description                                     |
|-----------------|----------------|-------------------------------------------------|
| `get(...)`      | `T`            | Retrieves object by name, id, instance, or type |
| `__getitem__()` | `T`            | Shortcut retrieval operator                     |
| `data`          | `dict[str, T]` | Direct access to internal storage               |

---

### Mutators

| Method          | Description                                                   |
|-----------------|---------------------------------------------------------------|
| `add(obj)`      | Adds an object to the container with automatic key resolution |
| `__setitem__()` | Alias for `add()`                                             |
| `rm(...)`       | Removes an object by multiple lookup strategies               |

---

### Core Methods

| Method       | Description                                       |
|--------------|---------------------------------------------------|
| `add()`      | Inserts object with collision-safe key generation |
| `get()`      | Multi-strategy lookup system                      |
| `rm()`       | Multi-strategy removal system                     |
| `__iter__()` | Iterates over stored objects                      |

---

### Utility Methods

| Method     | Description                     |
|------------|---------------------------------|
| `data`     | Exposes raw internal dictionary |
| `__iter__` | Iteration over stored values    |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Type Binding (allowed_type)
   │
   ▼
Runtime Insertion (add)
   │
   ▼
Lookup / Iteration / Removal
   │
   ▼
Destruction (container discarded)
```

---

## 🔹 Internal Behavior

`JEContainer` enforces strict type safety and controlled object ownership:

* Only objects inheriting from `JEInternBaseClass` can be stored
* Optional subclass allowance controlled via `JEBool`
* Objects are indexed using their `jeid`
* Key collisions are resolved using incremental suffixing `(1), (2), ...`
* Objects can register a parent relationship via `add_parent()`

Lookup system supports multiple strategies:

* by `name`
* by `jeid`
* by instance equality
* by type filtering

---

## 🔹 Execution Flow

```text id="a9p3dk"
add(obj)
   │
   ▼
Type validation
   │
   ▼
Generate base key (jeid)
   │
   ▼
Resolve collisions
   │
   ▼
Attach parent (if supported)
   │
   ▼
Store in _data
```

---

## 🔹 Usage

### Basic Example

```python id="v9q2lp"
container = JEContainer(MyClass, JEBool(True))

obj = MyClass()
container.add(obj)

print(container[obj.name])
```

---

### Realistic Example

```python id="x3m8kp"
for entity in game.entities:
    print(entity.name)

target = game.entities.get(name="Player")
game.entities.rm(instance=target)
```

---

## 🔹 Design Decisions

* Strong type enforcement ensures engine consistency
* Centralized object ownership prevents scattered references
* Multiple lookup strategies improve flexibility without exposing internals
* Collision-safe key generation avoids overwriting objects
* Optional subclass control allows strict or flexible container behavior

---

## 🔹 Performance Notes

* Lookup by key: O(1)
* Lookup by name/type: O(n)
* Insertion: O(1) amortized
* Collision resolution: O(k) in worst case
* Iteration: O(n)

Optimized for:

* moderate entity counts
* ECS-style iteration patterns
* runtime object management

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Internal dictionary is mutable
- Not designed for concurrent writes
- Intended for single-threaded game loop usage
```

---

## 🔹 Limitations

* Linear lookup for name/type queries
* No indexing optimization (hash maps only)
* No persistence or serialization layer
* Depends on `jeid` uniqueness correctness
* Not safe for multithreaded access

---

## 🔹 Edge Cases

* Duplicate `jeid` values generate suffixed keys
* Missing lookup fields raise `JEErrorKey`
* Removing non-existent objects raises exception
* Subclass restriction enforced at insertion time

---

## 🔹 Current State

⚠️ Fully functional typed container system for engine object management.

### Implemented

* Typed object storage system
* Multi-strategy lookup (`name`, `jeid`, instance, type)
* Safe removal system
* Parent linking support
* Collision-safe key generation

### Planned

* Indexed lookup optimization for large datasets
* Weak reference support
* Event hooks on add/remove
* ECS-optimized container specialization

---

## 🔹 Debugging

* Use `dump()` from `JEInternBaseClass`
* Inspect `.data` directly for raw state
* Validate object presence via iteration
* Check key collisions using internal `_data` keys

---

## 🔹 Related Classes

* [`JEInternBaseClass`](JEInternBaseClass.py)📎
* [`JEBool`](JEBool.py)📎
* [`JEEntity`](JEEntity.py)📎

---

## 🔹 Notes

`JEContainer` is a core structural component of JarEngine’s runtime model.

It acts as a **controlled object registry layer**, ensuring both flexibility in access patterns and strictness in type safety.
