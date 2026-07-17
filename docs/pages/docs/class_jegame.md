---
layout: page
title: JarEngine - Class - JEGame
sidebar: sidebar
permalink: /class_jegame.html
---

# 📦 JEGame

> Technical reference for the `JEGame` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEGame` is responsible for managing the main game runtime environment of JarEngine.**

Provides:
* Game lifecycle management.
* Window, input, event, resource, entity, and system handling.
* Central update and rendering loop management.

Main class used to create and control a JarEngine game instance. It acts as the central coordinator between game systems, entities, resources, events, input handling, and display management.

---

## 🔹 Location

```text
JarEngine
│
├── games
│     └── JEGame
│
└── ...
```

---

## 🔹 Data

|    Field    |              Type              | Description                                      | Property? | Can be set? |
|:-----------:|:------------------------------:|--------------------------------------------------|:---------:|:-----------:|
|    `wdw`    |           `JEWindow`           | Current game window                              |   True    |    False    |
|   `input`   |           `JEInput`            | Input handler (only available when enabled)      |   True    |    False    |
|   `clock`   |           `JEClock`            | Game clock handler (only available when enabled) |   True    |    False    |
|    `dt`     |            `float`             | Delta time between frames                        |   True    |    False    |
|   `event`   |        `JEEventHandler`        | Event manager                                    |   True    |    False    |
|  `is_open`  |            `JEBool`            | Whether the game is currently running            |   True    |    False    |
| `resources` |      `JEInternResources`       | Game resource storage                            |   True    |    False    |
| `entities`  |    `JEContainer[JEEntity]`     | Container containing all registered entities     |   True    |    False    |
|  `systems`  | `JEContainer[JEInternSystems]` | Container containing all registered systems      |   True    |    False    |

---

## 🔹 API

|     Function     |                         Arguments                          | Returns | Description                                                                  |
|:----------------:|:----------------------------------------------------------:|:-------:|------------------------------------------------------------------------------|
|    `__init__`    | `use_clock: JEBool = JEFalse, use_input: JEBool = JEFalse` |         | Creates a new game instance and optionally enables clock and input handling. |
|   `set_window`   |                     `window: JEWindow`                     |         | Assigns the game window.                                                     |
|  `is_key_down`   |                      `key: JEKeyCode`                      | `bool`  | Checks whether a keyboard key is pressed (requires input handling).          |
| `is_mouse_down`  |                   `button: JEMouseCode`                    | `bool`  | Checks whether a mouse button is pressed (requires input handling).          |
|     `close`      |                                                            |         | Closes the game instance and stops execution.                                |
|    `refresh`     |                                                            |         | Refreshes game information, system caches, and internal subsystems.          |
| `refresh_entity` |                     `entity: JEEntity`                     |         | Refreshes internal data for a single entity.                                 |
|   `add_entity`   |        `entity: JEEntity, refresh: JEBool = JETrue`        |         | Adds an entity to the game entity container.                                 |
|   `add_system`   |                 `system: JEInternSystems`                  |         | Adds a system to the game system container.                                  |
|     `update`     |                                                            |         | Updates entities through registered systems.                                 |
|    `display`     |                                                            |         | Displays the game window content.                                            |

---

## 🔹 Usage

```python
from jarengine.games.game import JEGame
from jarengine.games.window import JEWindow
from jarengine.systems.bool import JEBool

game = JEGame(
    use_clock=JETrue,
    use_input=JETrue
)

game.set_window(JEWindow(title="My JarEngine Game"))

while game.is_open:
    game.update()
    game.display()
```

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
