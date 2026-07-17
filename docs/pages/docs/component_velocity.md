---
layout: page
title: JarEngine - Component - Velocity
sidebar: sidebar
permalink: /component_velocity.html
---

# 📦 Velocity

> Technical reference for the `Velocity` component of JarEngine.

---

## 🔹 Overview

**`Velocity` stores the current movement speed and direction of an entity.**

Provides:
* Storage of the entity's 2D velocity vector.
* Access and modification of movement speed values.
* Data required to update entity positions over time.

Used by entities requiring movement behavior and systems that process motion and physics calculations.

---

## 🔹 Data

|   Field    |     Type     | Description                               |
|:----------:|:------------:|-------------------------------------------|
| `velocity` | `JEVector2D` | Current 2D velocity vector of the entity. |

---

## 🔹 Used by

### Entity
* `set_velocity`
* `update_velocity`
* `get_velocity`

### System
* No system currently requires this component.

---