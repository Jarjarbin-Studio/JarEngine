---
layout: page
title: JarEngine - Class - JETransform
sidebar: sidebar
permalink: /class_jetransform.html
---

# 📦 JETransform

> Technical reference for the `JETransform` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JETransform` is the base mathematical transformation class used for vector operations in JarEngine.**

Provides:
* Vector arithmetic operations
* Length and normalization calculations
* Distance and dot product utilities

It is the base class for `JEVector2D` and `JEVector3D`, allowing all vectors to share the same mathematical behavior.

---

## 🔹 Location

```text
JarEngine
│
├── Systems
│     └── JETransform
│
└── Vector classes
      ├── JEVector2D
      └── JEVector3D
````

---

## 🔹 Data

No public data nor property

---

## 🔹 API

| Function        | Arguments     | Returns       | Description                        |
|-----------------|---------------|---------------|------------------------------------|
| `__add__()`     | `JETransform` | `JETransform` | Add two vectors together           |
| `__sub__()`     | `JETransform` | `JETransform` | Subtract two vectors               |
| `__mul__()`     | `JETransform` | `JETransform` | Multiply two vectors               |
| `__truediv__()` | `JETransform` | `JETransform` | Divide two vectors                 |
| `__neg__()`     | None          | `JETransform` | Negate a vector                    |
| `__eq__()`      | `JETransform` | `JEBool`      | Compare two vectors                |
| `__iadd__()`    | `int`         | `JETransform` | Add a scalar value                 |
| `__isub__()`    | `int`         | `JETransform` | Subtract a scalar value            |
| `__imul__()`    | `int`         | `JETransform` | Multiply by a scalar value         |
| `__len__()`     | None          | `float`       | Get vector length                  |
| `length()`      | None          | `float`       | Calculate vector magnitude         |
| `normalize()`   | None          | `JETransform` | Get normalized vector              |
| `dot()`         | `JETransform` | `float`       | Calculate dot product              |
| `distance()`    | `JETransform` | `float`       | Calculate distance between vectors |
| `copy()`        | None          | `JETransform` | Create a vector copy               |
| `to_list()`     | None          | `list`        | Convert vector to list             |
| `__repr__()`    | None          | `str`         | Get vector representation          |

---

## 🔹 Usage

```python
from jarengine import Systems

# Create two vectors
velocity = Systems.JEVector2D(10, 5)
direction = Systems.JEVector2D(1, 0)

# Vector operations
movement = velocity + direction
scaled = velocity * 2

# Vector information
print(velocity.length())
print(velocity.distance(direction))

# Normalize direction
normal = direction.normalize()

print(movement)
print(scaled)
print(normal)
```

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
