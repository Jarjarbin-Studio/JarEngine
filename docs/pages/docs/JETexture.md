---
layout: page
title: Module - Resources | Class - JETexture
sidebar: sidebar
permalink: /JETexture.html
---

# 📦 JETexture

> Technical reference for the `JETexture` of JarEngine.

---

## 🔹 Overview

**`JETexture` is a JarEngine class responsible for loading and managing 2D image textures inside the `resources` module.**

It provides:

* Image loading from file system
* Automatic texture size extraction
* Pygame surface abstraction wrapper

---

## 🔹 Purpose

The purpose of `JETexture` is to:

* Load and store graphical textures used by rendering systems
* Provide a unified abstraction over Pygame image surfaces
* Expose texture metadata such as path and size

It is **not** a rendering system, but a **resource container for graphical surfaces**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── resources
│     ├── ...
│     ├── JETexture
│     └── ...
└── ...
```

`JETexture` is a low-level graphical resource used by rendering, sprite, and UI systems to display images.

---

## 🔹 Class Relationships

### Uses

* `PGExtern.image.load`
* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEInternOwnership`](JEInternOwnership.md)📎
* [`JEVector2D`](JEVector2D.md)📎

---

## 🔹 Data Model

| Field       | Type         | Description                      |
|-------------|--------------|----------------------------------|
| `_path`     | `str`        | Resolved texture file path       |
| `_surface`  | `Surface`    | Loaded Pygame surface            |
| `_size`     | `JEVector2D` | Width and height of texture      |
| `base_path` | `str`        | Default assets texture directory |

---

## 🔹 Public API

### Constructor

| Signature              | Description                                            |
|------------------------|--------------------------------------------------------|
| `__init__(name, path)` | Loads a texture from file and creates a Pygame surface |

---

### Accessors

| Method    | Returns      | Description                        |
|-----------|--------------|------------------------------------|
| `surface` | `Surface`    | Returns underlying Pygame surface  |
| `path`    | `str`        | Returns resolved texture file path |
| `size`    | `JEVector2D` | Returns texture dimensions         |

---

### Core Methods

| Method         | Description                                                   |
|----------------|---------------------------------------------------------------|
| `__deepcopy__` | Returns same instance (no duplication of GPU/resource memory) |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Path resolution
   │
   ▼
Image loading (Pygame Surface creation)
   │
   ▼
Size extraction
   │
   ▼
Runtime usage in rendering systems
   │
   ▼
Engine-managed destruction
```

A texture is typically loaded once at startup or scene initialization and reused throughout rendering cycles.

---

## 🔹 Internal Behavior

`JETexture` acts as a thin wrapper over Pygame image loading.

Key behaviors:

* If the path does not contain a directory separator, it is resolved using `base_path`
* Image is loaded immediately into a `Surface` with alpha support (`convert_alpha`)
* Size is extracted from the surface and stored as a `JEVector2D`
* Deep copy does not duplicate GPU memory; it returns the same instance

---

## 🔹 Execution Flow

```text
Constructor call
   │
   ▼
Path normalization
   │
   ▼
Pygame image load
   │
   ▼
Surface conversion (alpha enabled)
   │
   ▼
Size extraction
   │
   ▼
Ready for rendering usage
```

---

## 🔹 Usage

### Basic Example

```python
texture = JETexture("player", "player.png")

print(texture.path)
print(texture.size.x, texture.size.y)
```

---

### Realistic Example

```python
player_sprite = JETexture("player_idle", "sprites/player_idle.png")

screen.blit(player_sprite.surface, (100, 200))
```

---

## 🔹 Design Decisions

* Wrapper over Pygame Surface to isolate engine dependency
* Centralized asset path resolution through `base_path`
* Precomputed size stored as vector for fast access
* No duplication on deepcopy to avoid GPU memory overhead
* Designed as immutable runtime resource

---

## 🔹 Performance Notes

* Texture loading is expensive (disk I/O + GPU/Surface allocation)
* Must be cached externally to avoid repeated loads
* Accessors are O(1)
* No runtime allocations during read operations

---

## 🔹 Thread Safety

Thread-safe: No

Notes:

* Pygame surface operations are not thread-safe
* Resource loading must occur in main thread

---

## 🔹 Limitations

* No runtime texture modification support
* No automatic caching system inside class
* Deepcopy does not create independent instance
* Relies directly on Pygame image backend

---

## 🔹 Edge Cases

* Invalid path causes Pygame load exception
* Missing file results in runtime error during initialization
* Corrupted image data will fail surface conversion
* Large textures may impact memory and GPU usage

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* Texture loading from file
* Automatic path resolution
* Surface storage
* Size extraction via vector

### Planned

* Texture caching system
* Lazy loading support
* GPU texture batching integration
* Hot-reload for development mode

---

## 🔹 Debugging

* Verify `path` for correct asset resolution
* Check `surface` validity if rendering fails
* Inspect `size` for scaling issues
* Use rendering output validation in sprite/UI systems

---

## 🔹 Related Classes

* [`JEVector2D`](JEVector2D.md)📎
* [`JEInternGraphic`](JEInternGraphic.md)📎
* [`JEInternOwnership`](JEInternOwnership.md)📎

---

## 🔹 Notes

`JETexture` is designed to remain a lightweight immutable wrapper around a Pygame surface, with all heavy logic delegated to higher-level rendering systems.
