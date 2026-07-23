# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by PyGame, modern game engine design patterns,
# and directly influenced by the architecture of NewCSFML.
#
# It is designed for educational purposes and small-to-medium game projects.
#
# It provides structured systems such as entity management, scene handling,
# render abstraction, and advanced modules like particle systems.
#
# =============================================================================
# WARNING:
# =============================================================================
#
# This is NOT PyGame itself.
# It is a custom abstraction layer built on top of PyGame.
#
# =============================================================================

from __future__ import annotations

import inspect as _inspect

def documentation(cls):
    """Add automatic, runtime documentation"""

    def get_doc(obj) -> str:
        return _inspect.getdoc(obj) or ""

    def is_property(attr):
        return isinstance(attr, property)

    def build_docmap(target_cls):
        docmap = {
            "class": {
                "name": target_cls.__name__,
                "doc": get_doc(target_cls),
                "attributes": {},
                "methods": {},
                "properties": {},
            }
        }

        for name, value in vars(target_cls).items():
            if name.startswith("_"):
                continue

            if _inspect.isfunction(value) or _inspect.ismethod(value):
                continue

            if is_property(value):
                continue

            docmap["class"]["attributes"][name] = {
                "type": type(value).__name__,
                "value": repr(value),
                "doc": ""
            }

        for name, func in _inspect.getmembers(target_cls, _inspect.isfunction):
            if name.startswith("_") and not name.startswith("__"):
                continue

            docmap["class"]["methods"][name] = {
                "signature": str(_inspect.signature(func)),
                "doc": get_doc(func),
            }

        for name, attr in vars(target_cls).items():
            if isinstance(attr, property):
                docmap["class"]["properties"][name] = {
                    "doc": get_doc(attr.fget),
                    "read_only": attr.fset is None,
                }

        return docmap

    def print_docmap(docmap, indent=0):
        pad = "    " * indent

        def line(text):
            print(f"{pad}{text}")

        cls = docmap["class"]

        line(f"{cls['name']}")
        line("-" * len(cls["name"]))

        if cls["doc"]:
            line(cls["doc"])
            line("")

        if cls["attributes"]:
            line("Attributes:")
            for k, v in cls["attributes"].items():
                line(f"    - {k} ({v['type']}) = {v['value']}")

        if cls["properties"]:
            line("\nProperties:")
            for k, v in cls["properties"].items():
                ro = "read-only" if v["read_only"] else "read/write"
                line(f"    - {k} [{ro}]")
                if v["doc"]:
                    line(f"        {v['doc']}")

        if cls["methods"]:
            line("\nMethods:")
            for k, v in cls["methods"].items():
                line(f"    - {k}{v['signature']}")
                if v["doc"]:
                    line(f"        {v['doc']}")

    cls.__docmap__ = build_docmap(cls)
    cls.doc = classmethod(lambda c: print_docmap(c.__docmap__))

    return cls