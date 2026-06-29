---
layout: page
title: Module - Constants
sidebar: sidebar
permalink: /Constants.html
---

# 📦 Constants Module

> Centralized definition of engine-wide immutable values for input, events, and boolean wrappers.

---

## 🔹 Overview

**The `constants` module is a JarEngine core module responsible for defining global immutable engine constants such as input codes, event identifiers, and boolean wrappers.**

It provides the symbolic interface required to:

* Abstract pygame raw input values
* Standardize event handling across the engine
* Provide typed boolean representations
* Ensure consistent key/mouse/event references

---

## 🔹 Purpose

The `constants` module aims to:

* Replace raw pygame constants with typed engine-safe wrappers
* Provide a unified input namespace (`JEKey_*`, `JEEvt*`, `JEMse_*`)
* Enforce consistency across all input handling systems
* Centralize all engine-wide immutable values

It is **not** a logic processing module, but a **global constant mapping layer over pygame internals**.

---

## 🔹 Module Organization

```text
sources/
└── constants.py
```

This module is intentionally flat because it acts as a **global registry of immutable engine constants**.

| File           | Description                                           |
|----------------|-------------------------------------------------------|
| `constants.py` | Defines all JEKey, JEEvt, JEMse and boolean constants |

---

## 🔹 Responsibilities

| Responsibility | Description                                              |
|----------------|----------------------------------------------------------|
| Input mapping  | Maps pygame key codes to engine-safe `JEKey_*` constants |
| Event mapping  | Maps pygame events to `JEEvt*` constants                 |
| Mouse mapping  | Defines mouse button constants                           |
| Boolean system | Provides `JETrue` and `JEFalse` wrappers                 |
| Type safety    | Wraps raw values into engine-defined types               |

---

## 🔹 Public Constants

### Boolean System

| Constant  | Type     | Description          |
|-----------|----------|----------------------|
| `JETrue`  | `JEBool` | Engine boolean true  |
| `JEFalse` | `JEBool` | Engine boolean false |

---

### Event Constants

| Constant         | Description           |
|------------------|-----------------------|
| `JEEvtQuit`      | Window close event    |
| `JEEvtHidden`    | Window hidden event   |
| `JEEvtKeyDown`   | Key pressed event     |
| `JEEvtKeyUp`     | Key released event    |
| `JEEvtMouseDown` | Mouse button pressed  |
| `JEEvtMouseUp`   | Mouse button released |

---

### Keyboard Constants

All keyboard keys are defined as:

```text
JEKey_A ... JEKey_Z
JEKey_0 ... JEKey_9
JEKey_Enter
JEKey_Backspace
JEKey_Delete
JEKey_Tab
JEKey_Escape
JEKey_Up / Down / Left / Right
```

These wrap raw pygame keycodes into `JEKeyCode`.

---

### Mouse Constants

| Constant       | Description         |
|----------------|---------------------|
| `JEMse_Left`   | Left mouse button   |
| `JEMse_Middle` | Middle mouse button |
| `JEMse_Right`  | Right mouse button  |

---

## 🔹 Dependencies

### Depends On

* [`PGExtern`](PGExtern.md)📎
* [`JEBool`](JEBool.md)📎
* [`JEEventCode`](JEEventCode.md)📎
* [`JEKeyCode`](JEKeyCode.md)📎
* [`JEMouseCode`](JEMouseCode.md)📎

---

## 🔹 Data Flow

```text
pygame raw input
        │
        ▼
PGExtern constants
        │
        ▼
JE wrapper layer (constants.py)
        │
        ├── JEKeyCode
        ├── JEEventCode
        ├── JEMouseCode
        └── JEBool
        │
        ▼
Engine systems (Game / Input / Events)
```

---

## 🔹 Usage

### Basic Example

```python
if game.is_key_down(JEKey_S):
    print("Moving down")
```

---

### Event Usage

```python
if event.type == JEEvtQuit:
    game.close()
```

---

### Mouse Usage

```python
if game.is_mouse_pressed(JEMse_Left):
    print("Click detected")
```

---

## 🔹 Design Decisions

* Centralized constant registry avoids scattering pygame dependencies
* Strong typing via `JEKeyCode`, `JEEventCode`, `JEMouseCode`
* Ensures engine-level abstraction over raw backend
* Flat structure for maximum accessibility
* Immediate import usability (`from constants import JEKey_*`)

---

## 🔹 Performance Notes

* All constants are pre-instantiated at import time
* Zero runtime computation required for lookup
* Direct object comparison instead of string/key lookup
* Minimal overhead wrapper over pygame constants

---

## 🔹 Limitations

* Static mapping (no runtime remapping system yet)
* Large file due to explicit key enumeration
* No support for custom user-defined bindings yet
* Dependent on pygame key model

---

## 🔹 Current State

⚠️ Fully functional but static input mapping layer.

### Implemented

* Full keyboard mapping (A–Z, 0–9, arrows, control keys)
* Mouse button mapping
* Event abstraction layer
* Boolean wrapper system

### Planned

* Key rebinding system
* Input configuration profiles
* Runtime remapping layer
* Input action mapping (e.g. "Jump" instead of "Space")

---

## 🔹 Related Modules

* [`Events`](Events.md)📎
* [`Games`](Games.md)📎
* [`Systems`](Systems.md)📎
* [`Interns`](Interns.md)📎

---

## 🔹 Notes

This module acts as the **lowest-level abstraction layer over pygame input definitions**.

It is intentionally static and centralized to ensure deterministic behavior and to avoid runtime ambiguity in input handling.

---
