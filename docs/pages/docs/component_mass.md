---
layout: page
title: JarEngine - Component - Mass
sidebar: sidebar
permalink: /component_mass.html
---

# 📦 Mass

> Technical reference for the `Mass` component of JarEngine.

---

## 🔹 Overview

**`Mass` stores the physical mass value of an entity.**

Provides:
* Storage and access to an entity's mass value.
* Runtime modification of the entity mass through the entity API.
* Physical information required for physics-based calculations.

Used by entities requiring physical properties and systems handling physics simulation.

---

## 🔹 Data

| Field  |  Type   | Description                        |
|:------:|:-------:|------------------------------------|
| `mass` | `float` | Physical mass value of the entity. |

---

## 🔹 Used by

### Entity
* `JEEntity.set_mass()`
* `JEEntity.update_mass()`
* `JEEntity.get_mass()`

### System
* No system currently requires this component.

---