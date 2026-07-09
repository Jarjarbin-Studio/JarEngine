---
layout: page
title: JarEngine - Events
sidebar: sidebar
permalink: /module_events.html
---

# 📦 Entities

> Overview of the `Entities` module in JarEngine.

---

## 🔹 Overview

**`Entities` is a JarEngine module responsible for ECS entities and components.**

It provides:

* Audios components
* Graphics components
* Others components
* Physics components
* Transforms components
* Entity

---

## 🔹 Structure

```text
jarengine/
└── entities/
    ├── __init__.py
    ├── components_audios.py
    ├── components_graphics.py
    ├── components_others.py
    ├── components_physics.py
    ├── components_transforms.py
    └── entity.py
```

| File                    | Description                                      |
|-------------------------|--------------------------------------------------|
| `__init__.py`           | Public module exports.                           |
| `components_audios`     | Audios components (music, sound)                 |
| `components_graphics`   | Graphics components (texture, color, layer)      |
| `components_others`     | Others components (group)                        |
| `components_physics`    | Physics components (acceleration, mass)          |
| `components_transforms` | Transforms components (position, size, rotation) |
| `entity`                | Main entity class (component holder)             |

---

## 🔹 Main Classes

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

Each class has its own documentation page.

---

## 🔹 Usage

### Basic Example

```python
from jarengine import Entities

# Create an entity
player = Entities.JEEntity(name="Player")

# Add components to define its behavior and data
player.add_component(
    Entities.Transforms.JEPositionComponent(
        player,
        (100, 200)
    )
)

player.add_component(
    Entities.Transforms.JEVelocityComponent(
        player,
        (5, 0)
    )
)

player.add_component(
    Entities.Graphics.JEColorComponent(
        player,
        (255, 255, 255, 255)
    )
)

# Components automatically expose helper methods on the entity
player.update_position(x=10, y=-20)
player.update_velocity(x=1)

print(player.get_position())
print(player.get_velocity())
```

### Typical Workflow

```python
# 1. Create an entity containing the base entity structure
entity = Entities.JEEntity()

# 2. Add components to describe its properties
entity.add_component(Component(entity, data))

# 3. Add the entity to game for automatic update through systems
game.add_entity(entity)

# 4. Retrieve or modify component data through the entity
component = entity.get(Component)

# 5. Use the generated entity helpers or component API
entity.set_position((50, 50))
```

---

## 🔹 Important Notes

Things to know when using this module:

* Entity alone doesn't do anything, components are required.
* Components such as group makes the entity a holder of other entities.
* ECS has been optimized by me (and IA) for faster computation, but it is still a layer on top of pygame, and in Python. So it may be slower than any other engine.

---

## 🔹 Dependencies

Uses:

* `pygame`
* [`JEInternEntityComponent`]()📎
* [`JEVector2D`]()📎
* [`JEInternOwnership`]()📎
* [`JEInternEmptyComponent`]()📎
* [`JEInternGraphicalObject`]()📎
* [`JEContainer`]()📎
* [`JEBool`]()📎

---

## 🔹 Related Modules

* [`...`]()
* [`...`]()
* [`...`]()

---
