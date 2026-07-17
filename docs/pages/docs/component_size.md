---
layout: page
title: JarEngine - Component - Size
sidebar: sidebar
permalink: /component_size.html
---

# 📦 Size

> Technical reference for the `Size` component of JarEngine.

---

## 🔹 Overview

**`Size` stores the 2D dimensions of an entity.**

Provides:
* Storage of the entity width and height values.
* Access and modification of entity dimensions.
* Size information required by rendering, collision, or transform-related features.

Used by entities requiring size information for graphical representation, spatial calculations, or other systems that depend on entity dimensions.

---

## 🔹 Data

| Field  |     Type     | Description                                    |
|:------:|:------------:|------------------------------------------------|
| `size` | `JEVector2D` | Current width and height values of the entity. |

---

## 🔹 Used by

### Entity
* `set_size`
* `update_size`
* `get_size`

### System
* No system currently requires this component.

---