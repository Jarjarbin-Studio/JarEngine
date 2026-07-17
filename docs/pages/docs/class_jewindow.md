---
layout: page
title: JarEngine - Class - JEWindow
sidebar: sidebar
permalink: /class_jewindow.html
---

# 📦 JEWindow

> Technical reference for the `JEWindow` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEWindow` is responsible for managing the main PyGame application window and its rendering surface.**

Provides:
* Creation and configuration of the main PyGame display.
* Access to the active rendering surface.
* Basic window rendering operations such as filling and surface blitting.
* Centralized management of window settings.

`JEWindow` is the main interface between JarEngine applications and the underlying PyGame window system. It manages the display lifecycle and provides a simplified abstraction over PyGame's window handling.

Used as the primary rendering target for games and applications built with JarEngine.

---

## 🔹 Location

```text
JarEngine
│
├── Games
│     └── JEWindow
│
└── ...
```

---

## 🔹 Data

|   Field    |           Type           | Description                       | Property? | Can be set? |
|:----------:|:------------------------:|-----------------------------------|:---------:|:-----------:|
|  `screen`  |     `PyGame.Surface`     | Internal PyGame rendering surface |   True    |    False    |
| `settings` | `JEInternWindowSettings` | Window configuration settings     |   True    |    False    |

---

## 🔹 API

|  Function  |                                                                                Arguments                                                                                 | Returns | Description                                    |
|:----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------:|------------------------------------------------|
| `__init__` | `size: JEVector2D \| tuple[int, int] = JEVector2D(0, 0), flags: int = 0, fps: int = 60, depth: int = 0, display: int = 0, vsync: int = 0, title: str = "JarEngine Game"` |         | Initialize the PyGame window and its settings  |
|   `fill`   |                                                  `color: JEColor \| tuple[int, int, int] \| tuple[int, int, int, int]`                                                   |         | Fill the window rendering surface with a color |
|   `blit`   |                                                              `source: PyGame.Surface, dest: PyGame.Surface`                                                              |         | Copy a PyGame surface onto another surface     |

---

## 🔹 Usage

```python
from jarengine.games import JEWindow
from jarengine.systems import JEColor

# Create a game window
window = JEWindow(
    size=(1280, 720),
    fps=60,
    title="My JarEngine Game"
)

# Main game loop
while True:
    # Clear the window with a background color
    window.fill(JEColor(30, 30, 30))

    # Draw game elements here
    # window.blit(surface, position)

    # Update the display
    window.update()
```

---
