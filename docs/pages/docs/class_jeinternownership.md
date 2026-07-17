---
layout: page
title: JarEngine - Class - JEInternOwnership
sidebar: sidebar
permalink: /class_jeinternownership.html
---

# 📦 JEInternOwnership

> Technical reference for the `JEInternOwnership` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternOwnership` is responsible for managing parent and child relationships between JarEngine internal objects.**

Provides:
* Parent object storage
* Child object storage
* Ownership relationship management

This class is used internally by JarEngine classes that require hierarchical relationships, such as entities, components, and engine resources.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternOwnership
│
└── ...
```

---

## 🔹 Data

|   Field    |               Type               | Description                         | Property? | Can be set? |
|:----------:|:--------------------------------:|-------------------------------------|:---------:|:-----------:|
| `parents`  | `JEContainer[JEInternBaseClass]` | Container containing parent objects |   True    |    False    |
| `children` | `JEContainer[JEInternBaseClass]` | Container containing child objects  |   True    |    False    |

---

## 🔹 API

|   Function   |          Arguments          | Returns | Description                     |
|:------------:|:---------------------------:|:-------:|---------------------------------|
|  `__init__`  |                             |         | Initialize the ownership system |
| `add_parent` | `parent: JEInternBaseClass` |         | Add a parent object             |
| `add_child`  | `child: JEInternBaseClass`  |         | Add a child object              |

---
