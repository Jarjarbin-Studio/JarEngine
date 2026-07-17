---
layout: page
title: JarEngine - Class - JEFont
sidebar: sidebar
permalink: /class_jefont.html
---

# 📦 JEFont

> Technical reference for the `JEFont` class of JarEngine.

> Inherit from [`•>JEInternResource<•`]()📎 and [`•>JEInternOwnership<•`]()📎

---

## 🔹 Overview

**`JEFont` is responsible for storing and managing font resources.**

Provides:
* Font resource storage
* PyGame font access
* Font size management

`JEFont` is used by the resource system to store fonts used for text rendering inside JarEngine games.

---

## 🔹 Location

```text
JarEngine
│
├── Resources
│     └── JEFont
│
└── ...
```

---

## 🔹 Data

| Field  |        Type        | Description                 | Property? | Can be set? |
|:------:|:------------------:|-----------------------------|:---------:|:-----------:|
| `font` | `PyGame.font.Font` | Internal PyGame font object |   True    |    False    |
| `size` |       `int`        | Font size                   |   True    |    False    |

---

## 🔹 API

|  Function  |             Arguments             |      Returns       | Description                              |
|:----------:|:---------------------------------:|:------------------:|------------------------------------------|
| `__init__` | `name: str, path: str, size: int` |                    | Creates a font resource from a file path |

---

## 🔹 Usage

```python
from jarengine import Resources

# Create a font resource
# Automatic search of the font in the "assets/fonts/" folder (determined by the config)
main_font = Resources.JEFont(
    "main_font",
    "font.otf",
    24
)

# Access font information
print(main_font.font)
print(main_font.size)
```

---
