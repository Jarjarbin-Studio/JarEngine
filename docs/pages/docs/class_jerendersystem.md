---

layout: page
title: JarEngine - Class - JERenderSystem
sidebar: sidebar
permalink: /class_jerendersystem.html
-------------------------------------

# 📦 JERenderSystem

> Technical reference for the `JERenderSystem` class of JarEngine.

> Inherit from [`•>JEInternSystems<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JERenderSystem` is responsible for updating the rendering logic of entities.**

Provides:

* Entity rendering processing through the JarEngine system architecture.
* Automatic integration with the game rendering workflow.
* Access to entity containers, window rendering context, and timing information.

Internal system used by the engine to process visual rendering behavior on entities during the update phase. It extends `JEInternSystems` and follows the ECS (Entity Component System) architecture of JarEngine.

---

## 🔹 Location

```text
JarEngine
│
├── systems
│     └── JERenderSystem
│
└── ...
```

---

## 🔹 Data

No public data nor property

---

## 🔹 API

|  Function  |                                    Arguments                                     | Returns | Description                                                      |
|:----------:|:--------------------------------------------------------------------------------:|:-------:|------------------------------------------------------------------|
| `__init__` |                                 `owner: JEGame`                                  |         | Creates a render system attached to a game instance.             |
|  `update`  | `window: JEWindow, entity: JEEntity, entities: JEContainer[JEEntity], dt: float` |         | Updates the rendering of an entity during the game update cycle. |

---

## 🔹 Usage

```python
from jarengine import Games

game = Games.JEGame()

render_system = Games.Systems.JERenderSystem(game)

game.add_system(render_system)
```

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
