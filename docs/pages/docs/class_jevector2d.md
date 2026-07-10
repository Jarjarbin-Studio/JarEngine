---
layout: page
title: JarEngine - Class - JEVector2D
sidebar: sidebar
permalink: /class_jevector2d.html
---

# 📦 JEVector2D

> Technical reference for the `JEVector2D` class of JarEngine.

> Inherit from [`•>JEInternTransform<•`]()📎

---

## 🔹 Overview

**`JEVector2D` is a JarEngine class responsible for specialized float storing.**

It provides:

* x and y float storage.
* Transformation helpers (through inheritance).

---

## 🔹 Purpose

The purpose of this class is to:

* Store 2 values.
* Transform them though helpers.

---

## 🔹 Location in JarEngine

```text
JarEngine
│
├── Systems
│     └── JEVector2D
│
└── ...
```

JEVector is used everywhere in JarEngine.

---

## 🔹 Data

Internal data stored by this class.

| Field    | Type          | Description   | Public? |
|----------|---------------|---------------|:-------:|
| `vector` | `list[float]` | Value storage |  False  |
| `x`      | `float`       | Value storage |  True   |
| `y`      | `float`       | Value storage |  True   |

---

## 🔹 Functions / API

List all public functions available.

| Function                         | Arguments                          | Returns           | Description              |
|----------------------------------|------------------------------------|-------------------|--------------------------|
| [•>`__init__(...)`<•](#__iter__) | `x: float = 0.0`, `y: float = 0.0` |                   | JEVector2D creator.      |
| [•>`__iter__(...)`<•](#__iter__) |                                    | `Iterator[float]` | Iterate over the vector. |

---

### Argument Details

Additional details for complex functions.

#### __iter__

| Argument | Type   | Description                  |
|----------|--------|------------------------------|
| `arg1`   | `type` | Description of the argument. |
| `arg2`   | `type` | Description of the argument. |

**Returns:**

| Type   | Description                    |
|--------|--------------------------------|
| `type` | Description of returned value. |

---

## 🔹 Usage

### Basic Example

```python
# Minimal usage example
```

---

### Typical Workflow

```python
# Realistic usage example
```

---

## 🔹 Internal Behavior

Explain how the class works internally.

Include:

* state management
* interactions with other classes
* important processing steps

---

## 🔹 Performance Notes

Describe important performance information:

* execution cost
* memory usage
* allocations
* optimization details

---

## 🔹 Limitations

Current constraints:

* ...
* ...
* ...

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* ...
* ...

### Planned

* ...
* ...

---

## 🔹 Debugging

Useful debugging methods:

* `dump()`
* `debug()`
* logs
* common errors

---

## 🔹 Related Classes

* [`•>...<•`]()📎
* [`•>...<•`]()📎
* [`•>...<•`]()📎

---
