---
layout: page
title: JarEngine - Class - JEInternGraphicalObject
sidebar: sidebar
permalink: /class_jeinterngraphicalobject.html
---

# 📦 JEInternGraphicalObject

> Technical reference for the `JEInternGraphicalObject` class of JarEngine.

> Inherit from [`•>JEInternGraphic<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternGraphicalObject` is responsible for providing the base structure of graphical objects managed by JarEngine.**

Provides:
* Graphical object update handling
* Dirty state management
* Graphical lifecycle support

`JEInternGraphicalObject` is used internally by graphical entities and systems to track objects requiring updates or rendering refreshes.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternGraphicalObject
│
└── ...
```

---

## 🔹 Data

|   Field    |   Type   | Description                                                | Property? | Can be set? |
|:----------:|:--------:|------------------------------------------------------------|:---------:|:-----------:|
| `is_dirty` | `JEBool` | Whether the graphical object requires an update or refresh |   True    |    False    |

---

## 🔹 API

|   Function    |  Arguments  | Returns | Description                                   |
|:-------------:|:-----------:|:-------:|-----------------------------------------------|
|  `__init__`   | `name: str` |         | Creates a graphical object                    |
|   `update`    | `dt: float` |         | Updates the graphical object state            |
| `mark_dirty`  |             |         | Marks the graphical object as needing refresh |
| `clear_dirty` |             |         | Clears the dirty state                        |

---
