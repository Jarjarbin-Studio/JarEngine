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

|                 Class                 | Description               |
|:-------------------------------------:|---------------------------|
| [`•>JEEntity<•`](class_jeentity.md)📎 | Entity (component holder) |

|                          Component                           | Description                  |
|:------------------------------------------------------------:|------------------------------|
|        [`•>JEMusicComponent<•`](component_music.md)📎        | Music (resource)             |
|        [`•>JESoundComponent<•`](component_sound.md)📎        | Sound (resource)             |
|         [`•>JEFontComponent<•`](component_font.md)📎         | Font (resource)              |
|         [`•>JETextComponent<•`](component_text.md)📎         | Text (string)                |
|      [`•>JETextureComponent<•`](component_texture.md)📎      | Texture (resource)           |
|        [`•>JEColorComponent<•`](component_color.md)📎        | Color (JEColor)              |
|      [`•>JEOutlineComponent<•`](component_outline.md)📎      | Outline (JEColor and size)   |
|   [`•>JEVisibilityComponent<•`](component_visibility.md)📎   | Visibility (JEBool)          |
|        [`•>JELayerComponent<•`](component_layer.md)📎        | Layer (integer)              |
|         [`•>JEFlipComponent<•`](component_flip.md)📎         | Flip (tuple: JEBool, JEBool) |
|        [`•>JEGroupComponent<•`](component_group.md)📎        | Group (JEInternOwnership)    |
| [`•>JEAccelerationComponent<•`](component_acceleration.md)📎 | Acceleration (JEVector2D)    |
|         [`•>JEMassComponent<•`](component_mass.md)📎         | Mass (floating point)        |
|     [`•>JEPositionComponent<•`](component_position.md)📎     | Position (JEVector2D)        |
|     [`•>JEVelocityComponent<•`](component_velocity.md)📎     | Velocity (JEVector2D)        |
|         [`•>JESizeComponent<•`](component_size.md)📎         | Size (JEVector2D)            |
|     [`•>JERotationComponent<•`](component_rotation.md)📎     | Rotation (integer)           |

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
* ECS has been optimized by me (and IA) for faster computation, but it is still a layer on top of PyGame, and in Python. So it may be slower than any other engine.

---
