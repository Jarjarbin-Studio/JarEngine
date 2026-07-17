---
layout: page
title: JarEngine - JarEngine - Resources
sidebar: sidebar
permalink: /module_resources.html
---

# 📦 Resources

> Overview of the `Resources` module in JarEngine.

---

## 🔹 Overview

`Resources` provides the classes and utilities related to game resource storage and management.

It includes:
* Texture resources
* Font resources
* Music resources
* Sound resources

---

## 🔹 Contents

|                  Class                  | Description              |
|:---------------------------------------:|--------------------------|
| [`•>JETexture<•`](class_jetexture.md)📎 | Texture resource storage |
|    [`•>JEFont<•`](class_jefont.md)📎    | Font resource storage    |
|   [`•>JEMusic<•`](class_jemusic.md)📎   | Music resource storage   |
|   [`•>JESound<•`](class_jesound.md)📎   | Sound resource storage   |

---

## 🔹 Usage

```python
from jarengine import Resources

texture = Resources.JETexture(
    "player",
    "player.png"
)

font = Resources.JEFont(
    "default",
    "Nasalization.otf",
    20
)
```

The module provides resource objects that can be registered inside the game resource manager.

---

## 🔹 Notes

Useful information:

* Resource classes only store and describe resources.
* Resource loading and management is handled by the game resource system.
* Resources must be registered before being used by the game.

---
