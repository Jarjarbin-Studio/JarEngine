---
layout: page
title: JarEngine - Module - Games
sidebar: sidebar
permalink: /module_games.html
---

# 📦 Games

> Overview of the `Games` module in JarEngine.

---

## 🔹 Overview

`Games` provides the classes and utilities related to game management, window handling, input processing and ECS systems.

It includes:
* Game management
* Window handling
* User input processing
* ECS update systems

---

## 🔹 Contents

| Class                            | Description                             |
|----------------------------------|-----------------------------------------|
| [`•>JEGame<•`]()📎               | Main game manager and engine controller |
| [`•>JEWindow<•`]()📎             | Window creation and management          |
| [`•>JEInput<•`]()📎              | User input handling                     |
| [`•>JEMovementSystem<•`]()📎     | Entity movement update system           |
| [`•>JEAccelerationSystem<•`]()📎 | Entity acceleration update system       |
| [`•>JERenderSystem<•`]()📎       | Entity rendering update system          |

---

## 🔹 Usage

```python
from jarengine import Games, JETrue

game = Games.JEGame(
    use_clock=JETrue,
    use_input=JETrue
)

window = Games.JEWindow(
    size=(1280, 720),
    title="JarEngine Demo",
    fps=60
)

game.set_window(window)

Games.Systems.JERenderSystem(game)

while game.is_open:
    game.update()
    game.display()
```

The module provides the main runtime objects required to create and run a JarEngine application.

---

## 🔹 Notes

Useful information:

* `JEGame` is the central object connecting the engine systems together.
* Only one main game instance and window should normally be created.
* Systems must be registered before being updated by the game.

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
