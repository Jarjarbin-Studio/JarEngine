---
layout: page
title: JarEngine - Component - Acceleration
sidebar: sidebar
permalink: /component_acceleration.html
---

# 📦 Acceleration

> Technical reference for the `Acceleration` component of JarEngine.

---

## 🔹 Overview

**`Acceleration` stores the acceleration vector applied to an entity.**

Provides:
* Storage of the entity acceleration value.
* Access and modification of the acceleration vector.
* Integration with physics-based movement calculations.

Used by entities requiring acceleration-based physics behavior and the `JEAccelerationSystem`.

---

## 🔹 Data

|     Field      |     Type     | Description                                        |
|:--------------:|:------------:|----------------------------------------------------|
| `acceleration` | `JEVector2D` | Current acceleration vector applied to the entity. |

---

## 🔹 Used by

### Entity
* `set_acceleration(acceleration: JEVector2D \| tuple[float, float])`
* `update_acceleration(x: float, y: float)`
* `get_acceleration() -> JEVector2D`

### System
* [`•>JEAccelerationSystem<•`](class_jeaccelerationsystem.md)📎

---