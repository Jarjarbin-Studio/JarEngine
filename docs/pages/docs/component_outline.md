---
layout: page
title: JarEngine - Component - Outline
sidebar: sidebar
permalink: /component_outline.html
---

# 📦 Outline

> Technical reference for the `Outline` component of JarEngine.

---

## 🔹 Overview

**`Outline` stores the outline rendering properties of an entity.**

Provides:
* An outline color configuration.
* An outline size configuration.
* Access and modification of outline visual parameters.

Used by graphical entities and rendering features requiring outlined text or shapes.

---

## 🔹 Data

|  Field  |   Type    | Description                                |
|:-------:|:---------:|--------------------------------------------|
| `color` | `JEColor` | Color of the entity outline (RGB or RGBA). |
| `size`  |   `int`   | Thickness of the entity outline.           |

---

## 🔹 Used by

### Entity
* `set_outline_color`
* `update_outline_color`
* `get_outline_color`
* `set_outline_size`
* `update_outline_size`
* `get_outline_size`

### System
* [`•>JERenderSystem<•`](class_jerendersystem.md)📎 

---