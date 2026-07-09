---
layout: page
title: JarEngine - Resources
sidebar: sidebar
permalink: /module_resource.html
---

# 📦 Resources

> Overview of the `Resources` module in JarEngine.

---

## 🔹 Overview

**`Resources` is a JarEngine module responsible for <main responsibility>.**

It provides:

* Font
* Music
* Sound
* Texture

---

## 🔹 Structure

```text
jarengine/
└── resources/
    ├── __init__.py
    ├── font.py
    ├── music.py
    ├── sound.py
    └── texture.py
```

| File          | Description            |
|---------------|------------------------|
| `__init__.py` | Public module exports. |
| `font.py`     | Store font resource    |
| `music.py`    | Store music resource   |
| `sound.py`    | Store sound resource   |
| `texture.py`  | Store texture resource |

---

## 🔹 Main Classes

| Class       | Description              |
|-------------|--------------------------|
| `JEFont`    | Font resource storage    |
| `JEMusic`   | Music resource storage   |
| `JESound`   | Sound resource storage   |
| `JETexture` | Texture resource storage |

Each class has its own documentation page.

---

## 🔹 Usage

### Basic Example

```python
from jarengine import Resources

# Create a texture resource
texture = Resources.JETexture(
    "player_texture",
    "player.png"
)

# Create a font resource
font = Resources.JEFont(
    "default_font",
    "Nasalization.otf",
    20
)
```

### Typical Workflow

```python
from jarengine import Resources, init, Games

init("/home/user/my_game/")

game = Games.JEGame()

# Create resources
player_texture = Resources.JETexture(
    "player",
    "player.png"
)

main_font = Resources.JEFont(
    "main_font",
    "Nasalization.otf",
    24
)

music = Resources.JEMusic(
    "background_music",
    "background.ogg"
)

sound = Resources.JESound(
    "click_sound",
    "click.wav"
)

# Register resources
game.ressource.texture.add(player_texture)
game.ressource.font.add(main_font)
game.ressource.music.add(music)
game.ressource.sound.add(sound)

# Resources are now available during gameplay
```

---

## 🔹 Important Notes

Things to know when using this module:

* These resources classes don't do anything else other than storing, they won't do any actions on the resources.

Common mistakes:

* Forgetting to add the resource to the game resource manager.

---

## 🔹 Dependencies

Uses:

* `pygame`
* `jarbin-toolkit-error`
* [`JEInternBaseClass`]()📎
* [`JEVector2D`]()📎
* [`JEInternResource`]()📎
* [`JEInternOwnership`]()📎
* [`JEInternConfig`]()📎

---

## 🔹 Related Modules

* [`...`]()
* [`...`]()
* [`...`]()

---
