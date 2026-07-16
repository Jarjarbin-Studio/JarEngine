---
layout: page
title: JarEngine - Module - Events
sidebar: sidebar
permalink: /module_events.html
---

# 📦 Events

> Overview of the `Events` module in JarEngine.

---

## 🔹 Overview

`Events` provides the classes and utilities related to event handling and input monitoring.

It includes:
* Event watchers and dispatcher
* Keyboard and mouse input codes
* Runtime event management

---

## 🔹 Contents

| Class                        | Description            |
|------------------------------|------------------------|
| [`•>JEEvent<•`]()📎          | Runtime event object   |
| [`•>JEEventHandler<•`]()📎   | Event dispatcher       |
| [`•>JEEventCode<•`]()📎      | Single event code      |
| [`•>JEEventCodeGroup<•`]()📎 | Event code group       |
| [`•>JEEventWatcher<•`]()📎   | Event callback watcher |
| [`•>JEKeyCode<•`]()📎        | Single keyboard code   |
| [`•>JEKeyCodeGroup<•`]()📎   | Keyboard code group    |
| [`•>JEKeyWatcher<•`]()📎     | Keyboard input watcher |
| [`•>JEMouseCode<•`]()📎      | Single mouse code      |
| [`•>JEMouseCodeGroup<•`]()📎 | Mouse code group       |
| [`•>JEMouseWatcher<•`]()📎   | Mouse input watcher    |

---

## 🔹 Usage

```python
from jarengine import JEGame, JEEvtQuit, JEKey_Space
from jarengine.events import Event, EventKeyboard

game = JEGame(use_input=True)

# Create event callbacks
def on_quit(game, event):
    game.close()

def on_space(game, event):
    print("Space pressed")

# Register event watchers
game.event.add(
    Event.JEEventWatcher(
        JEEvtQuit,
        on_quit
    )
)

game.event.add(
    EventKeyboard.JEKeyWatcher(
        JEKey_Space,
        on_space
    )
)

while game.is_open:
    game.update()
```

Events are registered as watchers and automatically processed by the game's event manager.

---

## 🔹 Notes

Useful information:

* Event, keyboard and mouse codes can be combined into groups.
* Runtime events are automatically generated from PyGame events.
* Avoid creating custom runtime events manually.

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
