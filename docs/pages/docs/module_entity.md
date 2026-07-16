---
layout: page
title: JarEngine - Module - Entity
sidebar: sidebar
permalink: /module_entity.html
---


# 📦 <Module Name>

> Overview of the `Entity` module in JarEngine.

---

## 🔹 Overview

**`Entity` is a JarEngine module responsible for ECS entity and components.**

It provides:

* Audios components
* Graphics components
* Others components
* Physics components
* Transforms components
* Entity

---

## 🔹 Contents

| Class                     | Description                  |
|---------------------------|------------------------------|
| `JEMusicComponent`        | Music (resource)             |
| `JESoundComponent`        | Sound (resource)             |
| `JEFontComponent`         | Font (resource)              |
| `JETextComponent`         | Text (string)                |
| `JETextureComponent`      | Texture (resource)           |
| `JEColorComponent`        | Color (JEColor)              |
| `JEOutlineComponent`      | Outline (JEColor and size)   |
| `JEVisibilityComponent`   | Visibility (JEBool)          |
| `JELayerComponent`        | Layer (integer)              |
| `JEFlipComponent`         | Flip (tuple: JEBool, JEBool) |
| `JEGroupComponent`        | Group (JEInternOwnership)    |
| `JEAccelerationComponent` | Acceleration (JEVector2D)    |
| `JEMassComponent`         | Mass (floating point)        |
| `JEPositionComponent`     | Position (JEVector2D)        |
| `JEVelocityComponent`     | Velocity (JEVector2D)        |
| `JESizeComponent`         | Size (JEVector2D)            |
| `JERotationComponent`     | Rotation (integer)           |
| `JEEntity`                | Entity (component holder)    |

---

## 🔹 Usage

```python
from jarengine import Entity

# Create an entity
player = Entity.JEEntity(name="Player")

# Add components to define its properties
Entity.Transforms.JEPositionComponent(
    player,
    (100, 200)
)

Entity.Transforms.JEVelocityComponent(
    player,
    (5, 0)
)

Entity.Transforms.JESizeComponent(
    player,
    (20, 20)
)

Entity.Graphics.JEColorComponent(
    player,
    (255, 255, 255, 255)
)

# Components automatically add related helpers to the entity
player.set_position((150, 180))
player.set_velocity((10, 0))

print(player.get_position())
print(player.get_velocity())
```

An entity has been created as a white rectangle of 20 by 20.

---

## 🔹 Notes

Things to know when using this module:

* Entity alone doesn't do anything, components are required.
* Components such as group makes the entity a holder of other entity.
* ECS has been optimized by me (and IA) for faster computation, but it is still a layer on top of pygame, and in Python. So it may be slower than any other engine.

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
