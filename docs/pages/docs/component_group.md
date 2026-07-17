---
layout: page
title: JarEngine - Component - Group
sidebar: sidebar
permalink: /component_group.html
---

# 📦 Group

> Technical reference for the `Group` component of JarEngine.

---

## 🔹 Overview

**`Group` stores a collection of entities belonging to the same group.**

Provides:
* Storage of multiple entity references.
* Addition of entities to an entity group.
* Removal and retrieval of grouped entities.

Used by entities requiring hierarchical organization, entity collections, or group-based management features.

---

## 🔹 Data

|  Field  |          Type           | Description                                            |
|:-------:|:-----------------------:|--------------------------------------------------------|
| `group` | `JEContainer[JEEntity]` | Container storing entities associated with this group. |

---

## 🔹 Used by

### Entity
* `group_add`
* `group_remove`
* `get_group`

### System
* No direct system requirement.

---