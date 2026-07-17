---
layout: page
title: JarEngine - Component - Texture
sidebar: sidebar
permalink: /component_texture.html
---

# 📦 Texture

> Technical reference for the `Texture` component of JarEngine.

---

## 🔹 Overview

**`Texture` stores the texture resource used to render an entity.**

Provides:
* A texture resource reference.
* Access and replacement of the entity texture.
* Graphical data required for textured rendering.

Used by graphical entities and rendering features where an entity requires a texture resource.

---

## 🔹 Data

|   Field   |    Type     | Description                             |
|:---------:|:-----------:|-----------------------------------------|
| `texture` | `JETexture` | Texture resource applied to the entity. |

---

## 🔹 Used by

### Entity
* `set_texture`
* `get_texture`

### System
* [`•>JERenderSystem<•`](class_jerendersystem.md)📎 

---