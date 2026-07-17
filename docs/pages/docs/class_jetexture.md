---
layout: page
title: JarEngine - Class - JETexture
sidebar: sidebar
permalink: /class_jetexture.html
---

# 📦 JETexture

> Technical reference for the `JETexture` class of JarEngine.

> Inherit from [`•>JEInternResource<•`]()📎 and [`•>JEInternOwnership<•`]()📎

---

## 🔹 Overview

**`JETexture` is responsible for storing and managing texture resources.**

Provides:
* Texture resource storage
* Texture access through PyGame surfaces
* Texture size retrieval

`JETexture` is used by the resource system to store graphical textures that can later be used by entities and rendering systems.

---

## 🔹 Location

```text
JarEngine
│
├── Resources
│     └── JETexture
│
└── ...
```

---

## 🔹 Data

|   Field   |       Type       | Description                    | Property? | Can be set? |
|:---------:|:----------------:|--------------------------------|:---------:|:-----------:|
| `texture` | `PyGame.Surface` | Internal PyGame texture object |   True    |    False    |
|  `size`   |   `JEVector2D`   | Texture dimensions             |   True    |    False    |

---

## 🔹 API

|  Function  |       Arguments        |     Returns      | Description                                 |
|:----------:|:----------------------:|:----------------:|---------------------------------------------|
| `__init__` | `name: str, path: str` |                  | Creates a texture resource from a file path |

---

## 🔹 Usage

```python
from jarengine import Resources

# Create a texture resource
# Automatic search of the texture in the "assets/textures/" folder (determined by the config)
player_texture = Resources.JETexture(
    "player",
    "player.png"
)

# Access texture information
print(player_texture.texture)
print(player_texture.size)
```

---
