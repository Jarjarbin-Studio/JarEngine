---
layout: page
title: Module - Resources
sidebar: sidebar
permalink: /Resources.html
---

# 📦 Resources Module

> Technical reference for the `resources` module of JarEngine.

---

## 🔹 Overview

**`resources` is a JarEngine module responsible for managing graphical and textual assets used by the engine.**

It provides the classes and utilities required to:

* Load and manage textures
* Handle font resources
* Expose reusable rendering assets across the engine

---

## 🔹 Purpose

The `resources` module aims to centralize asset handling to ensure consistent loading, reuse, and lifecycle management of graphical and text resources.

It is **not** a rendering system itself, but a **resource management layer** used by higher-level systems.

---

## 🔹 Module Organization

```text
sources/
└── resources/
    ├── __init__.py
    ├── texture.py
    └── font.py
```

| File           | Description            |
|----------------|------------------------|
| `__init__.py`  | Public module exports  |
| `texture.py`   | Texture resource class |
| `font.py`      | Font resource class    |

---

## 🔹 Responsibilities

| Responsibility     | Description                               |
|--------------------|-------------------------------------------|
| Texture management | Loading and storing image-based resources |
| Font management    | Loading and providing font assets         |

---

## 🔹 Public Classes

| Class       | Description                  |
|-------------|------------------------------|
| `JETexture` | Texture resource abstraction |
| `JEFont`    | Font resource abstraction    |

Each class should have its own dedicated documentation page.

---

## 🔹 Dependencies

### Depends On

* `pygame` (implicit dependency through rendering backend)
* Internal engine resource system (via `sources.resources`)

---

## 🔹 Data Flow

```text
File Path / Asset Input
        │
        ▼
   Resource Loader
        │
        ├── JETexture
        ├── JEFont
        │
        ▼
   Engine Rendering / Text Systems
```

---

## 🔹 Usage

### Basic Example

```python
from sources.resources import JETexture, JEFont

texture = JETexture("assets/sprite.png")
font = JEFont("assets/font.ttf", size=16)
```

---

### Typical Workflow

```python
# Load resources at initialization
texture = JETexture("player.png")

# Use later in rendering system
sprite.set_texture(texture)
```

Step 1: Load asset from disk
Step 2: Store resource instance
Step 3: Reuse across engine systems
Step 4: Dispose when no longer needed

---

## 🔹 Design Decisions

* Centralized resource abstraction layer
* Separation between texture and font domains
* Minimal direct coupling with rendering systems
* Designed for reuse and caching potential
* Stub support for type safety (`.pyi` files)

---

## 🔹 Performance Notes

* Time complexity:

  * Loading: O(n) with respect to asset size
  * Access: O(1) after loading (reference-based reuse)

* Memory usage:

  * Stores GPU/CPU-backed assets depending on backend

* Cache behavior:

  * Intended to support reuse of loaded resources
  * Avoids redundant loading when reused properly

* Allocation notes:

  * Resource loading may trigger external library allocations (e.g., pygame surfaces)

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Resource loading is not synchronized
- Concurrent loading may cause race conditions if accessed in parallel
- Should be used in main thread or controlled loading phase
```

---

## 🔹 Limitations

* No built-in async loading system
* No automatic caching layer defined in this module
* Depends on external backend behavior for memory management
* No runtime hot-reloading support

---

## 🔹 Edge Cases

* Invalid file paths → resource load failure
* Unsupported font formats → backend exception
* Corrupted image files → undefined behavior depending on backend
* Missing assets → runtime errors unless handled externally

---

## 🔹 Current State

### Implemented

* Texture resource wrapper (`JETexture`)
* Font resource wrapper (`JEFont`)
* Module-level exports

### Planned

* Resource caching system
* Async loading pipeline
* Asset registry / manager
* Hot-reload support for development

---

## 🔹 Debugging

* `dump()` usage:

  * Not directly defined in this module, relies on base engine objects if wrapped

* `debug()` usage:

  * Use engine-level debug tools to inspect loaded resource objects

* Failure signals:

  * FileNotFoundError for missing assets
  * Backend-specific loading errors (pygame exceptions)

---

## 🔹 Related Classes

* [`Games`](Games.md)📎
* [`Systems`](Systems.md)📎
* [`Entities`](Entities.md)📎

---

## 🔹 Notes

This module is designed as a lightweight abstraction layer over backend asset handling. It intentionally avoids complex lifecycle or caching logic to keep resource management predictable and engine-neutral.
