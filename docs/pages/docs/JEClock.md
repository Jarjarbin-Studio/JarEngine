---
layout: page
title: Module - Systems | Class - JEClock
sidebar: sidebar
permalink: /JEClock.html
---

# 📦 JEClock

> Technical reference for the `JEClock` of JarEngine.

---

## 🔹 Overview

**`JEClock` is a JarEngine class responsible for managing frame timing and delta-time computation inside the `systems` module.**

It provides:

* Delta time computation per frame
* Frame rate tracking (FPS)
* Frame limiting through target FPS control
* Integration with the engine update loop

---

## 🔹 Purpose

The purpose of `JEClock` is to:

* Provide consistent time-step information for the engine
* Ensure frame-rate controlled execution
* Enable delta-time based movement and simulation

It is **not** a generic timer utility, but a **core timing controller for the engine loop**.

---

## 🔹 Architecture Position

```text
JarEngine
│
├── systems
│     ├── clock.py
│     │     └── JEClock
└── ...
```

Explain where the class fits in the engine.

`JEClock` is part of the core runtime systems and is directly used by the game loop to regulate update timing.

---

## 🔹 Class Relationships

### Uses

* [`PGExtern`](PGExtern.md)📎

---

## 🔹 Data Model

| Field         | Type    | Description                   |
|---------------|---------|-------------------------------|
| `_clock`      | `Clock` | Internal pygame clock wrapper |
| `_target_fps` | `int`   | Desired frame rate cap        |
| `_dt`         | `float` | Last computed delta time      |

---

## 🔹 Public API

### Constructor

| Signature       | Description                       |
|-----------------|-----------------------------------|
| `__init__(fps)` | Initializes clock with target FPS |

---

### Accessors

| Method       | Returns | Description              |
|--------------|---------|--------------------------|
| `dt`         | `float` | Last computed delta time |
| `fps`        | `float` | Real measured FPS        |
| `target_fps` | `int`   | Current FPS cap          |

---

### Mutators

| Method       | Description                          |
|--------------|--------------------------------------|
| `target_fps` | Sets FPS cap (minimum enforced to 1) |

---

### Core Methods

| Method     | Description                               |
|------------|-------------------------------------------|
| `update()` | Updates delta time and enforces FPS limit |

---

### Utility Methods

| Method        | Description                 |
|---------------|-----------------------------|
| `__float__()` | Returns delta time as float |
| `dump()`      | Debug full object structure |
| `debug()`     | Detailed value inspection   |

---

## 🔹 Lifecycle

```text
Creation
   │
   ▼
Clock Initialization (pygame Clock instance)
   │
   ▼
Runtime Loop Integration
   │
   ▼
Per-frame update() calls
   │
   ▼
Delta time + FPS computation
   │
   ▼
Engine shutdown
```

Describe each stage in detail.

---

## 🔹 Internal Behavior

`JEClock` is built around a frame-regulated timing system:

* `_clock.tick(target_fps)` limits frame rate and returns elapsed milliseconds
* Delta time (`_dt`) is computed in seconds
* Delta time is clamped to a maximum of `1/60` to avoid large frame spikes
* FPS is queried from the underlying pygame clock

This ensures:

* stable simulation timing
* prevention of physics instability due to frame spikes
* consistent movement across different hardware

---

## 🔹 Execution Flow

```text
update()
   │
   ▼
clock.tick(target_fps)
   │
   ▼
Convert ms → seconds
   │
   ▼
Clamp dt (max 1/60)
   │
   ▼
Store _dt
```

---

## 🔹 Usage

### Basic Example

```python
clock = JEClock(60)

while game.is_running:
    clock.update()
    print(clock.dt)
```

---

### Realistic Example

```python
clock = JEClock(144)

while game.running:
    clock.update()

    entity.position += entity.velocity * clock.dt
```

---

## 🔹 Design Decisions

* Uses pygame Clock for hardware-level timing accuracy
* Delta time clamped to prevent instability
* Frame limiting integrated directly into update step
* Simple float-based interface for performance
* Minimal abstraction overhead for hot loop usage

---

## 🔹 Performance Notes

* `update()` is O(1)
* No allocations in hot path
* Direct access to pygame timing backend
* Suitable for per-frame execution without overhead concerns

---

## 🔹 Thread Safety

```text
Thread-safe: No
```

Notes:

* Mutable internal state (`_dt`, `_target_fps`)
* Designed for single-threaded game loop usage only

---

## 🔹 Limitations

* No historical time tracking
* No fixed timestep mode
* No interpolation system
* Clamp may hide extreme frame spikes instead of exposing them

---

## 🔹 Edge Cases

* Extremely low FPS systems clamp dt to prevent instability
* Setting FPS below 1 is corrected to 1
* FPS reading may fluctuate depending on system load

---

## 🔹 Current State

⚠️ Stable core timing system for engine loop control.

### Implemented

* Delta time calculation
* FPS tracking
* FPS limiting
* Float casting support

### Planned

* Fixed timestep mode
* Accumulator-based physics stepping
* Frame interpolation support
* Performance profiling hooks

---

## 🔹 Debugging

* Use `dump()` to inspect internal clock state
* Compare `dt` spikes for performance issues
* Monitor `fps` fluctuations for system load analysis
* Validate physics stability with and without clamping

---

## 🔹 Related Classes

* [`JEGame`](JEGame.md)📎
* [`JEContainer`](JEContainer.md)📎
* [`JEClock`](JEClock.md)📎

---

## 🔹 Notes

`JEClock` is a foundational timing primitive of JarEngine.

All simulation stability, physics correctness, and movement consistency depend on its delta-time behavior.
