---
layout: page
title: JarEngine - Class - JESound
sidebar: sidebar
permalink: /class_jesound.html
---

# 📦 JESound

> Technical reference for the `JESound` class of JarEngine.

> Inherit from [`•>JEInternResource<•`]()📎 and [`•>JEInternOwnership<•`]()📎

---

## 🔹 Overview

**`JESound` is responsible for storing and managing sound resources.**

Provides:
* Sound resource storage
* PyGame sound access
* Resource integration with JarEngine

`JESound` is used by the resource system to store audio effects that can later be played by game systems.

---

## 🔹 Location

```text
JarEngine
│
├── Resources
│     └── JESound
│
└── ...
```

---

## 🔹 Data

|  Field  |         Type         | Description                  | Property? | Can be set? |
|:-------:|:--------------------:|------------------------------|:---------:|:-----------:|
| `sound` | `PyGame.mixer.Sound` | Internal PyGame sound object |   True    |    False    |

---

## 🔹 API

|  Function  |       Arguments        |       Returns        | Description                               |
|:----------:|:----------------------:|:--------------------:|-------------------------------------------|
| `__init__` | `name: str, path: str` |                      | Creates a sound resource from a file path |

---

## 🔹 Usage

```python
from jarengine import Resources

# Create a sound resource
# Automatic search of the sound in the "assets/sounds/" folder (determined by the config)
jump_sound = Resources.JESound(
    "jump",
    "jump.wav"
)

# Access the PyGame sound object
print(jump_sound.sound)
```

---
