---
layout: page
title: Home
sidebar: sidebar
permalink: /Home.html
---

# 📦 JarEngine Documentation

## 🔹 Overview

JarEngine is a lightweight Python game framework built on top of Pygame. It provides structured abstractions for game development, including entity management, rendering systems, input handling, and resource management.

The engine is designed for:

* Educational use
* Small to medium-scale game projects
* Rapid prototyping
* Structured engine architecture learning

---

## 🔹 Architecture Overview

```text
JarEngine
│
├── interns        → Core internal abstractions
├── entities       → Entity/component system
├── events         → Input and event handling
├── games          → Game loop and runtime systems
├── resources      → Assets (textures, fonts)
├── systems        → Low-level data structures
├── audios         → Audio system layer
└── constants      → Global constants
````

---

## 🔹 Core Principles

* Clear separation of systems and data
* Lightweight abstraction over Pygame
* Modular and extensible structure
* Engine-first design (not game-first)
* Explicit ownership and lifecycle control

---

## 🔹 Main Modules

| Module    | Responsibility                   |
|-----------|----------------------------------|
| interns   | Internal engine infrastructure   |
| entities  | ECS-style entity management      |
| events    | Input handling (keyboard, mouse) |
| games     | Runtime loop and game structure  |
| resources | Asset loading and management     |
| systems   | Primitive data structures        |
| audios    | Audio abstraction layer          |
| constants | Global configuration values      |

---

## 🔹 Navigation

Use the sidebar to explore:

* Core engine internals
* Systems and primitives
* Entity/component architecture
* Input and event system
* Resource handling
* Templates and guides

---

## 🔹 Current Status

⚠️ Active development stage

### Implemented

* Core architecture modules
* Base entity system
* Resource abstraction layer
* System primitives

### Planned

* Advanced ECS optimization
* Audio system expansion
* Rendering pipeline improvements
* Tooling and debug utilities

---

## 🔹 Notes

JarEngine is not a replacement for Pygame. It is a structured abstraction layer intended to simplify development while enforcing a clean architecture model.
