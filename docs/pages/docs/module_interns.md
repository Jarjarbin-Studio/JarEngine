---
layout: page
title: JarEngine - Module - Interns
sidebar: sidebar
permalink: /module_interns.html
---

# 📦 Interns

> Overview of the `Interns` module in JarEngine.

---

## 🔹 Overview

`Interns` provides the internal core classes and utilities used by JarEngine architecture.

It includes:
* Base classes
* Internal engine structures
* Configuration handling
* Core decorators

---

## 🔹 Contents

| Class                               | Description                                           |
|-------------------------------------|-------------------------------------------------------|
| [`•>JEInternBaseClass<•`]()📎       | Base class inherited by JarEngine classes             |
| [`•>JEInternConfig<•`]()📎          | Internal configuration manager                        |
| [`•>JEInternEmptyComponent<•`]()📎  | Placeholder component for entities without components |
| [`•>JEInternResources<•`]()📎       | Resource holder and manager                           |
| [`•>JEInternWindowSettings<•`]()📎  | Window settings storage                               |
| [`•>JEInternOwnership<•`]()📎       | Parent and child ownership handling                   |
| [`•>JEInternEntityComponent<•`]()📎 | Base class for entity components                      |
| [`•>JEInternSystems<•`]()📎         | Base class for entity systems                         |
| [`•>JEInternGraphic<•`]()📎         | Base class for graphical objects                      |
| [`•>JEInternGraphicalObject<•`]()📎 | Base class for drawable objects                       |
| [`•>JEInternResource<•`]()📎        | Base class for engine resources                       |

---

## 🔹 Usage

```python
from jarengine import Interns

# Internals are normally managed automatically by JarEngine.

config = Interns.Config.get_config("my_config")

config.set("MY_SECTION", "my_option", True)

if config.get_bool("MY_SECTION", "my_option"):
    print("my_option toggled")
```

The module exposes internal engine structures for advanced usage and extension.

---

## 🔹 Notes

Useful information:

* This module is intended for advanced users and engine extensions.
* Most classes should not be instantiated manually.
* Use internal classes carefully as they directly interact with JarEngine core systems.

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
