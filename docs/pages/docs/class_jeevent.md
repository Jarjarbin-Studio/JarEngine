---
layout: page
title: JarEngine - Class - JEEvent
sidebar: sidebar
permalink: /class_jeevent.html
---

# 📦 JEEvent

> Technical reference for the `JEEvent` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEEvent` is responsible for representing and abstracting PyGame events inside JarEngine.**

Provides:
* Access to event type information through `JEEventCode`.
* Extraction of keyboard and mouse input data.
* A unified event representation for JarEngine's event system.

Acts as a wrapper around PyGame events, converting low-level PyGame event objects into structured JarEngine objects. It is mainly used by event handlers, watchers, and input systems to process user interactions in a consistent way.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEEvent
│
└── ...
```

---

## 🔹 Data

|  Field  |          Type           | Description                               | Property? | Can be set? |
|:-------:|:-----------------------:|-------------------------------------------|:---------:|:-----------:|
| `type`  |      `JEEventCode`      | Event code identifying the event type.    |   True    |    False    |
|  `key`  |  `Optional[JEKeyCode]`  | Key code associated with keyboard events. |   True    |    False    |
| `mouse` | `Optional[JEMouseCode]` | Mouse code associated with mouse events.  |   True    |    False    |

---

## 🔹 API

|  Function  |          Arguments          | Returns | Description                                            |
|:----------:|:---------------------------:|:-------:|--------------------------------------------------------|
| `__init__` | `event: PyGame.event.Event` |         | Creates a JarEngine event wrapper from a PyGame event. |

---

## 🔹 Usage

```python
from jarengine import Events
import pygame

for pygame_event in pygame.event.get():
    event = JEEvent(pygame_event)

    print(f"\nEvent: {event.type}")

    if event.key:
        print(f"Key pressed: {event.key}")

    if event.key:
        print(f"Mouse pressed: {event.mouse}")
```

---
