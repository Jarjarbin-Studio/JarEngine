---
layout: page
title: JarEngine - Class - JEEventCodeGroup
sidebar: sidebar
permalink: /class_jeeventcodegroup.html
---

# 📦 JEEventCodeGroup

> Technical reference for the `JEEventCodeGroup` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEEventCodeGroup` is responsible for grouping multiple event codes into a single event collection.**

Provides:
* Storage of multiple `JEEventCode` objects.
* Event group combination through operator overloading.
* Iteration support over stored events.

Represents a collection of event identifiers used by JarEngine's event management system. It allows multiple events to be handled together, simplifying event comparisons and input handling while keeping compatibility with individual `JEEventCode` objects.

---

## 🔹 Location

```text
JarEngine
│
├── events
│     └── JEEventCodeGroup
│
└── ...
```

---

## 🔹 Data

|  Field   |        Type         | Description                                | Property? | Can be set? |
|:--------:|:-------------------:|--------------------------------------------|:---------:|:-----------:|
| `events` | `list[JEEventCode]` | Stored event codes contained in the group. |   True    |    False    |

---

## 🔹 API

|  Function  |                Arguments                 |         Returns         | Description                                                                              |
|:----------:|:----------------------------------------:|:-----------------------:|------------------------------------------------------------------------------------------|
| `__init__` |       `events: list[JEEventCode]`        |                         | Creates an event group from a list of event codes.                                       |
|  `__or__`  | `other: JEEventCode \| JEEventCodeGroup` |   `JEEventCodeGroup`    | Creates a new event group by combining existing event codes with another event or group. |
| `__iter__` |                                          | `Iterator[JEEventCode]` | Returns an iterator over the stored event codes.                                         |

---

## 🔹 Usage

```python
from jarengine import Events

quit_event = Events.Event.JEEventCode(1)
resize_event = Events.Event.JEEventCode(2)

event_group = quit_event | resize_event

for event in event_group:
    print(int(event))
```

---
