---
layout: page
title: Module - Systems | Class - JEVector3D
sidebar: sidebar
permalink: /JEVector3D.html
---

# 📦 JEVector3D

> Technical reference for the `JEVector3D` of JarEngine.

---

## 🔹 Overview

**`JEVector3D` is a JarEngine class responsible for representing and manipulating a 3D mathematical vector (x, y, z) inside the `systems` module.**

It provides:

* Storage of 3D coordinates
* Direct access and mutation of components
* Iteration over vector components

---

## 🔹 Purpose

The purpose of `JEVector3D` is to:

* Represent spatial positions or directions in 3D space
* Provide a lightweight mathematical structure for engine computations
* Enable direct and efficient component access

It is **not** a physics or transformation system, but a **data container for 3D vector values**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── systems
│     ├── ...
│     ├── JEVector3D
│     └── ...
└── ...
```

`JEVector3D` is a low-level mathematical structure used by higher-level systems such as transforms, rendering calculations, and potential future 3D extensions.

---

## 🔹 Class Relationships

### Uses

* None

---

## 🔹 Data Model

| Field     | Type          | Description                              |
|-----------|---------------|------------------------------------------|
| `_vector` | `list[float]` | Internal storage of (x, y, z) components |

---

## 🔹 Public API

### Constructor

| Signature           | Description                                                |
|---------------------|------------------------------------------------------------|
| `__init__(x, y, z)` | Creates a 3D vector initialized with coordinates (x, y, z) |

---

### Accessors

| Method | Returns | Description         |
|--------|---------|---------------------|
| `x()`  | `float` | Returns X component |
| `y()`  | `float` | Returns Y component |
| `z()`  | `float` | Returns Z component |

---

### Mutators

| Method | Description      |
|--------|------------------|
| `x =`  | Sets X component |
| `y =`  | Sets Y component |
| `z =`  | Sets Z component |

---

### Core Methods

| Method     | Description                        |
|------------|------------------------------------|
| `__iter__` | Iterates over (x, y, z) components |

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

A vector is typically created during entity initialization or system computations and remains active throughout transformations, movement, or rendering calculations.

---

## 🔹 Internal Behavior

`JEVector3D` stores its values in a mutable list `_vector`.

Key behaviors:

* Direct indexing is used for performance (`_vector[0]`, `_vector[1]`, `_vector[2]`)
* No validation is performed on assignments (engine assumes numeric correctness)
* Iteration exposes raw components in order (x → y → z)
* Fixed-size structure (always 3 elements expected)

This class is intentionally minimal to ensure suitability for ECS and performance-critical systems.

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
v = JEVector3D(10, 20, 30)

print(v.x)
print(v.y)
print(v.z)

v.x = 100
v.y = 200
v.z = 300
```

---

### Realistic Example

```python
camera.position.x += velocity.x * dt
camera.position.y += velocity.y * dt
camera.position.z += velocity.z * dt
```

---

## 🔹 Design Decisions

* Minimal abstraction for performance in ECS and rendering loops
* Direct attribute access instead of getter-heavy API
* Mutable internal structure for fast updates
* Designed for future extensibility toward 3D systems (camera, physics, rendering)

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
* Intended for single-threaded engine loop execution

---

## 🔹 Limitations

* No vector arithmetic operations (add, subtract, dot product not implemented)
* No normalization or length utilities
* No type validation on inputs
* No immutability guarantees

---

## 🔹 Edge Cases

* Assigning non-numeric values may break engine logic
* Iteration assumes exactly 3 elements in `_vector`
* No bounds or safety checks for component integrity

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* 3D vector storage
* Component access (x, y, z)
* Iteration support

### Planned

* Vector arithmetic operations
* Operator overloading
* Utility functions (normalize, length, dot product)
* Integration with physics and camera systems

---

## 🔹 Debugging

* Use `dump()` to inspect internal structure
* Use `debug()` for formatted value inspection
* Verify values during transformation or movement updates

---

## 🔹 Related Classes

* [`JEVector2D`](JEVector2D.md)📎

---

## 🔹 Notes

`JEVector3D` is intentionally minimal and optimized for ECS-style usage. Higher-level systems are responsible for mathematical operations and transformations.
