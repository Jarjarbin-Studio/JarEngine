---
layout: page
title: JarEngine - Class - JEVector2D
sidebar: sidebar
permalink: /class_jevector2d.html
---

# 📦 <Class Name>

> Technical reference for the `JEVector2D` class of JarEngine.

> Inherit from [`•>JETransform<•`]()📎

---

## 🔹 Overview

**`JEVector2D` is a JarEngine class responsible for specialized floats storing.**

It provides:

* x and y float storage.
* Transformation helpers (through inheritance).

JEVector2D is used everywhere in JarEngine.

---

## 🔹 Location

```text
JarEngine
│
├── Systems
│     └── JEVector2D
│
└── ...
```

---

## 🔹 Data

|  Field   |     Type      | Description   | Property? | Can be set? |
|:--------:|:-------------:|---------------|:---------:|:-----------:|
|   `x`    |    `float`    | Value storage |   True    |    True     |
|   `y`    |    `float`    | Value storage |   True    |    True     |

---

## 🔹 API

|    Function     |             Arguments              |      Returns      | Description              |
|:---------------:|:----------------------------------:|:-----------------:|--------------------------|
| `__init__(...)` | `x: float = 0.0`, `y: float = 0.0` |                   | JEVector2D creator.      |
| `__iter__(...)` |                                    | `Iterator[float]` | Iterate over the vector. |

---

## 🔹 Usage

```python
from jarengine.systems import JEVector2D

# Create vectors
position = JEVector2D(100, 50)
velocity = JEVector2D(5, -2)

# Access components
print(position.x)       # 100
print(position.y)       # 50

# Modify components
position.x = 150
position.y += 25

# Vector operations (inherited from JETransform)
result = position + velocity
scaled = result * 2
unit = result.normalize()

print(result)           # JEVector2D(155, 73)
print(result.length())  # Vector length

# Iterate over components
for value in result:
    print(value)

# Convert to a standard Python list
coords = result.to_list()
print(coords)           # [155, 73]
```

---
