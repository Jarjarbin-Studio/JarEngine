---
layout: page
title: JarEngine - Class - JEClock
sidebar: sidebar
permalink: /class_jeclock.html
---

# 📦 JEClock

> Technical reference for the `JEClock` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEClock` is responsible for controlling game timing and frame rate management.**

Provides:
* Delta time calculation
* Target FPS control
* Current FPS tracking

It is used by `JEGame` to keep gameplay updates synchronized and independent from hardware performance.

---

## 🔹 Location

```text
JarEngine
│
├── Systems
│     └── JEClock
│
└── ...
```

---

## 🔹 Data

|    Field     |  Type   | Description                        | Property? | Can be set? |
|:------------:|:-------:|------------------------------------|:---------:|:-----------:|
|     `dt`     | `float` | Time elapsed since the last update |   True    |    False    |
| `target_fps` |  `int`  | Target frame rate limit            |   True    |    True     |
|    `fps`     | `float` | Current measured FPS               |   True    |    False    |

---

## 🔹 API

|   Function    | Arguments  | Returns | Description                       |
|:-------------:|:----------:|:-------:|-----------------------------------|
| `__init__()`  | `fps: int` |         | Creates a clock with a target FPS |
|  `update()`   |            |         | Updates timing information        |
| `__float__()` |            | `float` | Returns current delta time        |

---

## 🔹 Usage

```python
from jarengine import Systems

# Create a clock targeting 60 FPS
clock = Systems.JEClock(60)

# Update clock every frame
clock.update()

# Use timing information
delta_time = clock.dt
current_fps = clock.fps

print(delta_time)
print(current_fps)
```

---
