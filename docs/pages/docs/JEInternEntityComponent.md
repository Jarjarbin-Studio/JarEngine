---
layout: page
title: Module - Interns | Module - HighClasses | Class - JEInternOwnership
sidebar: sidebar
permalink: /JEInternOwnership.html
---

# 📦 JEInternEntityComponent

> Technical reference for the `JEInternEntityComponent` of JarEngine.

---

## 🔹 Overview

**`JEInternEntityComponent` is a JarEngine class responsible for binding components to entities and integrating them into the ownership and component system inside the `interns` module.**

It provides:

* Automatic registration to an owning entity
* Ownership linkage through parent tracking
* Base structure for entity-component integration

---

## 🔹 Purpose

The purpose of `JEInternEntityComponent` is to:

* Attach components to an entity at construction time
* Ensure proper registration inside the entity component system
* Maintain structural relationships between entities and their components

It is **not** a standalone gameplay object, but a **low-level ECS component base class**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── interns
│     ├── JEInternGraphic
│     ├── JEInternOwnership
│     ├── JEInternEntityComponent
│     └── ...
└── ...
```

This class sits between the entity system and internal component architecture, acting as a bridge for automatic registration and ownership binding.

---

## 🔹 Class Relationships

### Uses

* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEInternOwnership`](JEInternOwnership.md)📎
* [`JEEntity`](JEEntity.md)📎

---

## 🔹 Data Model

| Field           | Type       | Description                                        |
|-----------------|------------|----------------------------------------------------|
| inherited       | varies     | Inherits graphical identity and ownership behavior |
| owner reference | `JEEntity` | Entity that owns this component                    |
| type reference  | `type`     | Component type identifier                          |

This class does not define explicit additional storage fields beyond initialization-time relationships.

---

## 🔹 Public API

### Constructor

| Signature                | Description                                                                |
|--------------------------|----------------------------------------------------------------------------|
| `__init__(owner, _type)` | Creates a component, registers it to the owner entity, and binds ownership |

---

### Accessors

None explicitly defined.

---

### Mutators

None explicitly defined.

Component lifecycle and registration are handled automatically at construction time.

---

### Core Methods

| Method       | Description                                                   |
|--------------|---------------------------------------------------------------|
| `__call__()` | Placeholder callable interface for derived component behavior |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Initialization (bind to entity)
   │
   ▼
Registration into entity component system
   │
   ▼
Runtime usage inside ECS update loop
   │
   ▼
Destruction
```

During initialization, the component automatically registers itself into its owning entity.

---

## 🔹 Internal Behavior

Internally, `JEInternEntityComponent` performs automatic ECS binding:

* Calls `super().__init__()` to initialize graphical identity
* Generates a name using `_type` and `owner.jeid`
* Registers itself to the owner via `owner.add_component(self)`
* Establishes parent relationship using `add_parent(owner)`
* Provides a callable interface placeholder (`__call__`) for derived implementations

This design ensures that every component is immediately integrated into the ECS structure upon creation without manual registration.

---

## 🔹 Execution Flow

```text
Component creation
   │
   ▼
Initialize base graphic identity
   │
   ▼
Bind to owner entity (add_parent)
   │
   ▼
Register component in entity (add_component)
   │
   ▼
Expose runtime interface (__call__)
```

---

## 🔹 Usage

### Basic Example

```python
component = JEInternEntityComponent(owner_entity, MyComponentType)
```

---

### Realistic Example

```python
class TransformComponent(JEInternEntityComponent):
    def __init__(self, owner):
        super().__init__(owner, TransformComponent)

    def __call__(self):
        # component logic
        pass
```

---

## 🔹 Design Decisions

* Automatic registration reduces boilerplate in ECS setup
* Ownership binding ensures consistent entity-component relationships
* Type-based naming improves debugging and introspection
* Callable interface allows flexible extension without strict API constraints

---

## 🔹 Performance Notes

* Time complexity: O(1) for initialization
* Memory usage: O(1) per component (excluding external references)
* Minimal overhead after construction
* Optimized for large-scale ECS entity populations

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Registration modifies entity state directly
- Intended for single-threaded ECS update loop
```

---

## 🔹 Limitations

* No built-in component removal logic
* No enforcement of component uniqueness per entity
* Depends on external entity implementation (`add_component`)
* Callable interface is unimplemented by default

---

## 🔹 Edge Cases

* Missing or invalid owner may break initialization
* Duplicate component registration depends on entity logic
* `_type` must provide a valid `__name__` attribute
* `__call__` does nothing unless overridden

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* Automatic entity registration
* Ownership binding
* Base ECS component structure

### Planned

* Component lifecycle hooks (on_attach, on_detach)
* Validation of component uniqueness
* Strong typing enforcement
* Event-driven component updates

---

## 🔹 Debugging

* Use `dump()` to inspect ownership and registration state
* Verify entity component list when debugging missing behavior
* Override `__call__` to trace execution flow

---

## 🔹 Related Classes

* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEInternOwnership`](JEInternOwnership.md)📎
* [`JEEntity`](JEEntity.md)📎

---

## 🔹 Notes

This class is a core ECS integration point in JarEngine, ensuring that components are correctly bound and registered at creation time with minimal manual intervention.
