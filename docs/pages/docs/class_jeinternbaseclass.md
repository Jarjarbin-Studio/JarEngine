---
layout: page
title: JarEngine - Class - JEInternBaseClass
sidebar: sidebar
permalink: /class_jeinternbaseclass.html
---

# 📦 JEInternBaseClass

> Technical reference for the `JEInternBaseClass` class of JarEngine.

> Inherit from `object`

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternBaseClass` is the foundational class of JarEngine's internal object architecture.**

Provides:
* A unified base implementation for every internal JarEngine class.
* Automatic instance identification through JEID management.
* Common serialization, representation, debugging, and introspection features.
* Support for advanced object behavior systems such as instance policies and recursive object inspection.

`JEInternBaseClass` is the core abstraction layer used by JarEngine classes. Every engine-level object inheriting from this class gains a standardized structure, allowing the framework to identify, debug, serialize, and inspect objects consistently.

It acts as the "root object" of JarEngine's custom class system and is required for most internal engine features.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternBaseClass
│
└── ...
```

---

## 🔹 Data

|         Field         |      Type       | Description                                                                                  | Property? | Can be set? |
|:---------------------:|:---------------:|----------------------------------------------------------------------------------------------|:---------:|:-----------:|
| `__instance_policy__` |      `str`      | Defines how instances are handled (`normal`, `flyweight`, `singleton`)                       |   False   |    True     |
| `__instance_limit__`  | `Optional[int]` | Maximum allowed number of instances (`None` for unlimited)                                   |   False   |    True     |
|    `__recursive__`    |     `bool`      | Defines whether the object can recursively reference itself during debug and dump operations |   False   |    True     |
|        `jeid`         |      `str`      | Unique JarEngine identifier assigned to the object                                           |   True    |    False    |

---

## 🔹 API

|  Function  |                                                 Arguments                                                 | Returns | Description                                                             |
|:----------:|:---------------------------------------------------------------------------------------------------------:|:-------:|-------------------------------------------------------------------------|
| `__init__` |                                                                                                           |         | Initialize the internal JarEngine object                                |
| `__str__`  |                                                                                                           |  `str`  | Get the human-readable string representation of the object              |
| `__repr__` |                                                                                                           |  `str`  | Get the developer representation of the object                          |
| `to_dict`  |                                                                                                           | `dict`  | Convert the object and its public data into a dictionary representation |
|  `debug`   | `is_colored: bool = False, max_depth: int = -1, branched_recursive: bool = False, show_root: bool = True` |  `str`  | Generate a detailed recursive debug representation of the object        |
|   `dump`   |                                                                                                           |  `str`  | Generate a simplified debug representation of the object                |

---
