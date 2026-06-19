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

from __future__ import annotations

from uuid import uuid4 as _uuid4
from typing import Any as _Any

from sources.interns import JTKInternError as _JTKInternError

class JEInternClassBase:

    def __init__(self) -> None:
        self.id: str = _uuid4().hex

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

        def get_value(value: _Any) -> _Any:
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

    def dump(
            self,
            prefix: str = "",
            is_last: bool = True,
            is_root: bool = True,
            show_root: bool = True,
            _visited: set | None = None
    ) -> str:
        lines = []

        if _visited is None:
            _visited = set()

        obj_id = id(self)
        if obj_id in _visited:
            return f"{prefix} └─ <recursive {self.__class__.__name__}>"

        _visited.add(obj_id)

        name = getattr(self, "name", None)
        class_name = self.__class__.__name__
        label = f"{name} ({class_name})" if name else class_name

        if is_root and show_root:
            lines.append(label)

        new_prefix = prefix + ("  " if is_last else "│ ")

        public_attrs = {}
        if hasattr(self, "__dict__"):
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
                except Exception as err:
                    props[f"@{attr_name}"] = f"<error: {err}>"

        all_attrs = {**public_attrs, **props}
        items = list(all_attrs.items())

        def is_je_object(v):
            return hasattr(v, "dump") and callable(getattr(v, "dump", None)) \
                and isinstance(v, JEInternClassBase)

        def is_mapping(v):
            return isinstance(v, dict)

        def is_iterable(v):
            return isinstance(v, (list, tuple, set))

        for i, (k, v) in enumerate(items):
            last = i == len(items) - 1
            connector = "└─ " if last else "├─ "

            if is_je_object(v):
                lines.append(f"{new_prefix}{connector}{k} ({v.__class__.__name__})")

                child_prefix = new_prefix + ("  " if last else "│ ")
                lines.extend(
                    v.dump(
                        child_prefix,
                        is_last=True,
                        is_root=False,
                        show_root=False,
                        _visited=_visited
                    ).split("\n")
                )

            elif is_mapping(v):
                lines.append(f"{new_prefix}{connector}{k} = {{}}")

                child_prefix = new_prefix + ("  " if last else "│ ")

                for j, (sub_k, sub_v) in enumerate(v.items()):
                    sub_last = j == len(v) - 1
                    sub_connector = " └─ " if sub_last else " ├─ "

                    if is_je_object(sub_v):
                        lines.append(f"{child_prefix}{sub_connector}{sub_k} ({sub_v.__class__.__name__})")

                        sub_child_prefix = child_prefix + ("  " if sub_last else "│ ")
                        lines.extend(
                            sub_v.dump(
                                sub_child_prefix,
                                is_last=True,
                                is_root=False,
                                show_root=False,
                                _visited=_visited
                            ).split("\n")
                        )
                    else:
                        lines.append(f"{child_prefix}{sub_connector}{sub_k} = {sub_v!r}")

            elif is_iterable(v):
                lines.append(f"{new_prefix}{connector}{k} = []")

                child_prefix = new_prefix + ("  " if last else "│ ")

                v_list = list(v)

                for j, sub_v in enumerate(v_list):
                    sub_last = j == len(v_list) - 1
                    sub_connector = " └─ " if sub_last else " ├─ "

                    if is_je_object(sub_v):
                        lines.append(f"{child_prefix}{sub_connector}[{j}] ({sub_v.__class__.__name__})")

                        sub_child_prefix = child_prefix + ("  " if sub_last else "│ ")
                        lines.extend(
                            sub_v.dump(
                                sub_child_prefix,
                                is_last=True,
                                is_root=False,
                                show_root=False,
                                _visited=_visited
                            ).split("\n")
                        )
                    else:
                        lines.append(f"{child_prefix}{sub_connector}[{j}] = {sub_v!r}")

            else:
                lines.append(f"{new_prefix}{connector}{k} = {v!r}")

        return "\n".join(lines)
