---
layout: page
title: JarEngine - Class - JEImmutable
sidebar: sidebar
permalink: /class_jeimmutable.html
---

# 📦 JEImmutable

> Technical reference for the `JEImmutable` class of JarEngine.

> Inherit from [`•>JEInternBaseClass<•`]()📎

---

## 🔹 Overview

**`JEImmutable` is responsible for creating frozen copies of objects that cannot be modified directly.**

Provides:
* Immutable object storage
* Automatic object freezing and restoration
* Collection-like access helpers

It is used to safely store configuration data and protected values while keeping access to the original data type when possible.

---

## 🔹 Location

```text
JarEngine
│
├── Systems
│     └── JEImmutable
│
└── ...
```

---

## 🔹 Data

|  Field   |   Type    | Description                                  | Property? | Can be set? |
|:--------:|:---------:|----------------------------------------------|:---------:|:-----------:|
|  `type`  | `Type[T]` | Original type of the stored object           |   True    |    False    |
| `frozen` |   `Any`   | Frozen internal representation of the object |   True    |    False    |
|  `data`  |    `T`    | Unfrozen copy of the stored object           |   True    |    False    |

---

## 🔹 API

The original type must handle these functions to work.

|     Function     |        Arguments         |     Returns      | Description                            |
|:----------------:|:------------------------:|:----------------:|----------------------------------------|
|   `__init__()`   |        `value: T`        |                  | Creates an immutable copy of an object |
|   `__str__()`    |                          |      `str`       | Returns the string representation      |
|   `__repr__()`   |                          |      `str`       | Returns the debug representation       |
|   `__iter__()`   |                          | `Iterator[Any]`  | Iterates through the object            |
|   `__len__()`    |                          |      `int`       | Gets object length                     |
| `__getitem__()`  |       `item: Any`        |      `Any`       | Gets an item from the object           |
| `__contains__()` |       `item: Any`        |     `JEBool`     | Checks if an item exists               |
|   `__bool__()`   |                          |      `bool`      | Gets boolean state                     |
| `__reversed__()` |                          | `Iterator[Any]`  | Iterates in reverse order              |
|     `map()`      |     `func: Callable`     |   `list[Any]`    | Applies a function to elements         |
|    `filter()`    |     `func: Callable`     |   `list[Any]`    | Filters elements                       |
|     `any()`      |                          |     `JEBool`     | Checks if any element is true          |
|     `all()`      |                          |     `JEBool`     | Checks if all elements are true        |
|    `count()`     |       `value: Any`       |      `int`       | Counts value occurrences               |
|    `index()`     |       `value: Any`       |      `int`       | Gets value index                       |
|     `keys()`     |                          |    `KeysView`    | Gets dictionary keys                   |
|    `values()`    |                          |   `ValuesView`   | Gets dictionary values                 |
|    `items()`     |                          |   `ItemsView`    | Gets dictionary items                  |
|     `get()`      | `key: Any, default: Any` |      `Any`       | Gets dictionary value                  |
|   `__list__()`   |                          |   `list[Any]`    | Converts to list                       |
|   `to_dict()`    |                          | `dict[Any, Any]` | Converts to dictionary                 |
|    `clone()`     |                          | `JEImmutable[T]` | Creates an immutable copy              |
|    `__eq__()`    |       `other: Any`       |     `JEBool`     | Compares two objects                   |

---

## 🔹 Usage

```python
from jarengine import Systems

# Create immutable configuration data
settings = Systems.JEImmutable(
    {
        "width": 1280,
        "height": 720,
        "fullscreen": False
    }
)

# Access data safely
print(settings.data)

# Dictionary-like access
print(settings["width"])

# Create another immutable copy
backup = settings.clone()

print(backup)
```

---
