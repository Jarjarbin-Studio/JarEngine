---
layout: page
title: JarEngine - Component - Visibility
sidebar: sidebar
permalink: /component_visibility.html
---

# 📦 Visibility

> Technical reference for the `Visibility` component of JarEngine.

---

## 🔹 Overview

**`Visibility` stores the visibility state of an entity.**

Provides:
* Visibility state storage using `JEBool`.
* Control over whether an entity is displayed.
* Integration with rendering systems.

Used by entities requiring dynamic visibility control.

---

## 🔹 Data

|    Field     |   Type   | Description                             |
|:------------:|:--------:|-----------------------------------------|
| `visibility` | `JEBool` | Current visibility state of the entity. |

---

## 🔹 Used by

### Entity
* `set_visibility`
* `get_visibility`

### System
* [`•>JERenderSystem<•`](class_jerendersystem.md)📎 

---