---
layout: page
title: JarEngine - Component - Flip
sidebar: sidebar
permalink: /component_flip.html
---

# 📦 JEFlipComponent

> Technical reference for the `JEFlipComponent` component of JarEngine.

---

## 🔹 Overview

**`JEFlipComponent` stores the horizontal and vertical flip state of an entity.**

Provides:
* Flip state storage using `tuple[JEBool, JEBool]`.
* Access to the entity's X and Y axis flip values.
* Integration with graphical rendering transformations.

Used by entities requiring sprite or graphical object flipping.

---

## 🔹 Data

| Field  |          Type           | Description                     |
|:------:|:-----------------------:|---------------------------------|
| `flip` | `tuple[JEBool, JEBool]` | Flip state on the X and Y axis. |

---

## 🔹 Used by

### Entity
* `set_flip`
* `get_flip`

### System
* [`•>JERenderSystem<•`](class_jerendersystem.md)📎 

---