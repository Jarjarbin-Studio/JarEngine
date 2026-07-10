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

It provides:

* Formated version

---

## 🔹 Purpose

The purpose of this class is to:

* Store version in a printable object

---

## 🔹 Location in JarEngine

```text
JarEngine
│
├── Systems
│     └── JEVersion
│
└── ...
```

This class is used in the constants, for JarEngine, PyGame, SDL and Python’s versions.
You can use it to store your game's version.

---

## 🔹 Data

Internal data stored by this class.

| Field   | Type  | Description                                             | Public? |
|---------|-------|---------------------------------------------------------|:-------:|
| `major` | `int` | Incompatible API changes.                               |  True   |
| `minor` | `int` | Functionality is added in a backward-compatible manner. |  True   |
| `patch` | `int` | Backward-compatible bug fixes are made.                 |  True   |

---

## 🔹 Functions / API

List all public functions available.

| Function                         | Arguments                                | Returns | Description          |
|----------------------------------|------------------------------------------|---------|----------------------|
| [•>`__init__(...)`<•](#__init__) | `major: int`, `minor: int`, `patch: int` |         | JEVersion creator.   |
| [•>`__str__(...)`<•](#__str__)   |                                          | `str`   | Printable JEVersion. |

---

### Argument Details

Additional details for complex functions.

#### __init__

| Argument | Type   | Description                                          |
|----------|--------|------------------------------------------------------|
| `major`  | `type` | Incompatible API changes.                            |
| `minor`  | `type` | Functionality added in a backward-compatible manner. |
| `patch`  | `type` | Backward-compatible bug fixes.                       |

---

#### __str__

**Returns:**

| Type  | Description          |
|-------|----------------------|
| `str` | Printable JEVersion. |

---

## 🔹 Usage

### Basic Example

```python
from jarengine.Systems import JEVersion

JEVersion_MyGame = JEVersion(3, 1, 12)

print(JEVersion_MyGame)
```

---

### Typical Workflow

```python
# JarEngine version stored as JEVersion
# JEVersion_JarEngine = JEVersion(...)
# when JarEngine imported, startup banner uses the version

print(f"JarEngine {JEVersion_JarEngine} (PyGame {JEVersion_PyGame}, SDL {JEVersion_SDL}, Python {JEVersion_Python})")

```

---

## 🔹 Internal Behavior

JEVersion inherit directly from PyGame's SoftwareVersion class AND from JEInternBaseClass (which allows it to have PyGame version handling and JarEngine compatibility)

---

## 🔹 Current State

⚠️ Stable (and unlikely to be changed).

---

## 🔹 Debugging

Useful debugging methods:

* `dump()`
* `debug()`
* logs
* common errors

---

## 🔹 Related Classes

* [`•>...<•`]()📎
* [`•>...<•`]()📎
* [`•>...`]()

---
