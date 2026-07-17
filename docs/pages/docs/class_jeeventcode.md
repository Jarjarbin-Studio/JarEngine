---
layout: page
title: JarEngine - Class - JEEventCode
sidebar: sidebar
permalink: /class_jeeventcode.html
---

# 📦 JEEventCode

> Technical reference for the `JEEventCode` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEEventCode` is responsible for representing and managing event input codes in JarEngine.**

Provides:
* Event identification and comparison.
* Conversion between internal event codes and integer values.
* Event code grouping through operator overloading.

Represents an event identifier used by JarEngine's event management system. It allows events to be handled as structured objects instead of raw integer values, providing easier comparison, grouping, and debugging capabilities.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEEventCode
│
└── ...
```

---

## 🔹 Data

| Field  | Type  | Description                | Property? | Can be set? |
|:------:|:-----:|----------------------------|:---------:|:-----------:|
| `name` | `str` | Human-readable event name. |   True    |    False    |

---

## 🔹 API

|  Function  |       Arguments        |      Returns       | Description                                                                 |
|:----------:|:----------------------:|:------------------:|-----------------------------------------------------------------------------|
| `__init__` | `event: Optional[int]` |                    | Creates an event code object from an optional event identifier.             |
| `__int__`  |                        |       `int`        | Converts the event code into its integer representation.                    |
| `__str__`  |                        |       `str`        | Human-readable event name.                                                  |
|  `__or__`  |  `other: JEEventCode`  | `JEEventCodeGroup` | Creates an event group by combining two event codes.                        |
|  `__eq__`  |  `other: JEEventCode`  |      `JEBool`      | Compares two event codes and returns whether they represent the same event. |
| `__hash__` |                        |       `int`        | Generates a hash value from the event code for future usage.                |

---

## 🔹 Usage

```python
from jarengine import Events

quit_event = Events.Event.JEEventCode(1)
resize_event = Events.Event.JEEventCode(2)

if quit_event == Events.Event.JEEventCode(1):
    print("Quit event detected")

event_group = quit_event | resize_event
```

---
