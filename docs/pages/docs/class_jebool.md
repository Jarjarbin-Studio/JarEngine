---
layout: page
title: JarEngine - Class - JEBool
sidebar: sidebar
permalink: /class_jebool.html
---

# 📦 JEBool

> Technical reference for the `JEBool` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEBool` is responsible for providing a JarEngine-compatible boolean wrapper.**

Provides:
* Boolean value storage
* Python boolean conversion
* Boolean inversion support

It is used throughout JarEngine when a custom boolean object is required for engine consistency, debugging, or internal systems.

---

## 🔹 Location

```text
JarEngine
│
├── Systems
│     └── JEBool
│
└── ...
```

---

## 🔹 Data

| Field |  Type  | Description            | Property? | Can be set? |
|:-----:|:------:|------------------------|:---------:|:-----------:|
|  `b`  | `bool` | Internal boolean value |   True    |    False    |

---

## 🔹 API

|   Function   |  Arguments   | Returns  | Description                             |
|:------------:|:------------:|:--------:|-----------------------------------------|
| `__init__()` | `value: Any` |          | Creates a boolean wrapper               |
| `__bool__()` |              |  `bool`  | Converts the object to a Python boolean |
| `__int__()`  |              |  `int`   | Converts the boolean to an integer      |
| `__call__()` |              | `JEBool` | Returns the reversed boolean value      |

---

## 🔹 Usage

```python
from jarengine import Systems

# Create JarEngine booleans (automatically created in JarEngine constants)
enabled = Systems.JEBool(True)
disabled = Systems.JEBool(False)

# Use in conditions
if enabled:
    print("Feature enabled")

# Get integer representation
print(int(enabled))

# Reverse the boolean
print(disabled())
```

---
