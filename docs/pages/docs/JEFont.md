---
layout: page
title: Module - Resources | Class - JEFont
sidebar: sidebar
permalink: /JEFont.html
---

# 📦 JEFont

> Technical reference for the `JEFont` of JarEngine.

---

## 🔹 Overview

**`JEFont` is a JarEngine class responsible for loading and managing font resources inside the `resources` module.**

It provides:

* Font file loading through Pygame backend
* Centralized font resource abstraction
* Size-based font instantiation

---

## 🔹 Purpose

The purpose of `JEFont` is to:

* Load font assets from file system or engine assets directory
* Provide a unified wrapper over Pygame font handling
* Expose font resource with controlled access

It is **not** a rendering system, but a **font resource container and loader abstraction**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── resources
│     ├── ...
│     ├── JEFont
│     └── ...
└── ...
```

`JEFont` is a low-level resource class used by rendering systems and UI systems to provide text rendering capabilities.

---

## 🔹 Class Relationships

### Uses

* `PGExtern.font.Font`
* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEInternOwnership`](JEInternOwnership.md)📎

---

## 🔹 Data Model

| Field       | Type   | Description                        |
|-------------|--------|------------------------------------|
| `_path`     | `str`  | Resolved font file path            |
| `_font`     | `Font` | Pygame font instance               |
| `_size`     | `int`  | Font size in pixels/points         |
| `base_path` | `str`  | Default assets font directory path |

---

## 🔹 Public API

### Constructor

| Signature                    | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `__init__(name, path, size)` | Loads a font resource from a file path and initializes it with a given size |

---

### Accessors

| Method | Returns | Description                             |
|--------|---------|-----------------------------------------|
| `font` | `Font`  | Returns underlying Pygame font instance |
| `path` | `str`   | Returns resolved font file path         |
| `size` | `int`   | Returns font size                       |

---

### Core Methods

| Method         | Description                              |
|----------------|------------------------------------------|
| `__deepcopy__` | Returns the same font instance reference |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Path resolution
   │
   ▼
Font loading (Pygame)
   │
   ▼
Runtime usage by render/UI systems
   │
   ▼
Destruction (engine-managed)
```

A font is typically created once at resource loading time and reused throughout rendering operations.

---

## 🔹 Internal Behavior

`JEFont` resolves the font path and delegates loading to Pygame.

Key behaviors:

* If the provided path is not absolute or does not contain a directory separator, it is resolved using `base_path`
* The font is immediately loaded into a `PGExtern.font.Font` object
* The class does not perform caching itself; it assumes external resource management
* Deep copy returns the same instance to avoid duplicate font loading overhead

---

## 🔹 Execution Flow

```text
Constructor call
   │
   ▼
Path normalization
   │
   ▼
Pygame Font creation
   │
   ▼
Store internal references
   │
   ▼
Ready for rendering usage
```

---

## 🔹 Usage

### Basic Example

```python
font = JEFont("default", "arial.ttf", 16)

text_font = font.font
print(font.size)
```

---

### Realistic Example

```python
ui_label_font = JEFont("ui_label", "ui/font.ttf", 24)

text_surface = ui_label_font.font.render("Hello", True, (255, 255, 255))
```

---

## 🔹 Design Decisions

* Wrapper over Pygame font to isolate engine dependency
* Centralized font resolution through `base_path`
* Immutable behavior in deep copy to prevent redundant resource allocation
* Separation between resource identity (`JEFont`) and rendering usage (`Font`)

---

## 🔹 Performance Notes

* Font loading is expensive (I/O + rasterization initialization)
* Intended to be loaded once and reused
* Deepcopy avoids duplication cost by returning same instance
* No runtime allocation during accessors

---

## 🔹 Thread Safety

Thread-safe: No

Notes:

* Font loading is not synchronized
* Resource access is safe only in single-threaded engine context

---

## 🔹 Limitations

* No dynamic font reloading
* No runtime size scaling after creation
* Deepcopy does not produce independent instance
* Relies directly on Pygame font backend

---

## 🔹 Edge Cases

* Invalid font path will raise backend error during initialization
* Missing file in `base_path` resolution will fail at load time
* Extremely large font sizes may degrade performance or fail depending on backend

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* Font loading from path
* Automatic base path resolution
* Access to underlying font object
* Size storage

### Planned

* Font caching system
* Shared resource registry integration
* Dynamic font scaling support
* Hot-reload for development mode

---

## 🔹 Debugging

* Use `path` property to verify resolution correctness
* Validate font loading by checking `font` existence
* Check rendering output in UI system if text is missing or corrupted

---

## 🔹 Related Classes

* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEInternOwnership`](JEInternOwnership.md)📎

---

## 🔹 Notes

This class is intentionally lightweight and acts as a bridge between engine resource management and Pygame’s font system.
