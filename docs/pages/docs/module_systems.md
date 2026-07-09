---
layout: page
title: JarEngine - Systems
sidebar: sidebar
permalink: /module_systems.html
---

# 📦 Systems

> Overview of the `Systems` module in JarEngine.

---

## 🔹 Overview

**`Systems` is a JarEngine module responsible for public core systems.**

It provides:

* Boolean
* Clock
* Color
* Container
* Immutable
* Vector
* Version

---

## 🔹 Structure

```text
jarengine/
└── systems/
    ├── __init__.py
    ├── bool.py
    ├── clock.py
    ├── color.py
    ├── container.py
    ├── immutable.py
    ├── vector.py
    └── version.py
```

| File           | Description                                          |
|----------------|------------------------------------------------------|
| `__init__.py`  | Public module exports.                               |
| `bool.py`      | Custom boolean.                                      |
| `clock.py`     | Clock for controlled fps.                            |
| `color.py`     | Color for RGBA.                                      |
| `container.py` | Container for custom saving/search/iteration.        |
| `immutable.py` | Immutable compatible with any classes (even custom). |
| `vector.py`    | Vectors 2D and 3D.                                   |
| `version.py`   | Version class.                                       |

---

## 🔹 Main Classes

| Class         | Description                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------|
| `JEBool`      | Custom boolean.                                                                                          |
| `JEClock`     | Clock for controlled fps.                                                                                |
| `JEColor`     | Color with simple RGB or full RGBA support.                                                              |
| `JEContainer` | Container for custom saving/search/iteration.                                                            |
| `JEImmutable` | Immutable compatible with any classes (even custom)(with large ammount of builtin class method support). |
| `JEVector2D`  | Vectors2D (x, y) for simple position, velocity or simply for storing 2 float values.                     |
| `JEVector3D`  | Vectors3D (x, y, z) for advanced math or simply for storing 3 float values.                              |
| `JEVersion`   | Version storage (used for JarEngine, PyGame, SDL and Python).                                            |

Each class has its own documentation page.

---

## 🔹 Usage

### Basic Example

```python
from jarengine import JEVector2D, JEColor, JEBool


# Create a position vector
position = JEVector2D(100, 50)

# Modify values
position.x += 10
position.y += 20


# Create a color
color = JEColor(255, 120, 50, 255)

print(position.x, position.y)
print(color.rgba)


# Use JarEngine boolean wrapper
enabled = JEBool(True)

if enabled:
    print("Feature enabled")
````

---

### Typical Workflow

```python
from jarengine import (
    JEVector2D,
    JEColor,
    JEContainer,
    JEImmutable
)

# Create object data
position = JEVector2D(300, 200)
color = JEColor(50, 150, 255, 255)

# Store objects inside a container
container = JEContainer(
    JEVector2D
)
container.add(position)

# Access stored data
current_position = container.get(
    instance=position
)

# Create immutable configuration data
settings = JEImmutable(
    {
        "width": 800,
        "height": 600,
        "fullscreen": False
    }
)

print(current_position.x)
print(settings.data)
```

---

## 🔹 Important Notes

Things to know when using this module:

* The systems classes are very important to the engine, and your game as it is the heart of many systems and components.
* Use the JEImmutable carefully with your custom classes as it is not fireproof (works perfectly for other JarEngine classes).

Common mistakes:

* Systems are not the core of the engine but the surface of it.
* ...

---

## 🔹 Dependencies

Uses:

* `pygame`
* `jarbin-toolkit-error`
* [`JEInternBaseClass`]()📎

---

## 🔹 Related Modules

* [`...`]()
* [`...`]()
* [`...`]()

---
