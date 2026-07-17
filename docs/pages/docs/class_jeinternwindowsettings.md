---
layout: page
title: JarEngine - Class - JEInternWindowSettings
sidebar: sidebar
permalink: /class_jeinternwindowsettings.html
---

# 📦 JEInternWindowSettings

> Technical reference for the `JEInternWindowSettings` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternWindowSettings` is responsible for storing and managing internal window configuration settings.**

Provides:
* Window size management
* Rendering configuration storage
* Window title management

This class is used internally by JarEngine to store window initialization and runtime settings. It acts as a centralized configuration holder for the engine window system.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternWindowSettings
│
└── ...
```

---

## 🔹 Data

|   Field   |     Type     | Description                            | Property? | Can be set? |
|:---------:|:------------:|----------------------------------------|:---------:|:-----------:|
|  `size`   | `JEVector2D` | Window size configuration              |   True    |    True     |
|  `flags`  |    `int`     | Window creation flags                  |   True    |    False    |
|   `fps`   |    `int`     | Target window FPS                      |   True    |    True     |
|  `depth`  |    `int`     | Display depth configuration            |   True    |    False    |
| `display` |    `int`     | Display index configuration            |   True    |    False    |
|  `vsync`  |    `int`     | Vertical synchronization configuration |   True    |    False    |
|  `title`  |    `str`     | Window title                           |   True    |    True     |

---

## 🔹 API

|  Function  |                                         Arguments                                          | Returns | Description                |
|:----------:|:------------------------------------------------------------------------------------------:|:-------:|----------------------------|
| `__init__` | `size: JEVector2D, flags: int, fps: int, depth: int, display: int, vsync: int, title: str` |         | Initialize window settings |

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
