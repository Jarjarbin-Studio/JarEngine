---
layout: page
title: Module - Interns | Class - JEInternBaseClass
sidebar: sidebar
permalink: /JEInternBaseClass.html
---

# 📦 JEInternClassBase

> Technical reference for the `JEInternClassBase` class of JarEngine.

---

## 🔹 Overview

**`JEInternClassBase` is a JarEngine core base class responsible for providing identity, debugging utilities, serialization, and recursive inspection capabilities for all JarEngine objects.**

It provides:

* Unique engine identifier generation
* String and representation formatting
* Dictionary serialization of public attributes
* Recursive debug tree visualization
* Structured dump inspection system

---

## 🔹 Purpose

The purpose of `JEInternClassBase` is to:

* Provide a unified base type for all internal engine objects
* Standardize debugging and introspection across the engine
* Enable hierarchical inspection of object graphs
* Offer safe serialization of public-facing state

It is **not** a feature-specific engine system, but a **universal internal abstraction base for all JarEngine classes**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── Interns
│     ├── base_classe.py
│     │     └── JEInternClassBase
│     ├── low_classes.py
│     ├── high_classes.py
│     ├── final_classes.py
│     └── config.py
└── ...
```

`JEInternClassBase` sits at the foundation of the internal class hierarchy and is inherited by most engine subsystems to ensure consistent identity and debugging behavior.

---

## 🔹 Class Relationships

### Uses

* `uuid.uuid4` 📎
* `sources.interns.JTKExternConsole` 📎
* `sources.interns.decorators.documentation` 📎
* `sources.systems.immutable.JEImmutable` 📎

---

## 🔹 Data Model

| Field                 | Type   | Description                                         |                                    |
|-----------------------|--------|-----------------------------------------------------|------------------------------------|
| `jeid`                | `str`  | Unique identifier generated at instantiation        |                                    |
| `__instance_policy__` | `str`  | Instance policy mode (normal, singleton, flyweight) |                                    |
| `__instance_limit__`  | `int   | None`                                               | Optional limit for instance policy |
| `__recursive__`       | `bool` | Enables recursive inspection in debug/dump          |                                    |

---

## 🔹 Public API

### Constructor

| Signature    | Description                                                |
|--------------|------------------------------------------------------------|
| `__init__()` | Initializes a new instance with a unique engine identifier |

---

### Accessors

| Method       | Returns | Description                                    |
|--------------|---------|------------------------------------------------|
| `__str__()`  | `str`   | Human-readable representation of the object    |
| `__repr__()` | `str`   | Developer representation including internal id |

---

### Mutators

No explicit mutator methods are defined.

---

### Core Methods

| Method      | Description                                            |
|-------------|--------------------------------------------------------|
| `to_dict()` | Serializes public attributes into a dictionary         |
| `debug()`   | Recursive formatted tree visualization of object graph |
| `dump()`    | Lightweight structural dump of object state            |

---

### Utility Methods

No additional utility methods are defined.

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
UUID Generation (jeid)
   │
   ▼
Initialization (__init__)
   │
   ▼
Runtime Usage (engine integration)
   │
   ▼
Debug / Dump inspection (on-demand)
   │
   ▼
Destruction (garbage collected)
```

---

## 🔹 Internal Behavior

The class operates as a foundational introspection and identity layer:

* Each instance receives a unique hexadecimal identifier (`jeid`) using UUID4
* Public attributes are automatically filtered for serialization via `to_dict`
* Private attributes (prefixed with `_`) are excluded from external serialization
* Recursive inspection (`debug`) traverses:

  * Engine objects (`JEInternClassBase`)
  * Collections (list, tuple, set, dict)
  * Properties dynamically resolved at runtime
* Cycle detection is enforced using `_visited` and `_stack` sets
* ANSI color rendering is optionally applied through external console utilities
* `dump()` provides a simplified structural snapshot of the object graph

---

## 🔹 Execution Flow

### `debug()` flow

```text
debug()
   │
   ▼
Initialize color system
   │
   ▼
Collect public attributes
   │
   ├── Direct attributes (__dict__)
   ├── Properties (dir scan)
   │
   ▼
Classify each value
   │
   ├── Engine object → recursive debug()
   ├── Collection → iterate children
   ├── Primitive → formatted leaf
   │
   ▼
Cycle detection check
   │
   ▼
Render tree output
   │
   ▼
Return formatted string
```

### `dump()` flow

```text
dump()
   │
   ▼
Collect raw attributes + properties
   │
   ▼
Detect circular references
   │
   ▼
Classify values
   │
   ├── Engine object → recursive dump()
   ├── Collection → summarized view
   ├── Primitive → direct representation
   │
   ▼
Build ASCII tree
   │
   ▼
Return formatted string
```

---

## 🔹 Usage

### Basic Example

```python
base = JEInternClassBase()
print(base)
```

---

### Realistic Example

```python
entity = SomeEngineObject()
print(entity.to_dict())

print(entity.debug(is_colored=True, max_depth=3))
print(entity.dump())
```

---

## 🔹 Design Decisions

* Centralized base class ensures consistent identity across all engine systems
* UUID-based `jeid` guarantees global uniqueness without external registry
* Separation between `debug()` (rich visualization) and `dump()` (lightweight inspection)
* Recursive traversal enables full object graph inspection for debugging complex engine states
* Explicit filtering of private attributes enforces encapsulation principles
* External console system used for optional color rendering without coupling core logic

---

## 🔹 Performance Notes

* Time complexity:

  * `to_dict`: O(n) over public attributes
  * `debug`: O(n + m) where n = attributes, m = recursive graph nodes
  * `dump`: O(n + m) with reduced overhead vs debug
* Memory usage:

  * Temporary structures for traversal stacks and visited sets
* Cache behavior:

  * No persistent caching; reflection-based evaluation each call
* Allocation notes:

  * Heavy string construction during debug rendering
  * Recursive calls may increase stack usage for deep graphs

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Shared traversal sets are local per call, but object mutation is not synchronized
- Concurrent modification of object state during debug/dump may produce inconsistent output
- UUID generation is thread-safe
```

---

## 🔹 Limitations

* Reflection-based inspection can be expensive on large object graphs
* No protection against deep recursion beyond cycle detection
* Output formatting depends on external console utilities
* No strict schema enforcement for public attributes
* Debug output may vary depending on runtime environment

---

## 🔹 Edge Cases

* Circular references in object graphs
* Properties raising exceptions during evaluation
* Non-repr-safe objects in attributes
* Extremely deep recursion chains
* Concurrent mutation during traversal
* Missing external console module for colored output

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* UUID-based identity system (`jeid`)
* `__str__` and `__repr__` formatting
* `to_dict` public serialization
* Recursive `debug` system
* Structured `dump` inspection
* Property introspection support

### Planned

* Optimized caching for debug trees
* Configurable recursion depth limits
* Faster non-reflection serialization mode
* Enhanced thread-safe inspection mode
* Structured logging integration

---

## 🔹 Debugging

### dump usage

```python
obj.dump()
```

Used for quick structural overview of the object.

### debug usage

```python
obj.debug(is_colored=True, max_depth=5)
```

Used for detailed hierarchical inspection with optional color output.

### Failure signals

* Recursion errors in deep object graphs
* Missing attribute or property access exceptions
* Inconsistent output due to runtime mutation
* Performance degradation on large hierarchies

---

## 🔹 Related Classes

* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEInternEntityComponent`](JEInternEntityComponent.md)📎
* [`JEInternConfig`](JEInternConfig.md)📎
* [`JEContainer`](JEContainer.md)📎

---

## 🔹 Notes

This class is a fundamental building block of JarEngine. It defines the introspection and identity layer used across almost all internal systems and is critical for debugging and engine diagnostics.
