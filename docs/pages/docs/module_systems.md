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

| Class                   | Description              |
|-------------------------|--------------------------|
| [`•>JEBool<•`]()📎      | Custom boolean wrapper   |
| [`•>JEClock<•`]()📎     | Controlled FPS clock     |
| [`•>JEColor<•`]()📎     | RGBA color management    |
| [`•>JEContainer<•`]()📎 | Custom data container    |
| [`•>JEImmutable<•`]()📎 | Immutable data storage   |
| [`•>JEVector2D<•`]()📎  | 2D vector representation |
| [`•>JEVector3D<•`]()📎  | 3D vector representation |
| [`•>JEVersion<•`]()📎   | Version storage          |

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
````

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
