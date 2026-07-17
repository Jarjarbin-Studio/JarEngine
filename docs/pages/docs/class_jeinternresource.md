---
layout: page
title: JarEngine - Class - JEInternResource
sidebar: sidebar
permalink: /class_jeinternresource.html
---

# 📦 JEInternResource

> Technical reference for the `JEInternResource` class of JarEngine.

> Inherit from [`•>JEInternGraphic<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternResource` is responsible for providing the base structure of JarEngine resources.**

Provides:
* Resource path storage
* Resource naming through inheritance
* Base resource management behavior

`JEInternResource` is the base class used by resource classes such as textures, sounds, music and fonts. It handles the common data shared by all resources.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternResource
│
└── ...
```

---

## 🔹 Data

| Field  | Type  | Description        | Property? | Can be set? |
|:------:|:-----:|--------------------|:---------:|:-----------:|
| `path` | `str` | Resource file path |   True    |    False    |

---

## 🔹 API

|  Function  |       Arguments        | Returns | Description                    |
|:----------:|:----------------------:|:-------:|--------------------------------|
| `__init__` | `name: str, path: str` |         | Creates a resource base object |

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
