---
layout: page
title: JarEngine - Component - Music
sidebar: sidebar
permalink: /component_music.html
---

# 📦 JEMusicComponent

> Technical reference for the `JEMusicComponent` component of JarEngine.

---

## 🔹 Overview

**`JEMusicComponent` stores and manages the music resource attached to an entity.**

Provides:
* Music resource storage using `JEMusic`.
* Music playback control through entity components.
* Volume management and playback state control.

Used by entities requiring background music or audio playback functionality.

---

## 🔹 Data

|  Field   |   Type    | Description                            |
|:--------:|:---------:|----------------------------------------|
| `music`  | `JEMusic` | Music resource attached to the entity. |
| `volume` |  `float`  | Current music volume value.            |

---

## 🔹 Used by

### Entity
* `set_music`
* `play_music`
* `pause_music`
* `resume_music`
* `stop_music`
* `set_music_volume`
* `get_music`

### System
* No system currently requires this component.

---