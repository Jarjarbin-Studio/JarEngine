---
layout: page
title: JarEngine - Class - JEInternSystems
sidebar: sidebar
permalink: /class_jeinternsystems.html
---

# 📦 JEInternSystems

> Technical reference for the `JEInternSystems` class of JarEngine.

> Inherit from [`•>JEInternOwnership<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternSystems` is responsible for providing the internal base architecture of JarEngine entity systems.**

Provides:
* Entity cache management
* Component requirement checking
* System update structure

This class is used internally by JarEngine systems to manage entities matching specific component requirements. It handles system ownership, entity caching, and optimized entity updates.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternSystems
│
└── ...
```

---

## 🔹 Data

|  Field  |       Type       | Description                                        | Property? | Can be set? |
|:-------:|:----------------:|----------------------------------------------------|:---------:|:-----------:|
| `cache` | `list[JEEntity]` | Cached entities used for faster system computation |   False   |    True     |

---

## 🔹 API

|     Function     |                                    Arguments                                     | Returns  | Description                                         |
|:----------------:|:--------------------------------------------------------------------------------:|:--------:|-----------------------------------------------------|
|    `__init__`    |                                 `owner: JEGame`                                  |          | Initialize the internal system with its owner game  |
|    `refresh`     |                                                                                  |          | Refresh the entity cache (high CPU cost)            |
| `refresh_entity` |                                `entity: JEEntity`                                |          | Refresh the entity cache with a single entity       |
|   `sort_cache`   |                                                                                  |          | Sort the entity cache                               |
|    `accepts`     |                `components: JEContainer[JEInternEntityComponent]`                | `JEBool` | Check whether an entity has the required components |
|     `update`     | `window: JEWindow, entity: JEEntity, entities: JEContainer[JEEntity], dt: float` |          | Update the system for an entity                     |

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
