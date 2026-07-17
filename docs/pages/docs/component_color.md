---
layout: page
title: JarEngine - Component - Color
sidebar: sidebar
permalink: /component_color.html
---

# 📦 Color

> Technical reference for the `Color` component of JarEngine.

---

## 🔹 Overview

**`Color` stores the rendering color properties of an entity.**

Provides:
* An RGB or RGBA color value.
* Access and modification of the entity's visual color.
* Color data required by rendering systems.

Used by graphical entities and rendering features where color customization is required.

---

## 🔹 Data

|  Field  |   Type    | Description                                    |
|:-------:|:---------:|------------------------------------------------|
| `color` | `JEColor` | Entity color value using RGB or RGBA channels. |

---

## 🔹 Used by

### Entity
* `set_color`
* `update_color`
* `get_color`

### System
* [`•>JERenderSystem<•`](class_jerendersystem.md)📎 

---