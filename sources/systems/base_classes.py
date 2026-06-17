"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v0.1.0
    Author: Jarjarbin Studio
    Licence: GPL v3

    This engine is inspired by Pygame, modern game engine design patterns,
    and directly influenced by the architecture of NewCSFML.

    It is designed for educational purposes and small-to-medium game projects.

    It provides structured systems such as entity management, scene handling,
    render abstraction, and advanced modules like particle systems.

    WARNING:
        This is NOT Pygame itself.
        It is a custom abstraction layer built on top of Pygame.
"""

import uuid
from typing import Any

from sources.systems import JTKInternError

class JEInternClassBase:

    def __init__(self) -> None:
        self.id: str = uuid.uuid4().hex

    def __str__(self) -> str:
        name = getattr(self, "name", None)
        id = getattr(self, "id", None)

        if name:
            return f"{self.__class__.__name__}({name=}, {id=})"

        return f"{self.__class__.__name__}({id=})"

    def __repr__(self) -> str:
        final_str: str = ""

        if self.__dict__:
            for key in self.__dict__:
                final_str += (
                    f"{key}={self.__dict__[key]!r}, "
                    if not key.startswith("_") else
                    ""
                )

            final_str = final_str[:-2]

        return f"<{self.__class__.__name__}{f': {final_str}' if final_str else ""}>"

    def to_dict(self) -> dict:

        def get_value(value: Any) -> Any:
            if isinstance(value, JEInternClassBase):
                return value.to_dict()
            else:
                return value

        return {
            "class": self.__class__.__name__,
            "id": self.id,
            "public": {
                k: get_value(v)
                for k, v in self.__dict__.items()
                if not k.startswith("_") and not callable(v)
            }
        }

    def dump(self, prefix: str = "", is_last: bool = True, is_root: bool = True, show_root: bool = True) -> str:
        lines = []
        name = getattr(self, "name", None)
        class_name = self.__class__.__name__
        label = f"{name} ({class_name})" if name else class_name

        if is_root and show_root:
            lines.append(label)

        new_prefix = prefix + ("  " if is_last else "│ ")
        public_attrs = {
            k: v for k, v in self.__dict__.items()
            if not k.startswith("_")
        }
        props = {}

        for attr_name in dir(self.__class__):
            attr = getattr(self.__class__, attr_name, None)

            if isinstance(attr, property) and not attr_name.startswith("_"):
                try:
                    props[f"@{attr_name}"] = getattr(self, attr_name)
                except JTKInternError.BaseError as err:
                    props[f"@{attr_name}"] = f"<error: {err.message.strip().removesuffix(".")}>"

        all_attrs = {**public_attrs, **props}
        items = list(all_attrs.items())

        for i, (k, v) in enumerate(items):
            last = i == len(items) - 1
            connector = "└─ " if last else "├─ "

            if isinstance(v, JEInternClassBase):
                lines.append(f"{new_prefix}{connector}{k} ({v.__class__.__name__})")
                child_prefix = new_prefix + ("  " if last else "│ ")
                child_lines = v.dump(
                    child_prefix,
                    is_last=True,
                    is_root=False,
                    show_root=False
                ).split("\n")
                lines.extend(child_lines)

            else:
                lines.append(f"{new_prefix}{connector}{k} = {v!r}")

        return "\n".join(lines)
