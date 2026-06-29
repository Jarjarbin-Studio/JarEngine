---
layout: page
title: Module - Interns | Module - FinalClasses | Class - JEInternRessources
sidebar: sidebar
permalink: /JEInternRessources.html
---

# 📦 JEInternRessources

> Technical reference for the JEInternRessources of JarEngine.

---

## 🔹 Overview

**JEInternRessources is a JarEngine class responsible for managing all loaded engine resources (textures, animations, fonts) inside the Resource Management module.**

It provides:

* Centralized storage for textures
* Centralized storage for animations
* Centralized storage for fonts

---

## 🔹 Purpose

The purpose of JEInternRessources is to:

* Provide a unified access point for graphical and textual assets
* Avoid duplicate loading of resources
* Organize engine-level assets in structured containers

It is **not** a rendering system, but a **resource manager and registry**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── Intern
│     ├── Resources
│     │     └── JEInternRessources
│     ├── Graphics
│     └── Systems
└── ...
```

JEInternRessources sits at the engine core level and is accessed by rendering systems, entities, and UI components to retrieve shared assets.

---

## 🔹 Class Relationships

### Uses

* [`JEContainer`](JEContainer.md)📎
* [`JETexture`](JETexture.md)📎
* [`JEFont`](JEFont.md)📎
* [`JEInternGraphic`](JEInternGraphic.md)📎

---

## 🔹 Data Model

| Field         | Type                           | Description                       |
|---------------|--------------------------------|-----------------------------------|
| `_textures`   | `JEContainer[JETexture]`       | Stores all loaded textures        |
| `_animations` | `JEContainer[JEInternGraphic]` | Stores animation-related graphics |
| `_font`       | `JEContainer[JEFont]`          | Stores loaded font assets         |

---

## 🔹 Public API

### Constructor

| Signature    | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `__init__()` | Initializes empty resource containers for textures, animations, and fonts |

---

### Accessors

| Method         | Returns                        | Description                |
|----------------|--------------------------------|----------------------------|
| `texture()`    | `JEContainer[JETexture]`       | Access texture container   |
| `animations()` | `JEContainer[JEInternGraphic]` | Access animation container |
| `font()`       | `JEContainer[JEFont]`          | Access font container      |

---

### Core Methods

None (this class is strictly a storage/registry container).

---

### Utility Methods

None

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Initialization (empty containers created)
   │
   ▼
Runtime Usage (resources added/retrieved)
   │
   ▼
Persistent Storage (shared across engine lifetime)
   │
   ▼
Destruction (engine shutdown)
```

The class is typically instantiated once and persists for the entire engine runtime.

---

## 🔹 Internal Behavior

JEInternRessources acts as a centralized registry. It does not load assets directly but stores references to already created resource objects.

Key behaviors:

* Containers are initialized empty
* Resources are expected to be added externally
* No automatic lifecycle management of assets
* Acts as a shared cache layer across engine systems

---

## 🔹 Execution Flow

```text
Request Resource
   │
   ▼
Access Container (texture / animation / font)
   │
   ▼
Retrieve stored asset
   │
   ▼
Return reference
```

No processing is performed internally; all logic is delegated to container operations.

---

## 🔹 Usage

### Basic Example

```python
resources = JEInternRessources()

texture = JETexture("player", "player.png")
resources.texture.add(texture)
```

---

### Realistic Example

```python
resources = JEInternRessources()

player_texture = JETexture("player", "assets/player.png")
enemy_texture = JETexture("enemy", "assets/enemy.png")

resources.texture.add(player_texture)
resources.texture.add(enemy_texture)

sprite.set_texture(resources.texture.get(name="player"))
```

---

## 🔹 Design Decisions

* Centralized resource registry avoids duplicated asset loading
* Separation between resource storage and resource loading logic
* Container-based design ensures extensibility (textures, fonts, animations)
* Lightweight structure to keep engine initialization fast

---

## 🔹 Performance Notes

* Time complexity: O(1) for container access (expected)
* Memory usage: depends on loaded assets
* Cache-friendly due to centralized access pattern
* No runtime processing overhead inside this class

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Containers are not protected against concurrent modifications
- External synchronization required if used in multithreaded context
```

---

## 🔹 Limitations

* Does not handle asset loading or decoding
* No automatic deduplication guarantees unless enforced by containers
* No reference counting or memory management

---

## 🔹 Edge Cases

* Accessing empty containers returns null or equivalent
* Missing resource keys must be handled externally
* Invalid asset insertion depends on JEContainer implementation

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* Texture container
* Animation container
* Font container

### Planned

* Resource caching layer
* Automatic loader integration
* Reference tracking system

---

## 🔹 Debugging

* Use container inspection to list stored assets
* Verify correct registration of textures/fonts
* Check missing keys when rendering fails
* Validate asset paths during creation phase

---

## 🔹 Related Classes

* [`JEContainer`](JEContainer.md)📎
* [`JETexture`](JETexture.md)📎
* [`JEFont`](JEFont.md)📎
* [`JEInternGraphic`](JEInternGraphic.md)📎

---

## 🔹 Notes

This class is intentionally minimal and acts as a structural anchor for the engine’s resource pipeline rather than an active processing system.
