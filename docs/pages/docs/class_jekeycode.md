---
layout: page
title: JarEngine - Class - JEKeyCode
sidebar: sidebar
permalink: /class_jekeycode.html
---

# 📦 JEKeyCode

> Technical reference for the `JEKeyCode` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEKeyCode` is responsible for representing and managing keyboard input codes in JarEngine.**

Provides:
* Keyboard key identification and comparison.
* Conversion between internal key codes and integer values.
* Key code grouping through operator overloading.

Represents a keyboard input identifier used by JarEngine's input system. It allows keyboard keys to be handled as structured objects instead of raw integer values, providing easier comparison, grouping, and debugging capabilities.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEKeyCode
│
└── ...
```

---

## 🔹 Data

| Field  | Type  | Description                       | Property? | Can be set? |
|:------:|:-----:|-----------------------------------|:---------:|:-----------:|
| `name` | `str` | Human-readable keyboard key name. |   True    |    False    |

---

## 🔹 API

|  Function  |      Arguments       |     Returns      | Description                                                             |
|:----------:|:--------------------:|:----------------:|-------------------------------------------------------------------------|
| `__init__` | `key: Optional[int]` |                  | Creates a key code object from an optional keyboard key identifier.     |
| `__int__`  |                      |      `int`       | Converts the key code into its integer representation.                  |
| `__str__`  |                      |      `str`       | Human-readable key name.                                                |
|  `__or__`  |  `other: JEKeyCode`  | `JEKeyCodeGroup` | Creates a key group by combining two key codes.                         |
|  `__eq__`  |  `other: JEKeyCode`  |     `JEBool`     | Compares two key codes and returns whether they represent the same key. |
| `__hash__` |                      |      `int`       | Generates a hash value from the key code for future usage.              |

---

## 🔹 Usage

```python
from jarengine import Events

jump_key = Events.Keyboard.JEKeyCode(32)
escape_key = Events.Keyboard.JEKeyCode(27)

if jump_key == Events.Keyboard.JEKeyCode(32):
    print("Jump key detected")

key_group = jump_key | escape_key
```

---
