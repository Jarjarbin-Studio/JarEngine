---
layout: page
title: JarEngine - Class - JEMouseWatcher
sidebar: sidebar
permalink: /class_jemousewatcher.html
---

# 📦 JEMouseWatcher

> Technical reference for the `JEMouseWatcher` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEMouseWatcher` is responsible for monitoring mouse events and executing actions when matching inputs are detected.**

Provides:
* Mouse event matching through mouse codes and groups.
* Automatic callback execution when a matching event occurs.
* Access to watcher configuration and callback information.

Represents a mouse input watcher used by JarEngine's event system. It links one or multiple mouse buttons to a callback function, allowing games to react to mouse interactions without manually checking every event.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEMouseWatcher
│
└── ...
```

---

## 🔹 Data

|  Field   |        Type        | Description                                     | Property? | Can be set? |
|:--------:|:------------------:|-------------------------------------------------|:---------:|:-----------:|
|   `on`   | `JEMouseCodeGroup` | Mouse codes monitored by the watcher.           |   True    |    False    |
| `params` |   `JEEventCode`    | Event code associated with the watcher.         |   True    |    False    |
|   `do`   |       `str`        | String representation of the callback function. |   True    |    False    |

---

## 🔹 API

|  Function  |                                                      Arguments                                                      | Returns | Description                                                                             |
|:----------:|:-------------------------------------------------------------------------------------------------------------------:|:-------:|-----------------------------------------------------------------------------------------|
| `__init__` | `on: JEMouseCode \| list[JEMouseCode] \| JEMouseCodeGroup, do: Callable[[JEGame, JEEvent], None], on_press: JEBool` |         | Creates a mouse watcher linked to one or multiple mouse inputs and a callback function. |
|  `match`   |                                                  `event: JEEvent`                                                   | `bool`  | Checks if an event matches the watched mouse inputs.                                    |
| `__call__` |                                           `game: JEGame, event: JEEvent`                                            |         | Executes the callback function associated with the watcher.                             |

---

## 🔹 Usage

```python
from jarengine import Events
from jarengine import Games

game = Games.JEGame()

def on_click(game, event):
    print("Mouse clicked")

watcher = Events.Mouse.JEMouseWatcher(
    Events.Mouse.JEMouseCode(1),
    on_click
)

game.event.add(watcher)
```

---
