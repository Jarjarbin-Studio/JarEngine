---
layout: page
title: JarEngine - Class - JEInternEntityComponent
sidebar: sidebar
permalink: /class_jeinternentitycomponent.html
---

# 📦 JEInternEntityComponent

> Technical reference for the `JEInternEntityComponent` class of JarEngine.

> Inherit from `JEInternGraphic` and [`•>JEInternOwnership<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternEntityComponent` is responsible for providing the internal base structure of JarEngine entity components.**

Provides:
* Component ownership management
* Internal component value access
* Entity-component relationship handling

This class is used internally by JarEngine's ECS architecture to connect components with their owning entities. It should only be extended when creating custom engine-level components.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternEntityComponent
│
└── ...
```

---

## 🔹 Data

No public data nor property

---

## 🔹 API

|  Function  |           Arguments            |          Returns          | Description                                                                |
|:----------:|:------------------------------:|:-------------------------:|----------------------------------------------------------------------------|
| `__init__` | `owner: JEEntity, _type: type` |                           | Initialize the internal component with its owner entity and component type |
| `__call__` |                                |           `Any`           | Get the internal value(s) of the component                                 |
|   `copy`   |                                | `JEInternEntityComponent` | Copy the component recursively                                             |

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
