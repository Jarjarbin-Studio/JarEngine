---
layout: page
title: JarEngine - Events
sidebar: sidebar
permalink: /module_events.html
---

# 📦 Events

> Overview of the `Events` module in JarEngine.

---

## 🔹 Overview

**`Events` is a JarEngine module responsible for events handling.**

It provides:

* Event watchers
* Automatic event dispatcher
* Key and Mouse codes (also used for input)

---

## 🔹 Structure

```text
jarengine/
└── events/
    ├── __init__.py
    ├── event.py
    ├── keyboard.py
    ├── manager.py
    └── mouse.py
```

| File          | Description                                             |
|---------------|---------------------------------------------------------|
| `__init__.py` | Public module exports.                                  |
| `event.py`    | Event code (singleton and groups) & event watcher       |
| `keyboard.py` | Keyboard code (singleton and groups) & keyboard watcher |
| `manager.py`  | Runtime event object & event handler                    |
| `mouse.py`    | Mouse code (singleton and groups) & mouse watcher       |

---

## 🔹 Main Classes

| Class              | Description                  |
|--------------------|------------------------------|
| `JEEventCode`      | Single event code            |
| `JEEventCodeGroup` | Event code group             |
| `JEEventWatcher`   | Event watcher                |
| `JEKeyCode`        | Single keyboard code         |
| `JEKeyCodeGroup`   | Keyboard code group          |
| `JEKeyWatcher`     | Keyboard watcher             |
| `JEEvent`          | Runtime event                |
| `JEEventHandler`   | Event handler and dispatcher |
| `JEMouseCode`      | Single mouse code            |
| `JEMouseCodeGroup` | Mouse code group             |
| `JEMouseWatcher`   | Mouse watcher                |

Each class has its own documentation page.

---

## 🔹 Usage

### Basic Example

```python
from jarengine import Games, JEEvtQuit

game = JEGame(use_input=True)

def on_quit(game, event):
    game.close()

def on_space(game, event):
    print("Space key pressed")

def on_click(game, event):
    print(f"Mouse clicked: {event.mouse.name}")

# Use the constants where events, keys and mouse are stored

# Watch a pygame event
game.event.add(
    JEEventWatcher(
        JEEvtQuit,
        on_quit
    )
)

# Watch a keyboard input
game.event.add(
    JEKeyWatcher(
        JEKey_Space,
        on_space
    )
)

# Watch a mouse input
game.event.add(
    JEMouseWatcher(
        JEMse_Left,
        on_click
    )
)

while game.is_open:
    game.update()
```

### Typical Workflow

```python
# 1. Create a watcher describing the input/event to monitor
# 2. Register it inside the game's event manager
# 3. The event manager automatically checks events every frame
# 4. Matching watchers execute their callback function

game.event.add(
    JEKeyWatcher(
        JEKeyCode(PGExtern.K_ESCAPE),
        lambda game, event: game.close()
    )
)
```

---

## 🔹 Important Notes

Things to know when using this module:

* Events, Keys and Mouses codes can be brought together by creating a group (like `JEKey_Delete | JEKey_Escape`)
* Runtime events are automatically created from the actual PyGame events.

Common mistakes:

* Do NOT create your own event as it will, in most cases, brake the event handler/dispatcher.

---

## 🔹 Dependencies

Uses:

* `pygame`
* `jarbin-toolkit-error`
* [`JEInternBaseClass`]()📎
* [`JEBool`]()📎

---

## 🔹 Related Modules

* [`...`]()
* [`...`]()
* [`...`]()

---
