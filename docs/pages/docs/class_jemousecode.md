---
layout: page
title: JarEngine - Class - JEMouseCode
sidebar: sidebar
permalink: /class_jemousecode.html
---

# 📦 JEMouseCode

> Technical reference for the `JEMouseCode` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEMouseCode` is responsible for representing and managing mouse input codes in JarEngine.**

Provides:
* Mouse button identification and comparison.
* Conversion between internal mouse codes and integer values.
* Mouse code grouping through operator overloading.

Represents a mouse input identifier used by JarEngine's input system. It allows mouse buttons to be handled as structured objects instead of raw integer values, providing easier comparison, grouping, and debugging capabilities.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEMouseCode
│
└── ...
```

---

## 🔹 Data

| Field  | Type  | Description                       | Property? | Can be set? |
|:------:|:-----:|-----------------------------------|:---------:|:-----------:|
| `name` | `str` | Human-readable mouse button name. |   True    |    False    |

---

## 🔹 API

|  Function  |       Arguments        |      Returns       | Description                                                                  |
|:----------:|:----------------------:|:------------------:|------------------------------------------------------------------------------|
| `__init__` | `mouse: Optional[int]` |                    | Creates a mouse code object from an optional mouse identifier.               |
| `__int__`  |                        |       `int`        | Converts the mouse code into its integer representation.                     |
| `__str__`  |                        |       `str`        | Human-readable mouse name.                                                   |
|  `__or__`  |  `other: JEMouseCode`  | `JEMouseCodeGroup` | Creates a mouse group by combining two mouse codes.                          |
|  `__eq__`  |  `other: JEMouseCode`  |      `JEBool`      | Compares two mouse codes and returns whether they represent the same button. |
| `__hash__` |                        |       `int`        | Generates a hash value from the mouse code for future usage.                 |

---

## 🔹 Usage

```python
from jarengine import Events

left_click = Events.Mouse.JEMouseCode(1)
right_click = Events.Mouse.JEMouseCode(3)

if left_click == Events.Mouse.JEMouseCode(1):
    print("Left mouse button pressed")

mouse_group = left_click | right_click
```

---
