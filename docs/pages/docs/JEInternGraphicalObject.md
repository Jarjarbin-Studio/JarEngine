---
layout: page
title: Module - Interns | Module - LowClasses | Class - JEInternGraphicalObject
sidebar: sidebar
permalink: /JEInternGraphicalObject.html
---

# 📦 JEInternGraphicalObject

> Technical reference for the `JEInternGraphicalObject` of JarEngine.

---

## 🔹 Overview

**`JEInternGraphicalObject` is a JarEngine class responsible for managing a graphical object lifecycle with a dirty-state tracking system inside the `interns` module.**

It provides:

* Dirty flag management for update optimization
* Base graphical lifecycle through inheritance
* Update hook for derived graphical components

---

## 🔹 Purpose

The purpose of `JEInternGraphicalObject` is to:

* Provide a lightweight base class for graphical engine objects
* Track modification state to optimize rendering or update pipelines
* Offer an extensible update method for derived classes

It is **not** a rendering system or scene manager, but a **low-level graphical state container for engine internals**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── interns
│     ├── JEInternGraphic
│     ├── JEInternGraphicalObject
│     └── ...
└── ...
```

This class extends `JEInternGraphic` and is used as a base for graphical entities that require state tracking during engine execution.

---

## 🔹 Class Relationships

### Uses

* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEBool`](JEBool.md)📎

---

## 🔹 Data Model

| Field    | Type     | Description                          |
|----------|----------|--------------------------------------|
| `_dirty` | `JEBool` | Indicates if the object was modified |

In addition to inherited fields from `JEInternGraphic`, this class adds a modification tracking flag used for optimization purposes.

---

## 🔹 Public API

### Constructor

| Signature        | Description                                         |
|------------------|-----------------------------------------------------|
| `__init__(name)` | Creates a graphical object with dirty state enabled |

---

### Accessors

| Method     | Returns  | Description                         |
|------------|----------|-------------------------------------|
| `is_dirty` | `JEBool` | Returns whether object was modified |

---

### Mutators

| Method          | Description                  |
|-----------------|------------------------------|
| `mark_dirty()`  | Marks the object as modified |
| `clear_dirty()` | Resets the dirty flag        |

---

### Core Methods

| Method     | Description                             |
|------------|-----------------------------------------|
| `update()` | Update hook for derived implementations |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Initialization
   │
   ▼
Runtime Usage
   │
   ▼
Update Cycles
   │
   ▼
Dirty State Tracking
   │
   ▼
Destruction
```

During runtime, the object is repeatedly marked dirty when modified and reset once processed by higher-level systems.

---

## 🔹 Internal Behavior

This class extends `JEInternGraphic` and introduces a modification tracking mechanism:

* `_dirty` is initialized to `True` (represented by `JEBool(1)`)
* Any structural change should call `mark_dirty()`
* Once processed, `clear_dirty()` resets the state
* `update()` acts as a placeholder for derived behavior
* Designed for minimal overhead in engine loops

This design supports efficient update batching in rendering or ECS-like systems.

---

## 🔹 Execution Flow

```text
Method Call
   │
   ▼
Dirty flag update (optional)
   │
   ▼
State modification
   │
   ▼
Engine processing phase
   │
   ▼
Clear dirty flag (if needed)
   │
   ▼
Return
```

---

## 🔹 Usage

### Basic Example

```python
obj = JEInternGraphicalObject("Entity")

obj.mark_dirty()

if obj.is_dirty:
    obj.clear_dirty()
```

---

### Realistic Example

```python
def update_entity(entity, dt):
    entity.update(dt)

    if entity.is_dirty:
        render_queue.add(entity)
        entity.clear_dirty()
```

---

## 🔹 Design Decisions

* Dirty flag system reduces unnecessary updates in rendering pipelines
* Separation of lifecycle (`update`) and state tracking (`dirty`)
* Lightweight inheritance from `JEInternGraphic`
* Optimized for ECS-style or batch-processing architectures

---

## 🔹 Performance Notes

* Time complexity: O(1) for all operations
* Memory usage: O(1)
* Very low overhead due to boolean flag system
* Suitable for hot-path execution in engine loops

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Mutating dirty state is not synchronized
- Intended for single-threaded engine loop usage
```

---

## 🔹 Limitations

* No automatic dirty detection (manual marking required)
* No built-in update logic
* Depends on correct usage of lifecycle methods
* Inherits minimal functionality only

---

## 🔹 Edge Cases

* Forgetting to call `clear_dirty()` may cause redundant processing
* Calling `update()` does nothing by default
* Multiple systems modifying `_dirty` may cause inconsistent state

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* Dirty flag system
* Update hook method
* Basic graphical inheritance

### Planned

* Automatic dirty tracking
* Event-based state updates
* Integration with ECS pipeline

---

## 🔹 Debugging

* Use `dump()` to inspect `_dirty` state
* Use `debug()` to trace lifecycle behavior
* Monitor dirty flag during render/update cycles to detect redundant processing

---

## 🔹 Related Classes

* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEBool`](JEBool.md)📎

---

## 🔹 Notes

This class is a core building block for optimization strategies in JarEngine’s internal rendering and update pipeline.
