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

from typing import Callable, Any
from types import MappingProxyType

from sources.systems import JTKInternError, JTKInternAction
import sources.systems.base_classes as JEInternBaseClasses

class JEInternImmutable(JEInternBaseClasses.JEInternClassBase):
    def __init__(
            self,
            value: Any
        ) -> None:
        super().__init__()

        self._type = type(value)
        self._mpt: MappingProxyType = MappingProxyType(value)

    @property
    def type(self) -> type:
        return self._type

    @property
    def data(self) -> Any:
        return self._type(self._mpt)

    def __str__(self) -> str:
        return f"{self._type(self._mpt)} (Immutable)"

    def __repr__(self) -> str:
        return f"{self._type(self._mpt)!r} (Immutable)"

class JEInternContainer(JEInternBaseClasses.JEInternClassBase):

    def __init__(
            self,
            allowed_type: type
        ):
        super().__init__()

        if not isinstance(allowed_type, type):
            raise JTKInternError.Error.ErrorType(
                f"\n{allowed_type.__name__!r} is not a class type."
            )

        if not issubclass(allowed_type, JEInternBaseClasses.JEInternClassBase):
            raise JTKInternError.Error.ErrorType(
                f"\n{type(allowed_type).__name__!r} isn't of type {JEInternBaseClasses.JEInternClassBase.__name__!r}."
            )

        self._data = {}
        self._allowed_type: type = allowed_type

    def __getitem__(self, name: str):
        return self._data[name]

    def __setitem__(self, key: str, value):
        self._data[key] = value

    def add(self, obj: JEInternBaseClasses.JEInternClassBase):
        if not isinstance(obj, self._allowed_type):
            raise JTKInternError.Error.ErrorType(
                f"\n{type(obj).__name__!r} isn't of type {JEInternBaseClasses.JEInternClassBase.__name__!r}."
            )

        self._data[obj.name] = obj

    @property
    def data(self) -> JEInternImmutable:
        return JEInternImmutable(self._data)

class JEInternClassGraphic(JEInternBaseClasses.JEInternClassBase):

    def __init__(
            self,
            name: str
        ) -> None:
        super().__init__()

        self.name = name
        self._name_hash = hash(self.name)
        self._object_hash = hash(self)
        self._destroyed: bool = False

    def update(
            self,
            dt: float
        ) -> None:
        pass

    def destroy(self) -> None:
        self._destroyed = True

    def is_alive(self) -> bool:
        return not self._destroyed

class JEInternClassGraphicalObject(JEInternClassGraphic):

    def __init__(
            self,
            name: str
        ) -> None:
        super().__init__(name)

        self._events: dict[str, JTKInternAction.Actions] = {}
        self._dirty: bool = True
        self._enabled: bool = True

    def update(
            self,
            dt: float
        ) -> None:
        pass

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def is_alive(self) -> bool:
        return (not self._destroyed) and self._enabled

    def on(
            self,
            event: str,
            callback: Callable
        ):

        if not event in self._events:
            self._events[event] = JTKInternAction.Actions()

        self._events[event] += JTKInternAction.Action(callback.__name__, callback)

    def emit(
            self,
            event: str
        ) -> None:

        callback: JTKInternAction.Actions | None = self._events.get(event, None)

        if callback:
            callback()
