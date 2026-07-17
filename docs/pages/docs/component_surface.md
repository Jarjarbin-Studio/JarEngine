---
layout: page
title: JarEngine - Component - Surface
sidebar: sidebar
permalink: /component_surface.html
---

# 📦 Surface

> Technical reference for the `Surface` component of JarEngine.

---

## 🔹 Overview

**`JESurfaceComponent` stores a pygame `Surface` linked to an entity.**

Provides:
* A direct way to render custom pygame surfaces.
* Support for custom primitives, generated graphics, and dynamic drawings.
* A base component for advanced graphical entities such as widgets and UI elements.

Used by graphical entities requiring custom rendering through `JERenderSystem`.

---

## 🔹 Data

|   Field   |        Type        | Description                            |
|:---------:|:------------------:|----------------------------------------|
| `surface` | `PGExtern.Surface` | Pygame surface attached to the entity. |

---

## 🔹 Used by

### Entity
* `set_surface`
* `get_surface`

### System
* [`•>JERenderSystem<•`](class_jerendersystem.md)📎 

---
