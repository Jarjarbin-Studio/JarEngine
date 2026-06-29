---
layout: page
title: Module - Interns | Module - LowClasses | Class - JEInternGraphic
sidebar: sidebar
permalink: /JEInternGraphic.html
---

# 📦 JEInternGraphic

> Technical reference for the `JEInternGraphic` of JarEngine.

---

## 🔹 Overview

**`JEInternGraphic` is a JarEngine internal base class responsible for providing identity, lifecycle tracking, and destruction state management for graphical engine objects inside the `interns` module.**

It provides:

* Object identity management (name + hashes)
* Lifecycle state tracking (alive / destroyed)
* Base interface for engine graphical internals

---

## 🔹 Purpose

The purpose of `JEInternGraphic` is to:

* Provide a unified base for all engine graphical internal objects
* Track whether an object is alive or destroyed
* Store identity metadata used internally by the engine

It is **not** a rendering component, but a **low-level lifecycle and identity base class for graphical engine objects**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── interns
│     ├── low_classes
│     │     ├── JEInternGraphic
│     │     └── JEInternGraphicalObject
│     └── ...
└── ...
```

`JEInternGraphic` is a foundational internal class used by higher-level graphical resources such as textures, fonts, and renderable engine objects.

---

## 🔹 Class Relationships

### Uses

* [`JEBool`](JEBool.md)📎
* [`JEInternBaseClass`](JEInternBaseClass.md)📎

---

## 🔹 Data Model

| Field          | Type     | Description                            |
|----------------|----------|----------------------------------------|
| `name`         | `str`    | Object identifier name                 |
| `_name_hash`   | `int`    | Precomputed hash of object name        |
| `_object_hash` | `int`    | Unique hash of the instance            |
| `_destroyed`   | `JEBool` | Lifecycle state flag (alive/destroyed) |

---

## 🔹 Public API

### Constructor

| Signature        | Description                                                    |
|------------------|----------------------------------------------------------------|
| `__init__(name)` | Initializes a graphical internal object with a name identifier |

---

### Accessors

| Method / Property | Returns  | Description                                               |
|-------------------|----------|-----------------------------------------------------------|
| `is_alive`        | `JEBool` | Returns whether the object is still alive (not destroyed) |

---

### Mutators

| Method      | Description                   |
|-------------|-------------------------------|
| `destroy()` | Marks the object as destroyed |

---

### Core Methods

| Method       | Description                              |
|--------------|------------------------------------------|
| `destroy()`  | Sets internal destroyed flag             |
| `__init__()` | Initializes identity and lifecycle state |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Initialization (name + hashes computed)
   │
   ▼
Runtime Usage
   │
   ▼
Alive State Monitoring
   │
   ▼
Destroy Call
   │
   ▼
Destroyed State
```

An instance remains alive until explicitly marked as destroyed through `destroy()`.

---

## 🔹 Internal Behavior

`JEInternGraphic` focuses on identity and lifecycle tracking rather than functional behavior.

Key behaviors:

* The object stores a human-readable name and two hash values for fast internal comparisons
* `_destroyed` is stored as a `JEBool` instead of a native boolean for engine consistency
* `is_alive` is computed dynamically from `_destroyed`
* No automatic cleanup is performed; destruction is explicit

---

## 🔹 Execution Flow

```text
Constructor call
   │
   ▼
Store name
   │
   ▼
Compute hashes
   │
   ▼
Initialize destroyed flag (false)
   │
   ▼
Object becomes active in engine
```

For destruction:

```text
destroy()
   │
   ▼
Set destroyed flag to true
   │
   ▼
is_alive becomes false
```

---

## 🔹 Usage

### Basic Example

```python
obj = JEInternGraphic("texture_01")

print(obj.is_alive)

obj.destroy()

print(obj.is_alive)
```

---

### Realistic Example

```python
class MyResource(JEInternGraphic):
    def __init__(self, name):
        super().__init__(name)

resource = MyResource("font_main")

if resource.is_alive:
    resource.destroy()
```

---

## 🔹 Design Decisions

* Minimal base class to reduce overhead in engine internals
* Explicit lifecycle control instead of automatic garbage management
* Engine-specific boolean type (`JEBool`) for consistency across systems
* Precomputed hashes for fast identity comparisons in engine systems

---

## 🔹 Performance Notes

* O(1) operations for all methods and properties
* Hash computation done once at initialization
* No dynamic allocation during runtime checks
* Designed for high-frequency usage in ECS-like systems

---

## 🔹 Thread Safety

Thread-safe: No

Notes:

* Lifecycle state is mutable without synchronization
* Intended for single-threaded engine loop usage

---

## 🔹 Limitations

* No automatic destruction handling
* No event system for lifecycle changes
* No copy/clone behavior defined
* Relies on engine-controlled lifecycle discipline

---

## 🔹 Edge Cases

* Multiple calls to `destroy()` have no additional effect
* Object remains accessible after destruction unless handled externally
* Hash collision theoretically possible but not handled

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* Name-based identity
* Hash caching
* Lifecycle flag (`destroyed`)
* Alive state query

### Planned

* Event hooks on destroy
* Automatic resource cleanup integration
* Reference tracking system
* Debug lifecycle tracing tools

---

## 🔹 Debugging

* Check `name` and hashes for identity issues
* Use `is_alive` to verify lifecycle state
* Verify `destroy()` calls when objects persist unexpectedly
* Inspect engine systems that may still reference destroyed objects

---

## 🔹 Related Classes

* [`JEBool`](JEBool.md)📎
* [`JEInternGraphicalObject`](JEInternGraphicalObject.md)📎
* [`JEInternBaseClass`](JEInternBaseClass.md)📎

---

## 🔹 Notes

`JEInternGraphic` is a foundational internal abstraction used by nearly all graphical engine objects to ensure consistent lifecycle tracking and identity management.
