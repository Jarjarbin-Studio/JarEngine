---
layout: page
title: JarEngine - Component - Position
sidebar: sidebar
permalink: /component_position.html
---

# 📦 Position

> Technical reference for the `Position` component of JarEngine.

---

## 🔹 Overview

**`Position` stores the 2D world position of an entity.**

Provides:
* Storage of the entity's X and Y coordinates.
* Access and modification of the current entity position.
* Spatial information required for movement and rendering.

Used by entities requiring a location in the game world and systems that process entity placement.

---

## 🔹 Data

|   Field    |     Type     | Description                           |
|:----------:|:------------:|---------------------------------------|
| `position` | `JEVector2D` | Current 2D coordinates of the entity. |

---

## 🔹 Used by

### Entity
* `set_position`
* `update_position`
* `get_position`

### System
* [`•>JEMovementSystem<•`](class_jemovementsystem.md)📎
* [`•>JEPositionComponent<•`](class_jerendersystem.md)📎

---