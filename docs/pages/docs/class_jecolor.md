---
layout: page
title: JarEngine - Class - JEColor
sidebar: sidebar
permalink: /class_jecolor.html
---

# 📦 JEColor

> Technical reference for the `JEColor` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEColor` is responsible for storing and manipulating RGBA color values.**

Provides:
* RGB and RGBA channel storage
* Individual channel access
* Color iteration support

It is used for graphical operations such as entity colors, rendering settings, and visual components.

---

## 🔹 Location

```text
JarEngine
│
├── Systems
│     └── JEColor
│
└── ...
```

---

## 🔹 Data

| Field  |            Type             | Description                 | Property? | Can be set? |
|:------:|:---------------------------:|-----------------------------|:---------:|:-----------:|
|  `r`   |            `int`            | Red channel value (0-255)   |   True    |    True     |
|  `g`   |            `int`            | Green channel value (0-255) |   True    |    True     |
|  `b`   |            `int`            | Blue channel value (0-255)  |   True    |    True     |
|  `a`   |            `int`            | Alpha channel value (0-255) |   True    |    True     |
| `rgb`  |   `tuple[int, int, int]`    | RGB color tuple             |   True    |    False    |
| `rgba` | `tuple[int, int, int, int]` | RGBA color tuple            |   True    |    False    |

---

## 🔹 API

|   Function   |            Arguments             |      Returns      | Description                     |
|:------------:|:--------------------------------:|:-----------------:|---------------------------------|
| `__init__()` | `r: int, g: int, b: int, a: int` |                   | Creates a color object          |
| `__iter__()` |                                  | `Iterator[float]` | Iterates through color channels |

---

## 🔹 Usage

```python
from jarengine import Systems

# Create a color
white = Systems.JEColor(
    255,
    255,
    255
)

# Modify channels
white.r = 200
white.a = 128

# Access color values
print(white.rgb)
print(white.rgba)

# Iterate through channels
for channel in white:
    print(channel)
```

---
