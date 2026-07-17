---
layout: page
title: JarEngine - Class - JEVersion
sidebar: sidebar
permalink: /class_jeversion.html
---


# 📦 JEVersion

> Technical reference for the `JEVersion` class of JarEngine.

> Inherit from `PyGame.version.SoftwareVersion` and [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEVersion` is a JarEngine class responsible for versions storing (JarEngine, PyGame, SDL and Python).**

Provides:
* Formated version

This class is used in the constants, for JarEngine, PyGame, SDL and Python’s versions.
You can use it to store your game's version.

---

## 🔹 Location

```text
JarEngine
│
├── Systems
│     └── JEVersion
│
└── ...
```

---

## 🔹 Data

|  Field  | Type  | Description                                             | Public? | Can be set? |
|:-------:|:-----:|---------------------------------------------------------|:-------:|:-----------:|
| `major` | `int` | Incompatible API changes.                               |  True   |    False    |
| `minor` | `int` | Functionality is added in a backward-compatible manner. |  True   |    False    |
| `patch` | `int` | Backward-compatible bug fixes are made.                 |  True   |    False    |

---

## 🔹 API

|    Function     |                Arguments                 | Returns | Description          |
|:---------------:|:----------------------------------------:|:-------:|----------------------|
| `__init__(...)` | `major: int`, `minor: int`, `patch: int` |         | JEVersion creator.   |
| `__str__(...)`  |                                          |  `str`  | Printable JEVersion. |

---

## 🔹 Usage

```python
from jarengine.systems import JEVersion

# Create a version object
game_version = JEVersion(3, 1, 12)

# Print the version
print(game_version)         # 3.1.12

# Access individual components
print(game_version.major)   # 3
print(game_version.minor)   # 1
print(game_version.patch)   # 12

# Compare versions
minimum = JEVersion(3, 0, 0)

if game_version >= minimum:
    print("Compatible version")

# Versions behave like tuples
major, minor, patch = game_version

print(major)                # 3
print(minor)                # 1
print(patch)                # 12
```

---

## 🔹 Related

* [`>...<`]()📎
* [`>...<`]()📎

---
