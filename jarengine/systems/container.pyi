# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.7
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by Pygame, modern game engine design patterns,
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
# This is NOT Pygame itself.
# It is a custom abstraction layer built on top of Pygame.
#
# =============================================================================

from __future__ import annotations

from typing import TypeVar, Optional, Iterator, Any, Generic, Type

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.systems.bool import JEBool

T = TypeVar("T", bound=JEInternBaseClass)

class JEContainer(Generic[T], JEInternBaseClass):
    def __init__(self, allowed_type: Type[T], allow_subclass: JEBool = JEBool(0)):
        """
            JEContainer
            
            Parameters:
                allowed_type (type): Object type that the container will store
                allow_subclass (JEBool) = JETrue: Whether the container will accept subclasses of this type
        """
        ...
    def add(self, obj: T):
        """
            Add an object to the container
            
            Parameters:
                obj (T): Object to add
        """
        ...
    def __getitem__(self, value: str | T | Type) -> T:
        """
            Get an item from the container (automatically reroute to the proper getter)
            
            Parameters:
                value (str | type | T): Name / JEID / instance / type of the object
            
            Returns:
                T: Object
        """
        ...
    def get(self, *, name: Optional[str] = None, jeid: Optional[str] = None, instance: Optional[T] = None, _type: Optional[Type] = None, default: Any = NotImplemented) -> T:
        """
            Get an item from the container

            Parameters:
                name (Optional[str]) = None: Name of the object
                jeid (Optional[str]) = None: JEID of the object
                instance (Optional[T]) = None: instance
                _type (Optional[type]) = None: Type of the object
                default (Any) = NotImplemented: Default value to return if object not found (raise an error if leaved as such)

            Returns:
                T: Object
        """
        ...
    def rm(self, *, name: Optional[str] = None, jeid: Optional[str] = None, instance: Optional[T] = None, _type: Optional[Type] = None) -> T:
        """
            Remove an item from the container

            Parameters:
                name (Optional[str]) = None: Name of the object
                jeid (Optional[str]) = None: JEID of the object
                instance (Optional[T]) = None: instance
                _type (Optional[type]) = None: Type of the object
        """
        ...
    def clear(self):
        """
            Clear the container
        """
        ...
    def __iter__(self) -> Iterator[T]:
        """
            Iterate over the container

            Returns:
                Iterator[T]: Iterator of objects
        """
        ...
    @property
    def data(self) -> dict[str, T]:
        """
            Get the raw data of the container

            Returns:
                dict[str, T]: Dictionary of objects
        """
        ...
