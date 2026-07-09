---
layout: page
title: JarEngine - Interns
sidebar: sidebar
permalink: /module_interns.html
---

# 📦 Interns

> Overview of the `Interns` module in JarEngine.

---

## 🔹 Overview

**`Interns` is a JarEngine module responsible for private core systems.**

It provides:

* BaseClasse
* Config
* Decorators
* FinalClasses
* HighClasses
* LowClasses

---

## 🔹 Structure

```text
jarengine/
└── <module>/
    ├── __init__.py
    ├── base_classe.py
    ├── config.py
    ├── decorators.py
    ├── final_classes.py
    ├── high_classes.py
    └── low_classes.py
```

| File               | Description                                                                      |
|--------------------|----------------------------------------------------------------------------------|
| `__init__.py`      | Public module exports.                                                           |
| `base_classe.py`   | Core BaseClass inheriting by every classes in JarEngine (directly or indirectly) |
| `config.py`        | Config loader/manager                                                            |
| `decorators.py`    | Custom decorators used by JarEngine                                              |
| `final_classes.py` | Classes furthest of the core that cannot be mutated by inheritance               |
| `high_classes.py`  | Classes further of the core BaseClass (generally using Systems classes)          |
| `low_classes.py`   | Classes closest to core BaseClass                                                |

---

## 🔹 Main Classes

| Class                     | Description                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------|
| `JEInternBaseClass`       | Core BaseClass inheriting by every classes in JarEngine (directly or indirectly)          |
| `JEInternConfig`          | Config loader/manager                                                                     |
| `JEInternEmptyComponent`  | Placeholder for when entities don't have any components                                   |
| `JEInternConfig`          | Config loader/manager                                                                     |
| `JEInternResources`       | Resource holder/manager (using JEContainers)                                              |
| `JEInternWindowSettings`  | Window settings holder (mostly immutable)                                                 |
| `JEInternOwnership`       | Ownership class (used by inheritance), adds parents and children (using JEContainer)      |
| `JEInternEntityComponent` | Base of every entity components                                                           |
| `JEInternSystems`         | Base of every entity systems                                                              |
| `JEInternGraphic`         | Base of every graphic-linked classes (allows naming and object destruction)               |
| `JEInternGraphicalObject` | Base of drawable objects (mostly JEEntity) with dirty tag support, and update placeholder |
| `JEInternResource`        | Base of every game resources with a path handling                                         |

Each class has its own documentation page.

---

## 🔹 Usage

### Basic Example

```python
from jarengine import Entities

# Internal classes are created automatically.
# Creating an entity also creates several internal objects.

entity = Entities.JEEntity(name="Player")

# Users normally never instantiate JEIntern* classes directly.
```

### Typical Workflow

```python
from jarengine import *

init("/home/user/my_game/")

game = Games.JEGame()

# Create an entity
player = Entities.JEEntity(name="Player")

# Add components
Entities.Transforms.JEPositionComponent(player, (100, 100))
Entities.Transforms.JESizeComponent(player, (64, 64))
Entities.Graphics.JEColorComponent(player, (255, 255, 255, 255))

# Register the entity
game.add_entity(player)

# Internally, JarEngine automatically uses:
# - JEInternEntityComponent
# - JEInternOwnership
# - JEInternGraphic
# - JEInternGraphicalObject
# - JEInternSystems
# - JEInternResources
#
# These classes provide the engine's internal architecture and
# are managed automatically during execution.
```

---

## 🔹 Important Notes

Things to know when using this module:

* As the user of my game engine, you shouldn't use the internals.
* But as I like to give freedom to the users of my creations, I still added the access (use them carefully).

---

## 🔹 Dependencies

Uses:

* `jarbin-toolkit-error`
* `jarbin_toolkit_config`
* `datetime`
* [`JETexture`]()📎
* [`JEMusic`]()📎
* [`JESound`]()📎
* [`JEFont`]()📎
* [`JEBool`]()📎

---

## 🔹 Related Modules

* [`...`]()
* [`...`]()
* [`...`]()

---
