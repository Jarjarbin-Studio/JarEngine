---
layout: page
title: Module - Interns | Module - FinalClasses | Class - JEInternWindowSettings
sidebar: sidebar
permalink: /JEInternWindowSettings.html
---

# 📦 JEInternWindowSettings

> Technical reference for the JEInternWindowSettings of JarEngine.

---

## 🔹 Overview

**JEInternWindowSettings is a JarEngine class responsible for storing and managing all configuration parameters required to initialize and control the game window inside the Window System module.**

It provides:

* Window resolution management
* Rendering configuration flags
* Frame rate configuration
* Display and depth settings
* Runtime window metadata (title, vsync)

---

## 🔹 Purpose

The purpose of JEInternWindowSettings is to:

* Centralize all window configuration in a single structure
* Provide controlled access to rendering and display parameters
* Allow safe modification of runtime window properties
* Standardize initialization data for window creation systems

It is **not** a rendering engine, but a **configuration container for window initialization and runtime settings**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── Games
│     ├── Window System
│     │     └── JEInternWindowSettings
│     ├── Window
│     └── Game Loop
└── ...
````

JEInternWindowSettings is used during engine startup to configure the window and may be queried at runtime by rendering and display systems.

---

## 🔹 Class Relationships

### Uses

* None (pure data/config class)

---

## 🔹 Data Model

| Field      | Type             | Description                          |
|------------|------------------|--------------------------------------|
| `_size`    | `tuple[int,int]` | Window resolution                    |
| `_flags`   | `int`            | Backend/window creation flags        |
| `_fps`     | `int`            | Target frames per second             |
| `_depth`   | `int`            | Color/depth buffer configuration     |
| `_display` | `int`            | Display index (multi-monitor setups) |
| `_vsync`   | `int`            | Vertical sync enable/disable flag    |
| `_title`   | `str`            | Window title                         |

---

## 🔹 Public API

### Constructor

| Signature                                                                                    |
|----------------------------------------------------------------------------------------------|
| `__init__(size=(0,0), flags=0, fps=60, depth=0, display=0, vsync=0, title="JarEngine Game")` |

Initializes a complete window configuration object with default or user-defined parameters.

---

### Accessors

| Method      | Returns          | Description             |
|-------------|------------------|-------------------------|
| `size()`    | `tuple[int,int]` | Get window size         |
| `flags()`   | `int`            | Get window flags        |
| `fps()`     | `int`            | Get target FPS          |
| `depth()`   | `int`            | Get depth configuration |
| `display()` | `int`            | Get display index       |
| `vsync()`   | `int`            | Get vsync state         |
| `title()`   | `str`            | Get window title        |

---

### Mutators

| Method        | Description           |
|---------------|-----------------------|
| `size = ...`  | Set window resolution |
| `fps = ...`   | Set target frame rate |
| `title = ...` | Set window title      |

---

### Core Methods

None (this class is purely a configuration container).

---

### Utility Methods

| Method           | Description                 |
|------------------|-----------------------------|
| `__deepcopy__()` | Returns self (no deep copy) |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Initialization (default or custom settings)
   │
   ▼
Consumed by window creation system
   │
   ▼
Runtime read-only usage (mostly)
   │
   ▼
Engine shutdown
```

This object is typically created once at engine startup and passed to the window system.

---

## 🔹 Internal Behavior

JEInternWindowSettings stores raw configuration values without performing validation or transformation.

Key behaviors:

* Direct attribute storage
* Minimal logic overhead
* Some properties are mutable (size, fps, title)
* Others remain effectively static after initialization (flags, depth, display, vsync)

---

## 🔹 Execution Flow

```text
Engine Startup
   │
   ▼
Create JEInternWindowSettings
   │
   ▼
Window System reads configuration
   │
   ▼
Initialize graphical context (Pygame backend)
   │
   ▼
Game loop uses FPS / vsync settings
```

---

## 🔹 Usage

### Basic Example

```python
settings = JEInternWindowSettings(
    size=(1280, 720),
    fps=60,
    title="My Game"
)

settings.fps = 144
settings.title = "Updated Game Title"
```

---

### Realistic Example

```python
settings = JEInternWindowSettings(
    size=(1920, 1080),
    flags=0,
    fps=60,
    depth=32,
    display=0,
    vsync=1,
    title="JarEngine Project"
)

window = JEWindow(settings)
```

---

## 🔹 Design Decisions

* Centralized configuration avoids scattered window parameters
* Mutable subset (size, fps, title) allows runtime adjustments
* Immutable-like fields ensure stable rendering backend configuration
* Lightweight design avoids overhead during engine startup

---

## 🔹 Performance Notes

* Time complexity: O(1) for all operations
* Memory usage: constant and minimal
* No allocations after initialization
* Ideal for hot-path safe access during runtime

---

## 🔹 Thread Safety

```text
Thread-safe: No

Notes:
- Direct attribute mutation is not protected
- Should only be modified on main thread (engine thread)
```

---

## 🔹 Limitations

* No validation of input values (e.g., negative FPS possible)
* No automatic synchronization with window system after modification
* No event-based update propagation

---

## 🔹 Edge Cases

* Changing `size` at runtime may not update actual window unless explicitly handled by window system
* Invalid FPS values may break frame limiter logic
* Missing or unsupported flags depend on backend (Pygame layer)

---

## 🔹 Current State

⚠️ Implementation status.

### Implemented

* Full configuration structure
* Property-based accessors
* Mutable core settings

### Planned

* Validation layer
* Live window update propagation
* Preset configurations (low/medium/high performance)

---

## 🔹 Debugging

* Inspect settings before window initialization
* Print values when rendering issues occur
* Verify FPS and vsync consistency
* Check resolution mismatches during fullscreen mode

---

## 🔹 Related Classes

* [`JEWindow`](JEWindow.md)📎
* [`JEGame`](JEGame.md)📎
* [`JEContainer`](JEContainer.md)📎
* [`JETexture`](JETexture.md)📎

---

## 🔹 Notes

This class is intentionally minimal and acts as a configuration contract between the engine core and the windowing backend.
