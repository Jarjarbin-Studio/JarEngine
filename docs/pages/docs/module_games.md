---
layout: page
title: JarEngine - Games
sidebar: sidebar
permalink: /module_games.html
---

# 📦 Games

> Overview of the `Games` module in JarEngine.

---

## 🔹 Overview

**`Games` is a JarEngine module responsible for game and user interaction handling and managing.**

It provides:

* Game
* Input
* Systems
* Window

---

## 🔹 Structure

```text
jarengine/
└── <module>/
    ├── __init__.py
    ├── game.py
    ├── input.py
    ├── systems.py
    └── window.py
```

| File          | Description                  |
|---------------|------------------------------|
| `__init__.py` | Public module exports.       |
| `game.py`     | Game handler (highest class) |
| `input.py`    | User input handler           |
| `systems.py`  | Systems for the ECS          |
| `window.py`   | Window handling              |

---

## 🔹 Main Classes

| Class                  | Description                                          |
|------------------------|------------------------------------------------------|
| `JEGame`               | Game handle, main starting point                     |
| `JEInput`              | User input handler (not linked to events in any way) |
| `JEMovementSystem`     | ECS system for movement update                       |
| `JEAccelerationSystem` | ECS system for acceleration update                   |
| `JERenderSystem`       | ECS system for rendering update                      |
| `JEWindow`             | Window handler                                       |

Each class has its own documentation page.

---

## 🔹 Usage

### Basic Example

```python
from jarengine.Games import JEGame, JEWindow

# Create the game
game = JEGame(use_clock=True, use_input=True)

# Create and attach a window
window = JEWindow(
    size=(1280, 720),
    title="My First Game",
    fps=60,
)

game.set_window(window)
```

### Typical Workflow

```python
from jarengine import Games

# Create the game
game = Games.JEGame(use_clock=True, use_input=True)

# Create the main window
window = Games.JEWindow(
    size=(1280, 720),
    title="JarEngine Demo",
    fps=60,
)

game.set_window(window)

# Register engine systems
Games.Systems.JEMovementSystem(game)
Games.Systems.JERenderSystem(game)

# Build system caches
game.refresh()

# Main game loop
while game.is_open:
    window.fill(JEColor(30, 30, 30))

    game.update()
    # Rendering is performed by the render system during the update

    game.display()
```

---

## 🔹 Important Notes

Things to know when using this module:

* This is the main entry point, game is the handler/manager for the input, event, entity, and many more classes
* You can create only 1 window, input, game.

Common mistakes:

* Game itself isn't the window, you have to link a JEWindow instance to the game
* ...

---

## 🔹 Dependencies

Uses:

* `pygame`
* `jarbin-toolkit-error`
* [`JEEventHandler`]()📎
* [`JEInternBaseClass`]()📎
* [`JEInternConfig`]()📎
* [`JEEntity`]()📎
* [`JEContainer`]()📎
* [`JEInternSystems`]()📎
* [`JEInternResources`]()📎
* [`JEBool`]()📎
* [`JEColor`]()📎
* [`JEInternWindowSettings`]()📎
* [`JEKeyCode`]()📎
* [`JEMouseCode`]()📎
* [`JEVector2D`]()📎
* [`JEFontComponent`]()📎
* [`JETextComponent`]()📎
* [`JEFlipComponent`]()📎
* [`JELayerComponent`]()📎
* [`JEVisibilityComponent`]()📎
* [`JETextureComponent`]()📎
* [`JEColorComponent`]()📎
* [`JEOutlineComponent`]()📎
* [`JEPositionComponent`]()📎
* [`JERotationComponent`]()📎
* [`JEVelocityComponent`]()📎
* [`JESizeComponent`]()📎
* [`JEMassComponent`]()📎
* [`JEAccelerationComponent`]()📎
* [`JEGroupComponent`]()📎
* [`JEMusicComponent`]()📎
* [`JESoundComponent`]()📎

---

## 🔹 Related Modules

* [`...`]()
* [`...`]()
* [`...`]()

---
