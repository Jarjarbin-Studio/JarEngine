---
layout: page
title: Module - Interns | Module - HighClasses | Class - JEInternOwnership
sidebar: sidebar
permalink: /JEInternOwnership.html
---

# 📦 JEInternOwnership

> Technical reference for the `JEInternOwnership` of JarEngine.

---

## 🔹 Overview

**`JEInternOwnership` is a JarEngine class responsible for managing hierarchical ownership relationships between engine objects inside the `interns` module.**

It provides:

* Parent/child relationship tracking between objects
* Bidirectional ownership graph structure
* Container-based storage of linked engine entities

---

## 🔹 Purpose

The purpose of `JEInternOwnership` is to:

* Represent structural relationships between engine objects
* Enable hierarchical propagation of ownership (scene graph-like structure)
* Provide a reusable base for components, systems, and entities requiring linkage

It is **not** a scene graph implementation, but a **low-level ownership and relationship management layer**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── interns
│     ├── JEInternGraphic
│     ├── JEInternOwnership
│     ├── JEInternEntityComponent
│     ├── JEInternRenderingSystems
│     └── ...
└── ...
```

This class acts as a foundational mixin for internal engine structures requiring parent-child relationships.

---

## 🔹 Class Relationships

### Uses

* [`JEContainer`](JEContainer.md)📎
* [`JEInternBaseClass`](JEInternBaseClass.md)📎

---

## 🔹 Data Model

| Field       | Type          | Description                         |
|-------------|---------------|-------------------------------------|
| `_parents`  | `JEContainer` | Stores references to parent objects |
| `_children` | `JEContainer` | Stores references to child objects  |

Both structures maintain runtime relationships between engine objects.

---

## 🔹 Public API

### Constructor

| Signature    | Description                                   |
|--------------|-----------------------------------------------|
| `__init__()` | Initializes empty parent and child containers |

---

### Accessors

| Method     | Returns       | Description                 |
|------------|---------------|-----------------------------|
| `parents`  | `JEContainer` | Returns parent objects list |
| `children` | `JEContainer` | Returns child objects list  |

---

### Mutators

| Method         | Description                      |
|----------------|----------------------------------|
| `add_parent()` | Adds a parent object to the node |
| `add_child()`  | Adds a child object to the node  |

---

### Core Methods

None.

This class is purely structural and does not define runtime behavior.

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Initialization
   │
   ▼
Relationship Binding
   │
   ▼
Runtime Hierarchy Usage
   │
   ▼
Destruction
```

Relationships are typically established during object initialization or system registration and persist throughout runtime.

---

## 🔹 Internal Behavior

Internally, `JEInternOwnership`:

* Uses `JEContainer` instances to store relationships
* Does not enforce strict tree constraints (graph-like structure possible)
* Allows multiple parents and multiple children
* Relies on external systems to maintain consistency

This design keeps ownership logic decoupled from engine-specific rules, allowing flexible composition patterns.

---

## 🔹 Execution Flow

```text
Object creation
   │
   ▼
Add parent / child relationships
   │
   ▼
Store references in containers
   │
   ▼
External systems traverse hierarchy
   │
   ▼
Optional cleanup on destruction
```

---

## 🔹 Usage

### Basic Example

```python
node = JEInternOwnership()

node.add_parent(parent_obj)
node.add_child(child_obj)

print(node.parents)
print(node.children)
```

---

### Realistic Example

```python
def build_scene_graph(entity, parent):
    entity.add_parent(parent)
    parent.add_child(entity)
```

---

## 🔹 Design Decisions

* Uses explicit containers to avoid hidden ownership logic
* Supports multiple parents for flexible engine architecture
* Decouples relationship management from gameplay systems
* Designed for reuse across entities, components, and systems

---

## 🔹 Performance Notes

* Time complexity:

  * Add parent/child: O(1) amortized
  * Access: O(1)
* Memory usage: O(n) per relationship set
* Minimal overhead due to container abstraction
* Suitable for large entity graphs

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Containers are not synchronized
- Intended for single-threaded engine update loop
```

---

## 🔹 Limitations

* No automatic bidirectional consistency enforcement
* No cycle detection
* No hierarchy validation rules
* Depends on external systems for integrity

---

## 🔹 Edge Cases

* Adding duplicate parents/children may result in redundant references
* Removing relationships is not handled in this class
* Cyclic graphs are possible and not prevented
* Null or invalid references depend on container behavior

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* Parent tracking system
* Child tracking system
* Container-based relationship storage

### Planned

* Relationship validation
* Automatic inverse linking
* Graph traversal utilities
* Cycle detection tools

---

## 🔹 Debugging

* Use `dump()` to inspect parent/child structures
* Use `debug()` to trace relationship inconsistencies
* Monitor container contents when debugging entity hierarchy issues

---

## 🔹 Related Classes

* [`JEContainer`](JEContainer.md)📎
* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEInternEntityComponent`](JEInternEntityComponent.md)📎
* [`JEInternRenderingSystems`](JEInternRenderingSystems.md)📎

---

## 🔹 Notes

This class forms the foundation of hierarchical structure management in JarEngine. It is intentionally minimal to allow flexible architectural patterns across different engine systems.
