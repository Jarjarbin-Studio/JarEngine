---
layout: page
title: Module - Systems | Class - JEVector2D
sidebar: sidebar
permalink: /JEVector2D.html
---

# 📦 JEVector2D

> Technical reference for the `JEVector2D` of JarEngine.

---

## 🔹 Overview

**`JEVector2D` is a JarEngine class responsible for representing and manipulating a 2D mathematical vector (x, y) inside the `systems` module.**

It provides:

* Storage of 2D coordinates
* Direct access and mutation of components
* Iteration over vector components

---

## 🔹 Purpose

The purpose of `JEVector2D` is to:

* Represent spatial positions or directions in 2D space
* Provide a lightweight mathematical structure for engine computations
* Enable direct and efficient component access

It is **not** a physics or transformation system, but a **data container for 2D vector values**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── systems
│     ├── ...
│     ├── JEVector2D
│     └── ...
└── ...
```

`JEVector2D` is a low-level mathematical structure used by higher-level systems such as transforms, movement systems, and rendering calculations.

---

## 🔹 Class Relationships

### Uses

* None

---

## 🔹 Data Model

| Field     | Type          | Description                           |
|-----------|---------------|---------------------------------------|
| `_vector` | `list[float]` | Internal storage of (x, y) components |

---

## 🔹 Public API

### Constructor

| Signature        | Description                                             |
|------------------|---------------------------------------------------------|
| `__init__(x, y)` | Creates a 2D vector initialized with coordinates (x, y) |

---

### Accessors

| Method | Returns | Description         |
|--------|---------|---------------------|
| `x()`  | `float` | Returns X component |
| `y()`  | `float` | Returns Y component |

---

### Mutators

| Method | Description      |
|--------|------------------|
| `x =`  | Sets X component |
| `y =`  | Sets Y component |

---

### Core Methods

| Method     | Description                     |
|------------|---------------------------------|
| `__iter__` | Iterates over (x, y) components |

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
Component Access / Mutation
   │
   ▼
Destruction
```

A vector is typically created during entity initialization or system computation and remains active throughout movement or rendering operations.

---

## 🔹 Internal Behavior

`JEVector2D` stores its values in a mutable list `_vector`.

Key behaviors:

* Direct indexing is used for performance (`_vector[0]`, `_vector[1]`)
* No validation is performed on assignments (engine assumes numeric correctness)
* Iteration exposes raw components in order (x → y)

This class is intentionally minimal to ensure it remains suitable for hot-path usage in ECS systems.

---

## 🔹 Execution Flow

```text
Read / Write Access
   │
   ▼
Direct list index access
   │
   ▼
Return or update value
```

All operations are constant-time and avoid abstraction overhead.

---

## 🔹 Usage

### Basic Example

```python
v = JEVector2D(10, 20)

print(v.x)
print(v.y)

v.x = 30
v.y = 40
```

---

### Realistic Example

```python
player.position.x += velocity.x * dt
player.position.y += velocity.y * dt
```

---

## 🔹 Design Decisions

* Minimal abstraction for performance in ECS loops
* Direct attribute access instead of getters/setters
* Mutable internal structure for fast updates
* Designed for compatibility with movement and physics systems

---

## 🔹 Performance Notes

* Time complexity: O(1) for all operations
* Memory usage: O(1)
* Cache-friendly contiguous storage (`list[float]`)
* No allocations during read/write operations

---

## 🔹 Thread Safety

Thread-safe: No

Notes:

* Mutability makes concurrent access unsafe
* Intended for single-threaded ECS update loop

---

## 🔹 Limitations

* No vector arithmetic operations (add, sub, dot product not implemented)
* No type validation on inputs
* Limited to 2D space only
* No immutability guarantees

---

## 🔹 Edge Cases

* Assigning non-numeric values may break engine logic
* Iteration assumes exactly 2 elements in `_vector`
* No bounds or range validation for components

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* 2D vector storage
* Component access (x, y)
* Iteration support

### Planned

* Vector arithmetic operations
* Operator overloading
* Utility functions (normalize, length, dot product)
* Integration helpers for physics system

---

## 🔹 Debugging

* Use `dump()` to inspect internal structure
* Use `debug()` for formatted value inspection
* Verify values during movement system updates if unexpected motion occurs

---

## 🔹 Related Classes

* [`JEVector3D`](JEVector3D.md)📎

---

## 🔹 Notes

This class is intentionally minimal and optimized for ECS usage. It is expected that higher-level systems handle mathematical operations rather than the vector itself.
