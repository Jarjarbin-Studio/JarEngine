---
layout: page
title: Module - Interns | Module - HighClasses | Class - JEInternSystems
sidebar: sidebar
permalink: /JEInternSystems.html
---

# 📦 JEInternSystems

> Technical reference for the `JEInternSystems` of JarEngine.

---

## 🔹 Overview

**`JEInternSystemss` is a JarEngine internal class responsible for managing and organizing gameplay systems inside the `Internals/Systems` module.**

It provides:

* System ownership and registration within a game instance
* Entity filtering based on required components
* System update dispatch logic

---

## 🔹 Purpose

The purpose of `JEInternSystemss` is to:

* Centralize system registration inside the engine
* Define system-level requirements for entity processing
* Provide a unified update entry point for ECS-like behavior

It is **not** a gameplay object itself, but a **structural execution layer for engine logic**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── Interns
│     ├── Ownership
│     ├── EntityComponent
│     ├── Systems   <-- JEInternSystemss
│     └── ...
└── Game
```

This class sits inside the internal architecture layer and acts as a bridge between the game instance and system-level logic execution.

---

## 🔹 Class Relationships

### Uses

* [`JEGame`](JEGame.md)📎
* [`JEWindow`](JEWindow.md)📎
* [`JEEntity`](JEEntity.md)📎
* [`JEContainer`](JEContainer.md)📎
* [`JEInternEntityComponent`](JEInternEntityComponent.md)📎

---

## 🔹 Data Model

| Field       | Type          | Description                                    |
|-------------|---------------|------------------------------------------------|
| `_parents`  | `JEContainer` | Owner references (game/system hierarchy)       |
| `_children` | `JEContainer` | Child systems if composed                      |
| `_required` | `list[type]`  | Component types required for entity processing |

---

## 🔹 Public API

### Constructor

| Signature                 | Description                                                            |
|---------------------------|------------------------------------------------------------------------|
| `__init__(owner: JEGame)` | Registers system under a game instance and initializes ownership links |

---

### Accessors

| Method     | Returns       | Description           |
|------------|---------------|-----------------------|
| `parents`  | `JEContainer` | Returns parent owners |
| `children` | `JEContainer` | Returns child systems |

---

### Mutators

| Method                | Description                                     |
|-----------------------|-------------------------------------------------|
| `accepts(components)` | Checks if an entity has all required components |

---

### Core Methods

| Method                                 | Description                                              |
|----------------------------------------|----------------------------------------------------------|
| `update(window, entity, entities, dt)` | Static system update entry point for processing entities |

---

## 🔹 Utility Methods

| Method      | Description                                           |
|-------------|-------------------------------------------------------|
| `accepts()` | Validates whether a system can process a given entity |
| `update()`  | Executes system logic across entities                 |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
System Registration (Game binding)
   │
   ▼
Requirement Definition
   │
   ▼
Runtime Entity Filtering
   │
   ▼
System Update Loop
   │
   ▼
Destruction
```

At creation, the system is attached to a `JEGame` instance and registered internally. During runtime, it continuously evaluates entity compatibility and executes update logic.

---

## 🔹 Internal Behavior

The class acts as a lightweight ECS system controller:

* Each system declares required components in `_required`
* `accepts()` checks entity compatibility using container lookups
* Update logic is executed through a static dispatcher
* Ownership ensures systems remain linked to the game lifecycle

This design allows separation between:

* entity data
* system logic
* execution scheduling

---

## 🔹 Execution Flow

```text
Game Loop
   │
   ▼
System Iteration
   │
   ▼
accepts(entity.components)
   │
   ▼
If valid → update(window, entity, entities, dt)
   │
   ▼
Apply system logic
   │
   ▼
Return
```

Each system evaluates entities individually before processing them, ensuring modular execution.

---

## 🔹 Usage

### Basic Example

```python
system = JEInternSystemss(game)
system._required = [PositionComponent, RenderComponent]
```

---

### Realistic Example

```python
for entity in entities:
    if system.accepts(entity.components):
        system.update(window, entity, entities, dt)
```

---

## 🔹 Design Decisions

* ECS-style architecture for scalability
* Separation of system logic from entity storage
* Ownership model ensures lifecycle consistency with `JEGame`
* Static update method avoids unnecessary instance coupling
* Component filtering optimized through container-based lookup

---

## 🔹 Performance Notes

* Entity filtering: O(n) per system per frame
* Component lookup depends on `JEContainer` implementation
* Designed for predictable update loops rather than dynamic reflection
* Minimal allocation during runtime execution

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Shared game state is mutated during update cycles
- Systems assume single-threaded game loop execution
```

---

## 🔹 Limitations

* No built-in parallel system execution
* `_required` list is manually managed
* No automatic dependency resolution between systems

---

## 🔹 Edge Cases

* Missing component types in `components.get()` → safe failure returning `False`
* Invalid container input → caught and converted to `False`
* Empty `_required` list → system accepts all entities

---

## 🔹 Current State

### Implemented

* System ownership binding
* Entity compatibility check
* Static update dispatcher

### Planned

* System ordering / priority layers
* Parallel system execution
* Dependency graph between systems

---

## 🔹 Debugging

* Use `accepts()` to validate entity processing eligibility
* Inspect `_required` for missing component definitions
* Trace update calls inside game loop
* Validate container contents for missing components

---

## 🔹 Related Classes

* [`JEGame`](JEGame.md)📎
* [`JEEntity`](JEEntity.md)📎
* [`JEContainer`](JEContainer.md)📎
* [`JEInternEntityComponent`](JEInternEntityComponent.md)📎

---

## 🔹 Notes

This class is a core ECS execution layer and should remain lightweight. Most complexity should stay in systems built on top of it rather than inside it.
