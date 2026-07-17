---
layout: page
title: JarEngine - Component - Rotation
sidebar: sidebar
permalink: /component_rotation.html
---

# 📦 Rotation

> Technical reference for the `Rotation` component of JarEngine.

---

## 🔹 Overview

**`Rotation` stores the rotation angle of an entity.**

Provides:
* Storage of the entity’s rotation value in degrees.
* Access and modification of the entity orientation.
* Rotation data required by graphical or transform-related features.

Used by entities requiring orientation information for rendering, transformations or other spatial operations.

---

## 🔹 Data

|   Field    |  Type   | Description                                      |
|:----------:|:-------:|--------------------------------------------------|
| `rotation` | `float` | Current rotation angle of the entity in degrees. |

---

## 🔹 Used by

### Entity
* `set_rotation`
* `update_rotation`
* `get_rotation`

### System
* [`•>JERenderSystem<•`](class_jerendersystem.md)📎 

---