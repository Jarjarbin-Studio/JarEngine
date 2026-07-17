---
layout: page
title: JarEngine - Component - Sound
sidebar: sidebar
permalink: /component_sound.html
---

# 📦 JESoundComponent

> Technical reference for the `JESoundComponent` component of JarEngine.

---

## 🔹 Overview

**`JESoundComponent` stores and manages the sound resource attached to an entity.**

Provides:
* Sound resource storage using `JESound`.
* Sound playback control through entity components.
* Volume management and channel control.

Used by entities requiring sound effects or audio playback functionality.

---

## 🔹 Data

|  Field   |   Type    | Description                            |
|:--------:|:---------:|----------------------------------------|
| `sound`  | `JESound` | Sound resource attached to the entity. |
| `volume` |  `float`  | Current sound volume value.            |

---

## 🔹 Used by

### Entity
* `set_sound`
* `play_sound`
* `stop_sound`
* `pause_sound`
* `resume_sound`
* `fade_sound`
* `set_sound_volume`
* `get_sound`

### System
* No system currently requires this component.

---