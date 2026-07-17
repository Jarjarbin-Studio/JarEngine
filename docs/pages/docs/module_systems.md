---
layout: page
title: JarEngine - Module - Systems
sidebar: sidebar
permalink: /module_systems.html
---

# 📦 Systems

> Overview of the `Systems` module in JarEngine.

---

## 🔹 Overview

`Systems` provides the classes and utilities related to common engine data structures and helpers.

It includes:
* Vector and transform utilities
* Color handling
* Custom containers
* Immutable data storage

---

## 🔹 Contents

|                    Class                    | Description              |
|:-------------------------------------------:|--------------------------|
|      [`•>JEBool<•`](class_jebool.md)📎      | Custom boolean wrapper   |
|     [`•>JEClock<•`](class_jeclock.md)📎     | Controlled FPS clock     |
|     [`•>JEColor<•`](class_jecolor.md)📎     | RGBA color management    |
| [`•>JEContainer<•`](class_jecontainer.md)📎 | Custom data container    |
| [`•>JEImmutable<•`](class_jeimmutable.md)📎 | Immutable data storage   |
|  [`•>JEVector2D<•`](class_jevector2d.md)📎  | 2D vector representation |
|  [`•>JEVector3D<•`](class_jevector3d.md)📎  | 3D vector representation |
|   [`•>JEVersion<•`](class_jeversion.md)📎   | Version storage          |

---

## 🔹 Usage

```python
from jarengine import Systems

position = Systems.JEVector2D(100, 50)

position.x += 10
position.y += 20

color = Systems.JEColor(255, 120, 50, 255)

print(position)
print(color)
```

The module provides reusable low-level objects used by JarEngine systems, components and games.

---

## 🔹 Notes

Useful information:

* Systems are core utilities used throughout JarEngine.
* Some classes are designed to be extended by engine components.
* Use immutable and container classes carefully with custom objects.

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
