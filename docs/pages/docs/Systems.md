---
layout: page
title: Module - Systems
sidebar: sidebar
permalink: /Systems.html
---

# 📦 Systems Module

> Technical reference for the `systems` module of JarEngine.

---

## 🔹 Overview

**`systems` is a JarEngine module responsible for providing foundational mathematical, data, and utility primitives used across the entire engine.**

It provides the classes and utilities required to:

* Represent geometric vectors for spatial computation
* Handle color abstraction for rendering systems
* Provide boolean wrappers for engine-level logic control
* Offer generic container abstractions for typed storage
* Define immutable data structures for safe state handling

---

## 🔹 Purpose

The `systems` module aims to:

* Provide low-level reusable primitives for all engine layers
* Standardize mathematical and utility representations
* Ensure type-safe containers and immutable structures
* Centralize core data types used by rendering and logic systems

It is **not** a gameplay or entity module, but a **core utility and primitive abstraction layer**.

---

## 🔹 Module Organization

```text
sources/
└── systems/
    ├── __init__.py
    ├── vector.py
    ├── color.py
    ├── bool.py
    ├── container.py
    ├── immutable.py
    └── clock.py
````

| File           | Description                            |
|----------------|----------------------------------------|
| `__init__.py`  | Public exports of system primitives    |
| `vector.py`    | 2D and 3D vector mathematics           |
| `color.py`     | Color representation utilities         |
| `bool.py`      | Engine-level boolean wrapper           |
| `container.py` | Generic typed container implementation |
| `immutable.py` | Immutable data structure utilities     |
| `clock.py`     | Time and clock utilities               |

---

## 🔹 Responsibilities

| Responsibility          | Description                                  |
|-------------------------|----------------------------------------------|
| Mathematical primitives | Vector operations for spatial computation    |
| Rendering data types    | Color representation for rendering pipelines |
| Type-safe storage       | Generic container abstraction                |
| Immutability control    | Prevent modification of critical data        |
| Engine utility types    | Core primitives used across modules          |

---

## 🔹 Public Classes

| Class         | Description                           |
|---------------|---------------------------------------|
| `JEVector2D`  | 2D vector math operations             |
| `JEVector3D`  | 3D vector math operations             |
| `JEColor`     | Color representation and manipulation |
| `JEBool`      | Engine-level boolean wrapper          |
| `JEContainer` | Generic typed storage container       |
| `JEImmutable` | Immutable object base type            |

Each class should have its own dedicated documentation page.

---

## 🔹 Dependencies

### Depends On

* None (pure internal system layer)

These components are designed to be dependency-free to ensure maximum reusability across all engine layers.

---

## 🔹 Data Flow

```text
External Systems
       │
       ▼
   systems module
       │
   ┌── Vector math (JEVector2D / JEVector3D)
   ├── Rendering data (JEColor)
   ├── Logic primitives (JEBool)
   ├── Storage layer (JEContainer)
   └── Safety layer (JEImmutable)
       │
       ▼
Engine High / Low / Final Layers
```

---

## 🔹 Usage

### Basic Example

```python
pos = JEVector2D(10, 20)
color = JEColor(255, 0, 0)
```

---

### Typical Workflow

```python
container = JEContainer(JEVector2D)
container.add(JEVector2D(1, 2))
container.add(JEVector2D(3, 4))
```

This workflow enables:

* typed storage enforcement
* safe iteration over engine objects
* reusable mathematical primitives

---

## 🔹 Design Decisions

The module is designed around:

* strict separation of pure data primitives from engine logic
* minimal dependency footprint for maximum portability
* explicit type enforcement via containers
* immutable structures to avoid unintended side effects
* reusable mathematical abstractions for all engine systems

---

## 🔹 Performance Notes

* Vector operations are designed for low-overhead arithmetic
* Container access is optimized for typed iteration patterns
* Immutable structures reduce mutation costs but may increase allocation frequency
* Module avoids external dependencies for deterministic performance

---

## 🔹 Limitations

* No advanced SIMD or hardware acceleration for vector math
* Immutable structures may increase memory usage in heavy mutation scenarios
* Container type enforcement introduces minor runtime overhead
* Clock utilities are not real-time OS synchronized at high precision

---

## 🔹 Current State

⚠️ Current implementation status.

### Implemented

* Vector2D and Vector3D mathematical structures
* Color representation system
* Generic typed container system
* Immutable base structure
* Boolean wrapper system

### Planned

* Clock and time utilities completion
* Extended vector math optimizations
* Additional numeric utility primitives
* Performance improvements for container iteration

---

## 🔹 Related Modules

* [`Games`](Games.md)📎
* [`Interns`](Interns.md)📎
* [`Entities`](Entities.md)📎
* [`Resources`](Resources.md)📎

---

## 🔹 Notes

This module serves as the foundation for all engine-level data representation. It is intentionally minimal and deterministic to ensure consistent behavior across rendering, logic, and gameplay systems.
