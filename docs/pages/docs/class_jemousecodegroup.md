---
layout: page
title: JarEngine - Class - JEMouseCodeGroup
sidebar: sidebar
permalink: /class_jemousecodegroup.html
---

# 📦 JEMouseCodeGroup

> Technical reference for the `JEMouseCodeGroup` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEMouseCodeGroup` is responsible for grouping multiple mouse codes into a single mouse input collection.**

Provides:
* Storage of multiple `JEMouseCode` objects.
* Mouse group combination through operator overloading.
* Iteration support over stored mouse codes.

Represents a collection of mouse identifiers used by JarEngine's input system. It allows multiple mouse buttons to be handled together, simplifying input comparisons while keeping compatibility with individual `JEMouseCode` objects.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEMouseCodeGroup
│
└── ...
```

---

## 🔹 Data

|  Field   |        Type         | Description                                | Property? | Can be set? |
|:--------:|:-------------------:|--------------------------------------------|:---------:|:-----------:|
| `mouses` | `list[JEMouseCode]` | Stored mouse codes contained in the group. |   True    |    False    |

---

## 🔹 API

|  Function  |                Arguments                 |         Returns         | Description                                                                              |
|:----------:|:----------------------------------------:|:-----------------------:|------------------------------------------------------------------------------------------|
| `__init__` |       `mouses: list[JEMouseCode]`        |                         | Creates a mouse group from a list of mouse codes.                                        |
|  `__or__`  | `other: JEMouseCode \| JEMouseCodeGroup` |   `JEMouseCodeGroup`    | Creates a new mouse group by combining existing mouse codes with another mouse or group. |
| `__iter__` |                                          | `Iterator[JEMouseCode]` | Returns an iterator over the stored mouse codes.                                         |

---

## 🔹 Usage

```python
from jarengine import Events

left_click = Events.Mouse.JEMouseCode(1)
right_click = Events.Mouse.JEMouseCode(3)

mouse_group = left_click | right_click

for mouse in mouse_group:
    print(int(mouse))
```

---
