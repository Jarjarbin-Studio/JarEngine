---
layout: page
title: Module - Interns | Module - Decorators
sidebar: sidebar
permalink: /InternsDecorators.html
---

# 📦 Decorators

> Technical reference for the decorators module of JarEngine.

---

## 🔹 Overview

**`Decorators` is a JarEngine module responsible for providing runtime class introspection and automatic documentation generation tools.**

It provides the classes and utilities required to:

* Attach runtime documentation metadata to classes
* Generate structured documentation maps from class definitions
* Provide inspection utilities for attributes, methods, and properties

---

## 🔹 Purpose

The `decorators` module aims to:

* Automate documentation extraction from engine classes
* Provide a standardized reflection system over engine objects
* Enable runtime introspection for debugging and tooling

It is **not** a rendering or gameplay module, but a **meta-programming and introspection utility layer**.

---

## 🔹 Module Organization

```text
sources/
└── interns/
    ├── decorators.py
````

| File            | Description                                      |
|-----------------|--------------------------------------------------|
| `decorators.py` | Provides runtime documentation decorator system. |

---

## 🔹 Responsibilities

| Responsibility            | Description                                   |
|---------------------------|-----------------------------------------------|
| Class introspection       | Extract metadata from classes using `inspect` |
| Documentation mapping     | Build structured representation of class APIs |
| Runtime attachment        | Attach `__docmap__` and `.doc()` method       |
| Filtering internal fields | Ignore private/internal attributes            |

---

## 🔹 Public Classes

| Class           | Description                                                         |
|-----------------|---------------------------------------------------------------------|
| `documentation` | Decorator that generates runtime documentation metadata for a class |

Each class should have its own dedicated documentation page.

---

## 🔹 Dependencies

### Depends On

* `inspect`

Used for runtime reflection of class structures, methods, and signatures.

---

## 🔹 Data Flow

```text
Class Definition
   │
   ▼
@documentation decorator applied
   │
   ▼
Inspect class using inspect module
   │
   ├── Extract attributes
   ├── Extract methods
   ├── Extract properties
   │
   ▼
Build __docmap__
   │
   ▼
Attach runtime .doc() method
   │
   ▼
Runtime introspection available
```

---

## 🔹 Usage

### Basic Example

```python
@documentation
class Example:
    def hello(self):
        """Say hello"""
        return "Hello"
```

---

### Typical Workflow

```python
# 1. Define class
@documentation
class Player:
    def move(self, x, y):
        """Move player"""
        pass

# 2. Access generated documentation
Player.doc()
```

Explanation:

* Step 1 attaches decorator
* Step 2 builds internal docmap
* Step 3 enables runtime inspection printing

---

## 🔹 Design Decisions

* Reflection-based design allows zero manual documentation overhead
* Separation between metadata generation and execution logic
* Filtering of private members ensures clean public API view
* Use of `inspect` ensures compatibility with Python runtime introspection

---

## 🔹 Performance Notes

* Time complexity: O(n) over class members
* Memory usage: proportional to number of attributes/methods
* Cache behavior: no caching; rebuilt per decoration
* Allocation strategy: builds full dictionary snapshot at decoration time

---

## 🔹 Limitations

* No incremental update of documentation after runtime modification
* Does not track dynamically added attributes after decoration
* No type inference beyond Python runtime type inspection

---

## 🔹 Edge Cases

* Properties without docstrings result in empty documentation fields
* Private methods (`_method`) are excluded from method map
* Classes with heavy dynamic modification may produce incomplete snapshots

---

## 🔹 Current State

⚠️ Current implementation status.

### Implemented

* Class introspection via `inspect`
* Automatic method/property/attribute extraction
* `__docmap__` attachment
* `.doc()` runtime printing method

### Planned

* JSON export of documentation maps
* Incremental update system for live classes
* Filtering presets (public/private/full views)

---

## 🔹 Debugging

* Use `ClassName.__docmap__` to inspect raw metadata
* Use `ClassName.doc()` to print formatted structure
* Check missing methods in docmap for decorator execution issues
* Verify `inspect.signature()` failures for dynamic functions

---

## 🔹 Notes

This module is a core meta-programming utility of JarEngine, enabling automatic reflection-based documentation generation without manual annotation overhead.
