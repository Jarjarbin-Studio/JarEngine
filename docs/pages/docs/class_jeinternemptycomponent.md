---
layout: page
title: JarEngine - Class - JEInternEmptyComponent
sidebar: sidebar
permalink: /class_jeinternemptycomponent.html
---

# 📦 JEInternEmptyComponent

> Technical reference for the `JEInternEmptyComponent` class of JarEngine.

> Inherit from [`•>JEInternEntityComponent<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternEmptyComponent` is responsible for representing an empty component used for entity checking.**

Provides:
* A placeholder component for entities without additional components.
* Compatibility with the entity component system.
* A default false-like behavior for component filtering.

Used internally by the entity system when an entity requires a component container entry without storing additional data.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternEmptyComponent
│
└── ...
```

---

## 🔹 Data

No public data nor property

---

## 🔹 API

|  Function  |       Arguments       |         Returns          | Description                                  |
|:----------:|:---------------------:|:------------------------:|----------------------------------------------|
| `__init__` |   `owner: JEEntity`   |                          | Initialize the empty component               |
| `__call__` |                       |        `NoneType`        | Return no component data for entity checking |
| `__bool__` |                       |          `bool`          | Return false for entity checking             |
|   `copy`   | `new_owner: JEEntity` | `JEInternEmptyComponent` | Copy the empty component to another entity   |

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
