---
layout: page
title: JarEngine - Class - JEKeyCodeGroup
sidebar: sidebar
permalink: /class_jekeycodegroup.html
---

# 📦 JEKeyCodeGroup

> Technical reference for the `JEKeyCodeGroup` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEKeyCodeGroup` is responsible for grouping multiple key codes into a single key collection.**

Provides:
* Storage of multiple `JEKeyCode` objects.
* Key group combination through operator overloading.
* Iteration support over stored keys.

Represents a collection of keyboard input identifiers used by JarEngine's input system. It allows multiple keys to be handled together, simplifying key combinations and input processing while maintaining compatibility with individual `JEKeyCode` objects.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEKeyCodeGroup
│
└── ...
```

---

## 🔹 Data

| Field  |       Type        | Description                              | Property? | Can be set? |
|:------:|:-----------------:|------------------------------------------|:---------:|:-----------:|
| `keys` | `list[JEKeyCode]` | Stored key codes contained in the group. |   True    |    False    |

---

## 🔹 API

|  Function  |              Arguments               |        Returns        | Description                                                                        |
|:----------:|:------------------------------------:|:---------------------:|------------------------------------------------------------------------------------|
| `__init__` |       `keys: list[JEKeyCode]`        |                       | Creates a key group from a list of key codes.                                      |
|  `__or__`  | `other: JEKeyCode \| JEKeyCodeGroup` |   `JEKeyCodeGroup`    | Creates a new key group by combining existing key codes with another key or group. |
| `__iter__` |                                      | `Iterator[JEKeyCode]` | Returns an iterator over the stored key codes.                                     |

---

## 🔹 Usage

```python
from jarengine import Events

jump_key = Events.Keyboard.JEKeyCode(32)
run_key = Events.Keyboard.JEKeyCode(16)

key_group = jump_key | run_key

for key in key_group:
    print(int(key))
```

---
