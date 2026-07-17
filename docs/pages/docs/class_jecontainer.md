---
layout: page
title: JarEngine - Class - JEContainer
sidebar: sidebar
permalink: /class_jecontainer.html
---

# 📦 JEContainer

> Technical reference for the `JEContainer` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEContainer` is responsible for storing and managing groups of JarEngine objects.**

Provides:
* Object storage with type checking
* Object searching and retrieval
* Safe object removal and iteration

It is used internally by JarEngine for managing entities, resources, systems and other grouped objects.

---

## 🔹 Location

```text
JarEngine
│
├── Systems
│     └── JEContainer
│
└── ...
```

---

## 🔹 Data

|      Field       |      Type      | Description                            | Property? | Can be set? |
|:----------------:|:--------------:|----------------------------------------|:---------:|:-----------:|
|      `data`      | `dict[str, T]` | Raw stored objects                     |   True    |    False    |

---

## 🔹 API

|    Function     |                           Arguments                            |    Returns    | Description                       |
|:---------------:|:--------------------------------------------------------------:|:-------------:|-----------------------------------|
|  `__init__()`   |        `allowed_type: Type[T], allow_subclass: JEBool`         |               | Creates a typed container         |
|     `add()`     |                            `obj: T`                            |               | Adds an object to the container   |
| `__getitem__()` |                   `value: str \| T \| Type`                    |      `T`      | Retrieves an object automatically |
|     `get()`     | `name: str, jeid: str, instance: T, _type: Type, default: Any` |      `T`      | Searches and returns an object    |
|     `rm()`      |        `name: str, jeid: str, instance: T, _type: Type`        |      `T`      | Removes and returns an object     |
|    `clear()`    |                                                                |               | Removes all objects               |
|  `__iter__()`   |                                                                | `Iterator[T]` | Iterates through stored objects   |

---

## 🔹 Usage

```python
from jarengine import Systems, Entity

# Create a container dedicated to entities
entities = Systems.JEContainer(
    Entity.JEEntity
)

# Create entities
player = Entity.JEEntity(name="Player")
enemy = Entity.JEEntity(name="Enemy")

# Store objects
entities.add(player)
entities.add(enemy)

# Retrieve an object by JEID
found = entities.get(
    jeid=player.jeid
)

# Retrieve an object by name
enemy_found = entities.get(
    name="Enemy"
)

# Iterate through stored objects
for entity in entities:
    print(entity)
```

---

## 🔹 Related

* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
