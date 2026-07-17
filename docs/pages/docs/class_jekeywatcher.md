---
layout: page
title: JarEngine - Class - JEKeyWatcher
sidebar: sidebar
permalink: /class_jekeywatcher.html
---

# 📦 JEKeyWatcher

> Technical reference for the `JEKeyWatcher` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEKeyWatcher` is responsible for monitoring keyboard events and executing actions when matching inputs are detected.**

Provides:
* Keyboard event matching through key codes and groups.
* Automatic callback execution when a matching event occurs.
* Access to watcher configuration and callback information.

Represents a keyboard input watcher used by JarEngine's event system. It links one or multiple keys to a callback function, allowing games to react to keyboard interactions without manually checking every event.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEKeyWatcher
│
└── ...
```

---

## 🔹 Data

|  Field   |       Type       | Description                                     | Property? | Can be set? |
|:--------:|:----------------:|-------------------------------------------------|:---------:|:-----------:|
|   `on`   | `JEKeyCodeGroup` | Keys monitored by the watcher.                  |   True    |    False    |
| `params` |  `JEEventCode`   | Event code associated with the watcher.         |   True    |    False    |
|   `do`   |      `str`       | String representation of the callback function. |   True    |    False    |

---

## 🔹 API

|  Function  |                                                   Arguments                                                   | Returns | Description                                                                              |
|:----------:|:-------------------------------------------------------------------------------------------------------------:|:-------:|------------------------------------------------------------------------------------------|
| `__init__` | `on: JEKeyCode \| list[JEKeyCode] \| JEKeyCodeGroup, do: Callable[[JEGame, JEEvent], None], on_press: JEBool` |         | Creates a key watcher linked to one or multiple keyboard inputs and a callback function. |
|  `match`   |                                               `event: JEEvent`                                                | `bool`  | Checks if an event matches the watched keyboard inputs.                                  |
| `__call__` |                                        `game: JEGame, event: JEEvent`                                         |         | Executes the callback function associated with the watcher.                              |

---

## 🔹 Usage

```python
from jarengine import Events
from jarengine import Games

game = Games.JEGame()

def on_jump(game, event):
    print("Jump key pressed")

watcher = Events.Keyboard.JEKeyWatcher(
    Events.Keyboard.JEKeyCode(32),
    on_jump
)

game.event.add(watcher)
```

---
