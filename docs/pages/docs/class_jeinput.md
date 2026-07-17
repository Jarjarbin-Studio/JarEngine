---
layout: page
title: JarEngine - Class - JEInput
sidebar: sidebar
permalink: /class_jeinput.html
---

# 📦 JEInput

> Technical reference for the `JEInput` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEInput` is responsible for handling keyboard and mouse inputs inside JarEngine.**

Provides:
* Keyboard state checking.
* Mouse button state checking.
* Mouse position retrieval.
* Unified input checking through callable interface.

Central input management class used to retrieve real-time user interactions. It acts as an abstraction layer over PyGame input handling, allowing JarEngine systems and games to query inputs without directly interacting with PyGame events.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEInput
│
└── ...
```

---

## 🔹 Data

No public data nor property

---

## 🔹 API

|    Function     |            Arguments             |   Returns    | Description                                                                     |
|:---------------:|:--------------------------------:|:------------:|---------------------------------------------------------------------------------|
|    `update`     |                                  |              | Updates keyboard and mouse input states.                                        |
|  `is_key_down`  |         `key: JEKeyCode`         |    `bool`    | Checks whether a keyboard key is currently pressed.                             |
| `is_mouse_down` |      `button: JEMouseCode`       |    `bool`    | Checks whether a mouse button is currently pressed.                             |
|   `mouse_pos`   |                                  | `JEVector2D` | Gets the current mouse position.                                                |
|   `__call__`    | `code: JEKeyCode \| JEMouseCode` |    `bool`    | Automatically checks whether the given keyboard key or mouse button is pressed. |

---

## 🔹 Usage

```python
from jarengine import Games
from jarengine import JEKey_Space, JEMse_Left

input_manager = Games.JEInput()

input_manager.update()

if input_manager(JEKey_Space):
    print("Space key pressed")

if input_manager.is_mouse_down(JEMse_Left):
    print("Left mouse button pressed")

mouse_position = input_manager.mouse_pos()
print(f"Mouse position: {mouse_position}")
```

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
