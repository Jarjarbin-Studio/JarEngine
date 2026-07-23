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

from typing import (
    final as _final,
    TypeVar as _TypeVar,
    Generic as _Generic
)

from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    assertion_class as _assertion_class,
    safe_cast as _safe_cast
)
import jarengine.interns.log as _log

_T = _TypeVar("_T", bound=_JEInternBaseClass)

@_documentation
@_final
class JEContainer(_Generic[_T], _JEInternBaseClass):

    def __init__(self, allowed_type, allow_subclass = _JEBool(0)):

        _assertion_type(allowed_type, type, "allowed_type must be of type 'type'", True)
        allow_subclass = _safe_cast(_assertion_type(allow_subclass, _JEBool, "allow_subclass must be of type 'JEBool'"), _JEBool)
        _assertion_class(allowed_type, _JEInternBaseClass, "allowed_type must be a subclass of 'JEInternBaseClass'", True)

        super().__init__()
        self._data = {}
        self._allowed_type = allowed_type
        self._allow_subclass = allow_subclass

        _log.log("DEBUG", "OBJECT", f"JEContainer: Created", self.jeid, allowed_type, allow_subclass)

    def add(self, obj):

        _assertion_type(obj, self._allowed_type, f"obj must be of type '{self._allowed_type.__name__}'", True)

        if self._allow_subclass:
            _assertion_class(type(obj), self._allowed_type, "allowed_type must be a subclass of 'JEInternBaseClass'", True)

        base_key = str(obj.jeid)
        key = base_key
        n = 1

        while key in self._data:
            key = f"{base_key}({n})"
            n += 1

        if hasattr(obj, "add_parent"):
            obj.add_parent(self)

        self._data[key] = obj

    def __getitem__(self, value):

        value = _safe_cast(_assertion_type(value, (str, int, type), "value must be of type 'str', 'int' or 'type'"), str)

        if isinstance(value, str):
            try:
                return self.get(name=value)
            except Exception:
                return self.get(jeid=value)
        elif isinstance(value, int):
            return self.get(index=value)
        return self.get(_type=value)

    def get(self, *, name = None, jeid = None, index = None, _type = None, default = NotImplemented):

        if name is not None:
            name = _safe_cast(_assertion_type(name, str, "name must be of type 'str'"), str)
        if jeid is not None:
            jeid = _safe_cast(_assertion_type(jeid, str, "jeid must be of type 'str'"), str)
        if index is not None:
            index = _safe_cast(_assertion_type(index, int, "index must be of type 'int'"), int)
        if _type is not None:
            _assertion_type(_type, type, "_type must be of type 'type'", True)

        if not (name or jeid or _type) and index is None:
            raise _JTKExternError.Error.ErrorKey(
                "\nName, JEID, index or type are required."
            )

        if name:
            for key, obj in self._data.items():
                if obj.name == name:
                    return obj
        elif jeid and jeid in self._data:
            return self._data[jeid]
        elif index is not None:
            return list(self._data.values())[index]
        elif _type:
            for key, obj in self._data.items():
                if isinstance(obj, _type):
                    return obj
        if default == NotImplemented:
            raise _JTKExternError.Error.ErrorKey(
                f"\n{f'{index!r}' if not index is None else f'{name or jeid or _type!r}'} not in container."
            )
        return default

    def rm(self, *, name = None, jeid = None, index = None, instance = None, _type = None):

        if name is not None:
            name = _safe_cast(_assertion_type(name, str, "name must be of type 'str'"), str)
        if jeid is not None:
            jeid = _safe_cast(_assertion_type(jeid, str, "jeid must be of type 'str'"), str)
        if index is not None:
            index = _safe_cast(_assertion_type(index, int, "index must be of type 'int'"), int)
        if instance is not None:
            _assertion_type(instance, _JEInternBaseClass, "instance must be of type 'JEInternBaseClass'", True)
        if _type is not None:
            _assertion_type(_type, type, "_type must be of type 'type'", True)

        if not (name or jeid or index or instance or _type):
            raise _JTKExternError.Error.ErrorKey(
                "\nName, JEID, index, instance or type are required."
            )

        if name:
            for key, obj in self._data.items():
                if obj.name == name:
                    return self._data.pop(key)
        elif jeid and jeid in self._data:
            return self._data.pop(jeid)
        elif index:
            return self._data.pop(self._data.values()[index].jeid)
        elif instance:
            for key, obj in self._data.items():
                if obj == instance:
                    return self._data.pop(key)
        elif _type:
            for key, obj in self._data.items():
                if isinstance(obj, _type):
                    return self._data.pop(key)
        raise _JTKExternError.Error.ErrorKey(
            f"\n{name or jeid or index or instance or _type!r} not in container."
        )

    def clear(self):
        self._data.clear()

    def __iter__(self):
        return iter(self._data.values())

    @property
    def data(self):
        return self._data

    def __deepcopy__(self, memo):
        new_container = JEContainer(self._allowed_type, allow_subclass = self._allow_subclass)

        for e in self:
            new_container.add(e)

        return new_container
