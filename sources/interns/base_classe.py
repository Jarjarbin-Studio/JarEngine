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

from sources.interns import JTKInternConsole as _JTKInternConsole
from sources.interns.decorators import documentation as _documentation

@_documentation
class JEInternClassBase:
    """ClassBase (Internal API)"""

    __instance_policy__ = "normal"
    __instance_limit__ = None
    __recursive__ = True

    def __init__(self):
        """JEInternClassBase creator"""
        self.jeid: str = _uuid4().hex

    def __str__(self):
        """Get information about the class"""
        name = getattr(self, "name", None)
        id = getattr(self, "id", None)

        if name:
            return f"{self.__class__.__name__}({name=}, {id=})"

        return f"{self.__class__.__name__}({id=})"

    def __repr__(self):
        """Get representation of the class"""
        return (
            f"<{self.__class__.__name__}"
            f" jeid={getattr(self, 'jeid', 'unknown')}>"
        )

    def to_dict(self):
        """Get dictionary representation of the class"""

        def get_value(value: _Any) -> _Any:
            if isinstance(value, JEInternClassBase):
                return value.to_dict()
            else:
                return value

        return {
            "class": self.__class__.__name__,
            "jeid": self.jeid,
            "public": {
                k: get_value(v)
                for k, v in self.__dict__.items()
                if not k.startswith("_") and not callable(v)
            }
        }

    def debug(self, *, is_colored = False, max_depth = -1, branched_recursive = False, prefix = "", is_last = True, is_root = True, show_root = True, _visited = None, _stack = None):
        """Pretty-print the class recursively (with all of its children)"""

        COLOR_THEME: dict[str, tuple[int, int, int]] = {
            "class": (180, 220, 255),
            "attribute": (255, 200, 120),
            "value": (200, 200, 200),
            "engine_object": (120, 255, 180),
            "container": (120, 180, 255),
            "id": (255, 120, 120),
            "name": (255, 255, 150),
            "list": (200, 160, 255),
            "dict": (160, 255, 220),
            "pygame": (255, 140, 255),
            "immutable": (180, 180, 180),
            "callable": (255, 180, 100),
            "error": (255, 80, 80),
            "policy": (255, 180, 255),
            "limit": (180, 255, 255),
        }

        BRANCH = "│   "
        SPACE = "    "

        from sources.systems.immutable import JEImmutable

        if _visited is None:
            _visited = set()

        if _stack is None:
            _stack = set()

        def _rgb(
                rgb: tuple[int, int, int],
                text: str
            ) -> str:
            return (
                _JTKInternConsole.Text.Format.apply(
                    text,
                    _JTKInternConsole.ANSI.Color.rgb_fg(*rgb),
                ) + _JTKInternConsole.ANSI.Color(_JTKInternConsole.ANSI.Color.C_RESET).s
            )

        def colorize(
                text: str,
                category: str
            ) -> str:
            if not is_colored:
                return text
            color = COLOR_THEME.get(category)
            if color is None:
                return text
            return _rgb(color, text)

        def get_instance_indicator(cls) -> str:
            policy = getattr(cls, "__instance_policy__", "normal")
            limit = getattr(cls, "__instance_limit__", None)

            if policy == "normal":
                return ""

            if policy == "singleton":
                return "{singleton:1}"

            if policy == "flyweight":
                if limit is None:
                    return "{flyweight:∞}"
                return f"{{flyweight:{limit}}}"

            return ""

        def classify(
                name: str,
                value
            ) -> str:
            if name == "JEID":
                return "id"
            if isinstance(value, JEInternClassBase):
                return "engine_object"
            if isinstance(value, JEImmutable):
                return "immutable"
            if callable(value):
                return "callable"
            if isinstance(value, dict):
                return "dict"
            if isinstance(value, (list, tuple, set)):
                return "list"
            module_name = getattr(type(value), "__module__", "")
            if module_name.startswith("pygame"):
                return "pygame"
            return "value"

        def extend_prefix(
                current_prefix: str,
                last_item: bool
            ) -> str:
            return current_prefix + (SPACE if last_item else BRANCH)

        def safe_repr(value) -> str:
            try:
                return repr(value)
            except Exception as err:
                return f"<repr error: {err}>"

        def append_child_object(
                label: str,
                child,
                child_prefix: str,
                last_item: bool
            ) -> None:
            connector = "└─ " if last_item else "├─ "
            cls_col = colorize(child.__class__.__name__, "engine_object")
            lines.append(f"{child_prefix}{connector}{label} ({cls_col})")
            if max_depth == 0:
                lines.append(f"{child_prefix}{SPACE if last_item else BRANCH} [...]")
                return

            lines.extend(
                child.debug(
                    is_colored=is_colored,
                    max_depth=max_depth - 1,
                    branched_recursive=branched_recursive,
                    prefix=extend_prefix(child_prefix, last_item),
                    is_last=True,
                    is_root=False,
                    show_root=False,
                    _visited=_visited,
                    _stack=_stack,
                ).splitlines()
            )

        def append_leaf(
                name: str,
                label: str,
                value,
                child_prefix: str,
                last_item: bool
            ) -> None:
            connector = "└─ " if last_item else "├─ "
            category = classify(name, value)
            rendered = safe_repr(value)

            module_name = getattr(type(value), "__module__", "")
            if module_name.startswith("pygame"):
                rendered = f"{type(value).__name__} (PGIntern)"
                category = "pygame"

            lines.append(
                f"{child_prefix}{connector}{label} = {colorize(rendered, category)}"
            )

        def append_mapping(
                name: str,
                label: str,
                mapping: dict,
                child_prefix: str,
                last_item: bool
            ) -> None:
            connector = "└─ " if last_item else "├─ "
            lines.append(f"{child_prefix}{connector}{label} = {colorize('{}', 'dict')}")

            nested_prefix = extend_prefix(child_prefix, last_item)
            items = list(mapping.items())

            for index, (sub_key, sub_value) in enumerate(items):
                sub_last = index == len(items) - 1
                sub_label = colorize(str(sub_key), "name")

                if isinstance(sub_value, JEInternClassBase):
                    append_child_object(sub_label, sub_value, nested_prefix, sub_last)
                else:
                    append_leaf(name, sub_label, sub_value, nested_prefix, sub_last)

        def append_sequence(
                name: str,
                label: str,
                sequence,
                child_prefix: str,
                last_item: bool
            ) -> None:
            connector = "└─ " if last_item else "├─ "
            lines.append(f"{child_prefix}{connector}{label} = {colorize('[]', 'list')}")

            nested_prefix = extend_prefix(child_prefix, last_item)
            items = list(sequence)

            for index, sub_value in enumerate(items):
                sub_last = index == len(items) - 1
                sub_label = colorize(f"[{index}]", "list")

                if isinstance(sub_value, JEInternClassBase):
                    append_child_object(sub_label, sub_value, nested_prefix, sub_last)
                else:
                    append_leaf(name, sub_label, sub_value, nested_prefix, sub_last)

        obj_id = id(self)
        if obj_id in _stack:
            return (
                f"{prefix}└─ {colorize('<recursive>', 'error')} "
                f"{colorize(self.__class__.__name__, "class")} ({colorize(f"JEID-{self.jeid}" if hasattr(self, "jeid") else f"ID-{obj_id}", 'id')})"
            )

        if self.__recursive__:
            _stack.add(obj_id)

        try:
            lines: list[str] = []

            name = getattr(self, "name", None)
            class_name_raw = self.__class__.__name__
            class_name = colorize(class_name_raw, "class")

            indicator = get_instance_indicator(self.__class__)
            indicator = f" {colorize(indicator, 'policy')}" if indicator else ""

            if name:
                base = f"{colorize(name, 'name')} ({class_name})"
            else:
                base = class_name

            label = f"{base}{indicator}"

            if is_root and show_root:
                lines.append(label)
            else:
                connector = "└─ " if is_last else "├─ "
                lines.append(f"{prefix}{connector}{label}")

            new_prefix = extend_prefix(prefix, is_last)

            public_attrs = {
                key: value
                for key, value in getattr(self, "__dict__", {}).items()
                if not key.startswith("_")
            }

            props: dict[str, object] = {}
            for attr_name in dir(self.__class__):
                attr = getattr(self.__class__, attr_name, None)
                if isinstance(attr, property) and not attr_name.startswith("_"):
                    try:
                        props[f"@{attr_name}"] = getattr(self, attr_name)
                    except Exception as err:
                        props[f"@{attr_name}"] = f"<error: {err}>"

            all_attrs = {**public_attrs, **props}

            for index, (attr_name, attr_value) in enumerate(all_attrs.items()):
                last_item = index == len(all_attrs) - 1
                attr_name = "JEID" if attr_name == "jeid" else attr_name
                attr_label = colorize(attr_name, "id" if attr_name == "JEID" else "attribute")

                if isinstance(attr_value, JEInternClassBase):
                    append_child_object(attr_label, attr_value, new_prefix, last_item)
                elif isinstance(attr_value, dict):
                    append_mapping(attr_name, attr_label, attr_value, new_prefix, last_item)
                elif isinstance(attr_value, (list, tuple, set)):
                    append_sequence(attr_name, attr_label, attr_value, new_prefix, last_item)
                else:
                    append_leaf(attr_name, attr_label, attr_value, new_prefix, last_item)

            return "\n".join(lines)
        finally:
            if branched_recursive:
                _stack.discard(obj_id)

    def dump(self, *, prefix="", is_last=True, is_root=True, _attr_key=None, _visited=None):
        BRANCH = "│   "
        SPACE = "    "
        TEE = "├─ "
        ELBOW = "└─ "

        if _visited is None:
            _visited = set()

        def extend_prefix(current: str, last: bool) -> str:
            return current + (SPACE if last else BRANCH)

        def type_name(v) -> str:
            return type(v).__name__

        def safe_repr(v) -> str:
            try:
                r = repr(v)
                return r if len(r) <= 80 else r[:77] + "…"
            except Exception:
                return "<repr error>"

        def summarize_collection(v) -> str:
            if isinstance(v, dict):
                if not v:
                    return "dict[0]"
                contained = sorted({type(x).__name__ for x in v.values()})
                return f"dict[{len(v)}] of {', '.join(contained)}"
            try:
                elements = list(v)
            except Exception:
                return f"{type_name(v)}(?)"
            if not elements:
                return f"{type_name(v)}[0]"
            contained = sorted({type(x).__name__ for x in elements})
            return f"{type_name(v)}[{len(elements)}] of {', '.join(contained)}"

        obj_id = id(self)
        if obj_id in _visited and self.__recursive__:
            connector = ELBOW if is_last else TEE
            key_part = f"{_attr_key}: " if _attr_key else ""
            return f"{prefix}{connector}{key_part}<circular> {self.__class__.__name__}"
        _visited.add(obj_id)

        lines = []
        class_name = self.__class__.__name__
        name = getattr(self, "name", None)

        class_part = class_name + (f" ({name!r})" if name else "")

        if is_root:
            lines.append(class_part)
        else:
            connector = ELBOW if is_last else TEE
            key_part = f"{_attr_key}: " if _attr_key else ""
            lines.append(f"{prefix}{connector}{key_part}{class_part}")

        new_prefix = extend_prefix(prefix, is_last)

        raw_attrs: dict = {k: v for k, v in dict(getattr(self, "__dict__", {})).items() if not k.startswith("_")}

        props: dict = {}
        for attr_name in dir(self.__class__):
            descriptor = getattr(self.__class__, attr_name, None)
            if isinstance(descriptor, property) and not attr_name.startswith("_"):
                try:
                    props[f"@{attr_name}"] = getattr(self, attr_name)
                except Exception as exc:
                    props[f"@{attr_name}"] = f"<error: {exc}>"

        items = list({**raw_attrs, **props}.items())

        for i, (k, v) in enumerate(items):
            last = (i == len(items) - 1)
            connector = ELBOW if last else TEE

            if isinstance(v, JEInternClassBase):
                if id(v) in _visited:
                    lines.append(
                        f"{new_prefix}{connector}{k}: {v.__class__.__name__} = <circular>"
                    )
                else:
                    child = v.dump(
                        prefix=new_prefix,
                        is_last=last,
                        is_root=False,
                        _attr_key=k,
                        _visited=_visited,
                    )
                    lines.append(child)

            elif isinstance(v, (list, tuple, dict)):
                summary = summarize_collection(v)
                lines.append(f"{new_prefix}{connector}{k}: {type_name(v)} = {summary}")

            else:
                lines.append(f"{new_prefix}{connector}{k}: {type_name(v)} = {safe_repr(v)}")

            if last:
                lines.append(f"{new_prefix}")

        lines = [line for line in lines if line.strip()]

        return "\n".join(lines)
