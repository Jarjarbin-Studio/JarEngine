---
layout: page
title: Module - Systems | Class - JEColor
sidebar: sidebar
permalink: /JEColor.html
---

# 📦 JEColor

> Technical reference for the `JEColor` of JarEngine.

---

## 🔹 Overview

**`JEColor` is a JarEngine class responsible for representing and manipulating RGBA color values inside the `systems` module.**

It provides:

* RGBA color storage
* Channel-level access and mutation
* Tuple-based export formats (RGB / RGBA)
* Iteration support over channels

---

## 🔹 Purpose

The purpose of `JEColor` is to:

* Provide a unified color representation for rendering systems
* Allow direct manipulation of individual color channels
* Offer lightweight conversion to common graphics formats

It is **not** a rendering object, but a **low-level color data container used by rendering and UI systems**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── systems
│     ├── color.py
│     │     └── JEColor
└── ...
```

Explain where the class fits in the engine.

`JEColor` is part of the rendering data layer and is used by graphical components to define visual appearance.

---

## 🔹 Class Relationships

### Uses

* [`JEInternBaseClass`](JEInternBaseClass.md)📎

---

## 🔹 Data Model

| Field    | Type        | Description                          |
|----------|-------------|--------------------------------------|
| `_color` | `list[int]` | Internal RGBA storage `[r, g, b, a]` |

---

## 🔹 Public API

### Constructor

| Signature             | Description                               |
|-----------------------|-------------------------------------------|
| `JEColor(r, g, b, a)` | Creates a color object with RGBA channels |

---

### Accessors

| Method | Returns                     | Description        |
|--------|-----------------------------|--------------------|
| `rgb`  | `tuple[int, int, int]`      | Returns RGB tuple  |
| `rgba` | `tuple[int, int, int, int]` | Returns RGBA tuple |

---

### Mutators

| Method | Description        |
|--------|--------------------|
| `r`    | Sets red channel   |
| `g`    | Sets green channel |
| `b`    | Sets blue channel  |
| `a`    | Sets alpha channel |

---

### Core Methods

| Method       | Description                 |
|--------------|-----------------------------|
| `__iter__()` | Iterates over RGBA channels |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Initialization (RGBA storage setup)
   │
   ▼
Runtime Usage (channel updates / reads)
   │
   ▼
Used by rendering systems
   │
   ▼
Destruction
```

Describe each stage in detail.

`JEColor` is typically created during entity/component initialization and remains stable during rendering cycles, with occasional channel updates.

---

## 🔹 Internal Behavior

`JEColor` stores color as a mutable list of four integers:

* Index 0 → Red
* Index 1 → Green
* Index 2 → Blue
* Index 3 → Alpha

Key behaviors:

* Properties provide controlled access to each channel
* Updates directly modify internal list (no copy overhead)
* `rgb` and `rgba` expose immutable tuple views
* Iteration returns sequential channel values

This design prioritizes:

* low overhead in rendering loops
* direct memory-like access pattern
* simplicity over safety constraints

---

## 🔹 Execution Flow

```text
Property Access (e.g. r)
   │
   ▼
Read/Write _color[index]
   │
   ▼
Return or mutate value
```

For RGB/RGBA:

```text
rgb / rgba call
   │
   ▼
Slice internal array
   │
   ▼
Return tuple copy
```

---

## 🔹 Usage

### Basic Example

```python
color = JEColor(255, 0, 0, 255)

print(color.r)   # 255
color.g = 128
```

---

### Realistic Example

```python
player_color = JEColor(0, 200, 255, 255)

if player.health < 50:
    player_color.r = 255  # indicate damage state
```

---

## 🔹 Design Decisions

* Mutable list chosen for fast channel access
* Property-based API for controlled mutation
* Tuple exports prevent accidental modification
* Lightweight design for rendering hot-path usage
* Avoids object-heavy RGBA abstractions

---

## 🔹 Performance Notes

* O(1) access for all channels
* No allocations for individual channel updates
* Tuple conversion adds minimal overhead
* Optimized for frequent read/write in render loops

---

## 🔹 Thread Safety

```text
Thread-safe: No
```

Notes:

* Internal state is mutable
* Concurrent writes may cause race conditions
* Intended for single-threaded game loop usage

---

## 🔹 Limitations

* No color validation (values not clamped)
* No color space conversion (RGB only)
* No immutability protection
* Alpha channel always present even if unused

---

## 🔹 Edge Cases

* Values outside 0–255 are accepted (no enforcement)
* Iteration exposes raw internal state
* Direct mutation bypasses validation layer (none exists)

---

## 🔹 Current State

⚠️ Stable low-level color representation system.

### Implemented

* RGBA storage system
* Channel getters/setters
* RGB/RGBA export
* Iteration support
* Deep copy support

### Planned

* Value clamping (0–255 enforcement)
* Color math utilities (blend, lerp)
* HSV/HSL support
* Immutable color variant

---

## 🔹 Debugging

* Use `dump()` to inspect internal `_color` list
* Check channel values via properties (`r`, `g`, `b`, `a`)
* Verify rendering output using `rgba` export
* Watch for invalid high-range values (no safety clamp)

---

## 🔹 Related Classes

* [`JEInternBaseClass`](JEInternBaseClass.md)📎
* [`JEContainer`](JEContainer.md)📎
* [`JEEntity`](JEEntity.md)📎
* [`JEGame`](JEGame.md)📎

---

## 🔹 Notes

`JEColor` is designed as a **minimal overhead rendering primitive**.

It prioritizes performance and simplicity over safety, making it suitable for real-time rendering pipelines inside JarEngine.
