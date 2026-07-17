---
layout: page
title: JarEngine - Component - Text
sidebar: sidebar
permalink: /component_text.html
---

# 📦 Text

> Technical reference for the `Text` component of JarEngine.

---

## 🔹 Overview

**`Text` stores the text content displayed by an entity.**

Provides:
* A string value representing the entity text.
* Access and modification of displayed text data.
* Text information required for text rendering.

Used by text-based graphical entities and rendering features where an entity displays a text string.

---

## 🔹 Data

| Field  | Type  | Description                           |
|:------:|:-----:|---------------------------------------|
| `text` | `str` | Text content displayed by the entity. |

---

## 🔹 Used by

### Entity
* `set_text`
* `get_text`

### System
* [`•>JERenderSystem<•`](class_jerendersystem.md)📎 

---