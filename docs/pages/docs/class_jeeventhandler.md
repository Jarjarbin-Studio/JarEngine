---
layout: page
title: JarEngine - Class - JEEventHandler
sidebar: sidebar
permalink: /class_jeeventhandler.html
---

# 📦 JEEventHandler

> Technical reference for the `JEEventHandler` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`](class_jeinternbaseclass.md)📎

---

## 🔹 Overview

**`JEEventHandler` is responsible for managing event watchers and dispatching incoming events to the appropriate callbacks.**

Provides:
* Registration and removal of event, keyboard, and mouse watchers.
* Centralized processing of PyGame events.
* Automatic dispatch of matching events to registered callbacks.

`JEEventHandler` is the core of JarEngine's event system. It continuously polls PyGame events, wraps them into `JEEvent` objects, and forwards them to every compatible watcher. It allows games to react to user input without manually iterating through the event queue, providing a clean callback-based architecture.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEEventHandler
│
└── ...
```

---

## 🔹 Data

|   Field    |                           Type                           | Description                                               | Property? | Can be set? |
|:----------:|:--------------------------------------------------------:|-----------------------------------------------------------|:---------:|:-----------:|
| `watchers` | `list[JEEventWatcher \| JEKeyWatcher \| JEMouseWatcher]` | List of registered watchers that receive matching events. |   True    |    False    |

---

## 🔹 API

|  Function  |                          Arguments                          | Returns  | Description                                                                              |
|:----------:|:-----------------------------------------------------------:|:--------:|------------------------------------------------------------------------------------------|
| `__init__` |                                                             |          | Creates an empty event handler.                                                          |
|   `add`    | `watcher: JEEventWatcher \| JEKeyWatcher \| JEMouseWatcher` |          | Registers a watcher so it can receive matching events.                                   |
|  `remove`  | `watcher: JEEventWatcher \| JEKeyWatcher \| JEMouseWatcher` |          | Removes a previously registered watcher.                                                 |
|  `clear`   |                                                             |          | Removes every registered watcher from the handler.                                       |
|   `has`    |       `code: JEEventCode \| JEKeyCode \| JEMouseCode`       | `JEBool` | Checks whether at least one watcher is monitoring the specified code.                    |
| `process`  |           `game: JEGame, is_single_match: JEBool`           |          | Polls PyGame events, dispatches them to matching watchers, and executes their callbacks. |

---

## 🔹 Usage

```python
from jarengine import Events
from jarengine import Games

game = Games.JEGame()

def on_quit(game, event):
    game.close()

handler = Events.JEEventHandler()

handler.add(
    Events.Event.JEEventWatcher(
        Events.Event.Event.QUIT,
        on_quit
    )
)

while game.is_open:
    handler.process(game)
```

---
