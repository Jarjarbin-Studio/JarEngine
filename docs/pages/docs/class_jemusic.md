---
layout: page
title: JarEngine - Class - JEMusic
sidebar: sidebar
permalink: /class_jemusic.html
---

# 📦 JEMusic

> Technical reference for the `JEMusic` class of JarEngine.

> Inherit from [`•>JEInternResource<•`]()📎 and [`•>JEInternOwnership<•`]()📎

---

## 🔹 Overview

**`JEMusic` is responsible for storing and managing music resources.**

Provides:
* Music resource storage
* Resource integration with JarEngine
* Audio file management

`JEMusic` is used by the resource system to store background music and long audio tracks used by games.

---

## 🔹 Location

```text
JarEngine
│
├── Resources
│     └── JEMusic
│
└── ...
```

---

## 🔹 Data

No public data nor property.

---

## 🔹 API

|  Function  |       Arguments        | Returns | Description                               |
|:----------:|:----------------------:|:-------:|-------------------------------------------|
| `__init__` | `name: str, path: str` |         | Creates a music resource from a file path |

---

## 🔹 Usage

```python
from jarengine import Resources

# Create a music resource
# Automatic search of the music in the "assets/musics/" folder (determined by the config)
background_music = Resources.JEMusic(
    "background",
    "background.ogg"
)
```

---
