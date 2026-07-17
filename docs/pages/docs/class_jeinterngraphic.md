---
layout: page
title: JarEngine - Class - JEInternGraphic
sidebar: sidebar
permalink: /class_jeinterngraphic.html
---

# 📦 JEInternGraphic

> Technical reference for the `JEInternGraphic` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternGraphic` is responsible for providing the base structure of graphic-linked objects in JarEngine.**

Provides:
* Graphic object lifecycle management
* Object destruction handling
* Graphic state tracking

`JEInternGraphic` is the base internal class for objects linked to graphic processing. It is inherited by graphical objects and resources requiring managed lifetime behavior.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternGraphic
│
└── ...
```

---

## 🔹 Data

|   Field    |   Type   | Description                                 | Property? | Can be set? |
|:----------:|:--------:|---------------------------------------------|:---------:|:-----------:|
| `is_alive` | `JEBool` | Whether the graphical object is still alive |   True    |    False    |

---

## 🔹 API

|  Function  |  Arguments  | Returns | Description                           |
|:----------:|:-----------:|:-------:|---------------------------------------|
| `__init__` | `name: str` |         | Creates a graphic object              |
| `destroy`  |             |         | Marks the graphic object as destroyed |

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
