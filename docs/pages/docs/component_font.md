---
layout: page
title: JarEngine - Component - Font
sidebar: sidebar
permalink: /component_font.html
---

# 📦 JEFontComponent

> Technical reference for the `JEFontComponent` component of JarEngine.

---

## 🔹 Overview

**`JEFontComponent` stores the font resource attached to an entity.**

Provides:
* Font resource storage using `JEFont`.
* Font access for text rendering components.
* Integration with entity graphical features.

Used by entities requiring font data for text rendering.

---

## 🔹 Data

| Field  |   Type   | Description                           |
|:------:|:--------:|---------------------------------------|
| `font` | `JEFont` | Font resource attached to the entity. |

---

## 🔹 Used by

### Entity
* `set_font`
* `get_font`

### System
* No system currently requires this component.

---