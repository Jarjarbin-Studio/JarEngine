---
layout: page
title: JarEngine - Component - Layer
sidebar: sidebar
permalink: /component_layer.html
---

# 📦 Layer

> Technical reference for the `Layer` component of JarEngine.

---

## 🔹 Overview

**`Layer` stores the rendering order placement of an entity.**

Provides:
* Layer index storage.
* Rendering order management.
* Layer modification through entity helpers.

Used by entities requiring a configurable rendering priority.

---

## 🔹 Data

|  Field  | Type  | Description                          |
|:-------:|:-----:|--------------------------------------|
| `layer` | `int` | Rendering layer index of the entity. |

---

## 🔹 Used by

### Entity
* `set_layer`
* `update_layer`
* `get_layer`

### System
* No system currently requires this component.

---