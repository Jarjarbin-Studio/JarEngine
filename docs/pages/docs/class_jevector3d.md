---
layout: page
title: JarEngine - Class - JEVector3D
sidebar: sidebar
permalink: /class_jevector3d.html
---

# 📦 <Class Name>

> Technical reference for the `JEVector3D` class of JarEngine.

> Inherit from [`•>JETransform<•`]()📎

---

## 🔹 Overview

**`JEVector3D` is a JarEngine class responsible for advanced specialized floats storing.**

It provides:

* x and y float storage.
* Transformation helpers (through inheritance).

JEVector3D is used everywhere in JarEngine.

---

## 🔹 Location

```text
JarEngine
│
├── Systems
│     └── JEVector3D
│
└── ...
```

---

## 🔹 Data

|  Field   |     Type      | Description   | Property? | Can be set? |
|:--------:|:-------------:|---------------|:---------:|:-----------:|
|   `x`    |    `float`    | Value storage |   True    |    True     |
|   `y`    |    `float`    | Value storage |   True    |    True     |
|   `z`    |    `float`    | Value storage |   True    |    True     |

---

## 🔹 API

|    Function     |                      Arguments                       | Returns           | Description              |
|:---------------:|:----------------------------------------------------:|-------------------|--------------------------|
| `__init__(...)` | `x: float = 0.0`, `y: float = 0.0`, `z: float = 0.0` |                   | JEVector3D creator.      |
| `__iter__(...)` |                                                      | `Iterator[float]` | Iterate over the vector. |

---

## 🔹 Usage

```python
from jarengine.systems import JEVector3D

# Create 3D vectors
position = JEVector3D(10, 5, 2)
velocity = JEVector3D(1, 0, -1)

# Vector addition (movement simulation)
new_position = position + velocity

print(new_position)
# Output: JEVector3D(11, 5, 1)


# Scale a vector
speed = velocity * 5

print(speed)
# Output: JEVector3D(5, 0, -5)


# Normalize a direction vector
direction = JEVector3D(10, 0, 0)

normalized = direction.normalize()

print(normalized)
# Output: JEVector3D(1.0, 0.0, 0.0)


# Calculate distance between two points
player = JEVector3D(0, 0, 0)
enemy = JEVector3D(10, 0, 5)

distance = player.distance(enemy)

print(distance)
# Output: 11.18...


# Dot product for direction comparison
forward = JEVector3D(0, 0, 1)
movement = JEVector3D(0, 0, 5)

alignment = forward.dot(movement)

print(alignment)
# Output: 5


# Modify vectors directly
position += JEVector3D(0, 10, 0)
position *= 2

print(position)
# Output: JEVector3D(22, 30, 2)


# Access individual components
position.x = 100
position.z = -20

print(position.x, position.y, position.z)
# Output: 100 30 -20


# Convert vector data
values = position.to_list()

print(values)
# Output: [100, 30, -20]
```

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
