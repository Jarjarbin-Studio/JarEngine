---
layout: page
title: JarEngine
sidebar: sidebar
permalink: /module_jarengine.html
---

# 📦 JarEngine

> Overview of the main module in JarEngine.

---

## 🔹 Overview

**`JarEngine` is the main module containing every sub-modules of the game engine.**

It provides:

* Engine initialization and shutdown
* Direct access to constants

---

## 🔹 Structure

```text
jarengine/
├── __init__.py
├── constants.py
├── Entities/
├── Events/
├── Games/
├── Interns/
├── Resources/
└── Systems/
````

| File           | Description                                           |
|----------------|-------------------------------------------------------|
| `__init__.py`  | Public module exports.                                |
| `constants.py` | JarEngine constants (Booléan, Keys, Events, Versions) |

---

## 🔹 Main Modules

| Class       | Description                                |
|-------------|--------------------------------------------|
| `Entities`  | ECS Entity manager                         |
| `Events`    | Events handler and manager                 |
| `Games`     | Game, Window, ECS System and Input manager |
| `Interns`   | Internal API (use carefully)               |
| `Resources` | Game resources handler                     |
| `Systems`   | Logic, Math, Tools classes                 |

Each module has its own documentation page.

## 🔹 Important Notes

Common mistakes:

* This is not PyGame but a wrapper, do not apply its API to JarEngine.
* Not initializing JarEngine doesn't initialize subsystems such as pygame, config files, and other outside libraries.

---

## 🔹 Dependencies

Uses:

* `pygame`
* `jarbin-toolkit-console`
* `jarbin-toolkit-time`
* `jarbin-toolkit-error`

---
