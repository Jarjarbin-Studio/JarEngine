---
layout: page
title: JarEngine - Main
sidebar: sidebar
permalink: /module_main.html
---

# 📦 JarEngine

> Overview of the main module in JarEngine.

---

## 🔹 Overview

`JarEngine` provides the main entry point and access to all engine modules.

It includes:
* Engine initialization
* Engine shutdown
* Access to engine modules and constants

---

## 🔹 Contents

| Modules               | Description                     |
|-----------------------|---------------------------------|
| [`•>Entities<•`]()📎  | Entity and component management |
| [`•>Events<•`]()📎    | Event handling system           |
| [`•>Games<•`]()📎     | Game runtime management         |
| [`•>Interns<•`]()📎   | Internal engine structures      |
| [`•>Resources<•`]()📎 | Resource management             |
| [`•>Systems<•`]()📎   | Core utility systems            |

---

## 🔹 Usage

```python
import jarengine

jarengine.init()

# Use JarEngine modules here

jarengine.quit()
```

The main module initializes the engine environment and provides access to its different modules.

---

## 🔹 Notes

Useful information:

* JarEngine is a wrapper and abstraction layer over PyGame, not PyGame itself.
* Initialization must be done before using engine features.
* Internal modules should be used carefully.

---
