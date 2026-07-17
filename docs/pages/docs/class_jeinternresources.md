---
layout: page
title: JarEngine - Class - JEInternResources
sidebar: sidebar
permalink: /class_jeinternresources.html
---

# 📦 JEInternResources

> Technical reference for the `JEInternResources` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternResources` is responsible for managing JarEngine resource storages.**

Provides:
* Centralized access to loaded textures, fonts, music, and sounds.
* Resource containers used internally by the engine.
* A unified resource management interface.

Used by internal engine systems to store and retrieve loaded resources.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternResources
│
└── ...
```

---

## 🔹 Data

|    Field     |              Type              | Description                                  | Property? | Can be set? |
|:------------:|:------------------------------:|----------------------------------------------|:---------:|:-----------:|
|  `texture`   |    `JEContainer[JETexture]`    | Texture resource storage                     |   True    |    False    |
| `animations` | `JEContainer[JEInternGraphic]` | Animation resource storage (not implemented) |   True    |    False    |
|    `font`    |     `JEContainer[JEFont]`      | Font resource storage                        |   True    |    False    |
|   `music`    |     `JEContainer[JEMusic]`     | Music resource storage                       |   True    |    False    |
|   `sound`    |     `JEContainer[JESound]`     | Sound resource storage                       |   True    |    False    |

---

## 🔹 API

|  Function  | Arguments | Returns | Description                     |
|:----------:|:---------:|:-------:|---------------------------------|
| `__init__` |           |         | Initialize the resource manager |

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
