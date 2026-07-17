---
layout: page
title: JarEngine - Class - JEInternConfig
sidebar: sidebar
permalink: /class_jeinternconfig.html
---

# 📦 JEInternConfig

> Technical reference for the `JEInternConfig` class of JarEngine.

> Inherit from `jarbin_toolkit_config.Config` and [`•>JEInternBaseClass<•`]()📎

> ⚠️ **Internal Class Warning**
>
> This class is part of JarEngine's internal architecture and is not intended for normal user usage.
>
> Direct usage or modification may break engine behavior. Use only when creating advanced extensions, custom systems, or engine-level features.

---

## 🔹 Overview

**`JEInternConfig` is responsible for managing JarEngine internal configuration data.**

Provides:
* Configuration storage and access.
* Integration between JarEngine and the external configuration system.
* Runtime project and configuration path tracking.

Used internally to load and manage engine configuration files and settings.

---

## 🔹 Location

```text
JarEngine
│
├── Interns
│     └── JEInternConfig
│
└── ...
```

---

## 🔹 Data

|     Field      |      Type       | Description                     | Property? | Can be set? |
|:--------------:|:---------------:|---------------------------------|:---------:|:-----------:|
| `project_path` | `Optional[str]` | Path of the current project     |   False   |    True     |
| `config_path`  | `Optional[str]` | Path of the configuration files |   False   |    True     |

---

## 🔹 API

|  Function  |                       Arguments                        | Returns | Description                         |
|:----------:|:------------------------------------------------------:|:-------:|-------------------------------------|
| `__init__` | `name: str, data: Optional[dict[str, dict[str, Any]]]` |         | Initialize the configuration object |

---

## 🔹 Usage

```python
# Example usage
```

---
