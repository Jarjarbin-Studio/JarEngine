---
layout: page
title: JarEngine - Class - JEMovementSystem
sidebar: sidebar
permalink: /class_jemovementsystem.html
---

# 📦 JEMovementSystem

> Technical reference for the `JEMovementSystem` class of JarEngine.

> Inherit from [`•>JEInternSystems<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEMovementSystem` is responsible for updating the movement logic of entities.**

Provides:
* Entity movement processing through the JarEngine system architecture.
* Automatic integration with the game update cycle.
* Access to entity containers and timing information.

Internal system used by the engine to process movement-related behavior on entities during the update phase. It extends `JEInternSystems` and follows the ECS (Entity Component System) architecture of JarEngine.

---

## 🔹 Location

```text
JarEngine
│
├── systems
│     └── JEMovementSystem
│
└── ...
```

---

## 🔹 Data

No public data nor property

---

## 🔹 API

|  Function  |                                    Arguments                                     | Returns | Description                                                     |
|:----------:|:--------------------------------------------------------------------------------:|:-------:|-----------------------------------------------------------------|
| `__init__` |                                 `owner: JEGame`                                  |         | Creates a movement system attached to a game instance.          |
|  `update`  | `window: JEWindow, entity: JEEntity, entities: JEContainer[JEEntity], dt: float` |         | Updates the movement of an entity during the game update cycle. |

---

## 🔹 Usage

```python
from jarengine import Games

game = Games.JEGame()

movement_system = Games.Systems.JEMovementSystem(game)

game.add_system(movement_system)
```

---
