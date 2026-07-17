---
layout: page
title: JarEngine - Class - JEEventWatcher
sidebar: sidebar
permalink: /class_jeeventwatcher.html
---

# 📦 JEEventWatcher

> Technical reference for the `JEEventWatcher` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEEventWatcher` is responsible for monitoring general events and executing actions when matching event codes are detected.**

Provides:
* Event matching through event codes and groups.
* Automatic callback execution when a matching event occurs.
* Access to watcher configuration and callback information.

Represents a generic event watcher used by JarEngine's event system. It links one or multiple event codes to a callback function, allowing games to react to custom events without manually filtering every received event.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEEventWatcher
│
└── ...
```

---

## 🔹 Data

| Field |        Type        | Description                                     | Property? | Can be set? |
|:-----:|:------------------:|-------------------------------------------------|:---------:|:-----------:|
| `on`  | `JEEventCodeGroup` | Event codes monitored by the watcher.           |   True    |    False    |
| `do`  |       `str`        | String representation of the callback function. |   True    |    False    |

---

## 🔹 API

|  Function  |                                             Arguments                                             | Returns | Description                                                                             |
|:----------:|:-------------------------------------------------------------------------------------------------:|:-------:|-----------------------------------------------------------------------------------------|
| `__init__` | `on: JEEventCode \| list[JEEventCode] \| JEEventCodeGroup, do: Callable[[JEGame, JEEvent], None]` |         | Creates an event watcher linked to one or multiple event codes and a callback function. |
|  `match`   |                                         `event: JEEvent`                                          | `bool`  | Checks if an event matches the watched event codes.                                     |
| `__call__` |                                  `game: JEGame, event: JEEvent`                                   |         | Executes the callback function associated with the watcher.                             |

---

## 🔹 Usage

```python
from jarengine import Events
from jarengine import Games

game = Games.JEGame()

def on_event(game, event):
    print("Event received")

watcher = Events.Event.JEEventWatcher(
    Events.Event.JEEventCode(1),
    on_event
)

game.event.add(watcher)
```

---
