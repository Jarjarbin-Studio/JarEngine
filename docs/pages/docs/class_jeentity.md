---
layout: page
title: JarEngine - Class - JEEntity
sidebar: sidebar
permalink: /class_jeentity.html
---

# 📦 JEEntity

> Technical reference for the `JEEntity` class of JarEngine.

> Inherit from [`•>JEInternGraphicalObject<•`]()📎 and [`•>JEInternOwnership<•`]()📎

---

## 🔹 Overview

**`JEEntity` is responsible for representing every interactive object that exists inside a JarEngine game.**

Provides:
* Component-based architecture for building game objects.
* Unified interface for graphics, physics, audio, transforms, and custom behaviors.
* Deep-copy support and automatic integration with JarEngine systems.

`JEEntity` is the foundation of JarEngine's Entity Component System (ECS). Rather than inheriting specialized classes, entities are composed by attaching components that define their capabilities. Systems then iterate over entities and update only the components they require, making entities lightweight, modular, extensible, and reusable across different projects.

---

## 🔹 Location

```text
JarEngine
│
├── entity
│     └── JEEntity
│
└── ...
```

---

## 🔹 Data

|    Field     |                  Type                  | Description                                           | Property? | Can be set? |
|:------------:|:--------------------------------------:|-------------------------------------------------------|:---------:|:-----------:|
| `components` | `JEContainer[JEInternEntityComponent]` | Collection of every component attached to the entity. |   True    |    False    |

---

## 🔹 API

|    Function     |              Arguments               |          Returns          | Description                                                        |
|:---------------:|:------------------------------------:|:-------------------------:|--------------------------------------------------------------------|
|   `__init__`    |       `name: str = "JEEntity"`       |                           | Creates a new entity with the specified name.                      |
| `add_component` | `component: JEInternEntityComponent` |                           | Attaches a component to the entity.                                |
|      `get`      |          `component: type`           | `JEInternEntityComponent` | Retrieves the first component matching the specified type.         |
|     `copy`      |                                      |        `JEEntity`         | Creates a complete deep copy of the entity and all its components. |

|    Component     |        Function        |                               Arguments                               |         Returns         | Description                                      |
|:----------------:|:----------------------:|:---------------------------------------------------------------------:|:-----------------------:|--------------------------------------------------|
|     **Font**     |       `set_font`       |                            `font: JEFont`                             |                         | Sets the entity font resource.                   |
|                  |       `get_font`       |                                                                       |        `JEFont`         | Returns the entity font resource.                |
|     **Text**     |       `set_text`       |                              `text: str`                              |                         | Sets the displayed text.                         |
|                  |       `get_text`       |                                                                       |          `str`          | Returns the displayed text.                      |
|   **Texture**    |     `set_texture`      |                         `texture: JETexture`                          |                         | Sets the entity texture resource.                |
|                  |     `get_texture`      |                                                                       |       `JETexture`       | Returns the entity texture resource.             |
|    **Color**     |      `set_color`       | `color: JEColor \| tuple[int, int, int] \| tuple[int, int, int, int]` |                         | Sets the entity color.                           |
|                  |     `update_color`     |                   `r: int, g: int, b: int, a: int`                    |                         | Updates the current entity color.                |
|                  |      `get_color`       |                                                                       |        `JEColor`        | Returns the entity color.                        |
|   **Outline**    |  `set_outline_color`   | `color: JEColor \| tuple[int, int, int] \| tuple[int, int, int, int]` |                         | Sets the outline color.                          |
|                  | `update_outline_color` |                   `r: int, g: int, b: int, a: int`                    |                         | Updates the current outline color.               |
|                  |  `get_outline_color`   |                                                                       |        `JEColor`        | Returns the outline color.                       |
|                  |   `set_outline_size`   |                              `size: int`                              |                         | Sets the outline thickness.                      |
|                  | `update_outline_size`  |                               `s: int`                                |                         | Updates the current outline thickness.           |
|                  |   `get_outline_size`   |                                                                       |          `int`          | Returns the outline thickness.                   |
|  **Visibility**  |    `set_visibility`    |                         `visibility: JEBool`                          |                         | Sets the entity visibility.                      |
|                  |    `get_visibility`    |                                                                       |        `JEBool`         | Returns the entity visibility.                   |
|    **Layer**     |      `set_layer`       |                             `layer: int`                              |                         | Sets the rendering layer.                        |
|                  |     `update_layer`     |                               `l: int`                                |                         | Updates the current rendering layer.             |
|                  |      `get_layer`       |                                                                       |          `int`          | Returns the rendering layer.                     |
|     **Flip**     |       `set_flip`       |                     `flip: tuple[JEBool, JEBool]`                     |                         | Sets the sprite flip state.                      |
|                  |       `get_flip`       |                                                                       | `tuple[JEBool, JEBool]` | Returns the sprite flip state.                   |
|    **Music**     |      `set_music`       |                           `music: JEMusic`                            |                         | Sets the music resource.                         |
|                  |      `play_music`      |                              `loop: int`                              |                         | Plays the music resource.                        |
|                  |     `pause_music`      |                                                                       |                         | Pauses the music playback.                       |
|                  |     `resume_music`     |                                                                       |                         | Resumes the music playback.                      |
|                  |      `stop_music`      |                                                                       |                         | Stops the music playback.                        |
|                  |   `set_music_volume`   |                             `volume: int`                             |                         | Sets the music volume.                           |
|                  |      `get_music`       |                                                                       |        `JEMusic`        | Returns the music resource.                      |
|    **Sound**     |      `set_sound`       |                           `sound: JESound`                            |                         | Sets the sound resource.                         |
|                  |      `play_sound`      |                              `loop: int`                              |                         | Plays the sound resource.                        |
|                  |      `stop_sound`      |                                                                       |                         | Stops the sound playback.                        |
|                  |     `pause_sound`      |                                                                       |                         | Pauses the sound playback.                       |
|                  |     `resume_sound`     |                                                                       |                         | Resumes the sound playback.                      |
|                  |      `fade_sound`      |                          `milliseconds: int`                          |                         | Fades out the sound over the specified duration. |
|                  |   `set_sound_volume`   |                             `volume: int`                             |                         | Sets the sound volume.                           |
|                  |      `get_sound`       |                                                                       |        `JESound`        | Returns the sound resource.                      |
| **Acceleration** |   `set_acceleration`   |           `acceleration: JEVector2D \| tuple[float, float]`           |                         | Sets the entity acceleration.                    |
|                  | `update_acceleration`  |                         `x: float, y: float`                          |                         | Updates the current acceleration.                |
|                  |   `get_acceleration`   |                                                                       |      `JEVector2D`       | Returns the entity acceleration.                 |
|     **Mass**     |       `set_mass`       |                             `mass: float`                             |                         | Sets the entity mass.                            |
|                  |     `update_mass`      |                              `m: float`                               |                         | Updates the current mass.                        |
|                  |       `get_mass`       |                                                                       |         `float`         | Returns the entity mass.                         |
|   **Position**   |     `set_position`     |             `position: JEVector2D \| tuple[float, float]`             |                         | Sets the entity position.                        |
|                  |   `update_position`    |                         `x: float, y: float`                          |                         | Updates the current position.                    |
|                  |     `get_position`     |                                                                       |      `JEVector2D`       | Returns the entity position.                     |
|   **Velocity**   |     `set_velocity`     |             `velocity: JEVector2D \| tuple[float, float]`             |                         | Sets the entity velocity.                        |
|                  |   `update_velocity`    |                         `x: float, y: float`                          |                         | Updates the current velocity.                    |
|                  |     `get_velocity`     |                                                                       |      `JEVector2D`       | Returns the entity velocity.                     |
|     **Size**     |       `set_size`       |               `size: JEVector2D \| tuple[float, float]`               |                         | Sets the entity size.                            |
|                  |     `update_size`      |                         `x: float, y: float`                          |                         | Updates the current size.                        |
|                  |       `get_size`       |                                                                       |      `JEVector2D`       | Returns the entity size.                         |
|   **Rotation**   |     `set_rotation`     |                           `rotation: float`                           |                         | Sets the entity rotation in degrees.             |
|                  |   `update_rotation`    |                              `r: float`                               |                         | Updates the current rotation.                    |
|                  |     `get_rotation`     |                                                                       |         `float`         | Returns the entity rotation in degrees.          |
|    **Group**     |      `group_add`       |                          `entity: JEEntity`                           |                         | Adds an entity to the group.                     |
|                  |     `group_remove`     |                          `entity: JEEntity`                           |                         | Removes an entity from the group.                |
|                  |      `get_group`       |                                                                       | `JEContainer[JEEntity]` | Returns the entity group.                        |


---

## 🔹 Usage

```python
from jarengine.entity.entity import JEEntity
from jarengine.components.position import JEPositionComponent
from jarengine.components.velocity import JEVelocityComponent

player = JEEntity(name="Player")

player.add_component(JEPositionComponent())
player.add_component(JEVelocityComponent())

position = player.get(JEPositionComponent)

clone = player.copy()
```

---
