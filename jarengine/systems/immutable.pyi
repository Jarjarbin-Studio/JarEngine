# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
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

from typing import Any, Callable, TypeVar, Type, Iterator, Generic, ItemsView, ValuesView, KeysView

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.systems.bool import JEBool

T: TypeVar = TypeVar("T")

class JEImmutable(Generic[T], JEInternBaseClass):
    def __init__(self, value: T):
        """
            JEImmutable

            Parameters:
                value (T): Object that will be frozen
        """
        ...
    @property
    def type(self) -> Type[T]:
        """
            Get the initial type of the object before frozen

            Returns:
                Type[T]: Initial type of the object
        """
        ...
    @property
    def frozen(self) -> Any:
        """
            Get the frozen state of the object (may not be of the original type)(all JarEngine objects keep their original types)
            
            Returns:
                Any: Frozen object
        """
        ...
    @property
    def data(self) -> T:
        """
            Get the unfrozen state of the object (it is NOT the original object)

            Returns:
                T: Unfrozen object
        """
        ...
    def __str__(self) -> str:
        """
            Get the string of the object (if supported)

            Returns:
                str: String of the object
        """
        ...
    def __repr__(self) -> str:
        """
            Get the string representation of the object (if supported)

            Returns:
                str: String representation
        """
        ...
    def __iter__(self) -> Iterator[Any]:
        """
            Iterate over the object (if supported)

            Returns:
                Iterator[Any]: Iterator
        """
        ...
    def __len__(self) -> int:
        """
            Get the length of the object (if supported)

            Returns:
                int: Length
        """
        ...
    def __getitem__(self, item: Any) -> Any:
        """
            Get an item from the object (if supported)
            
            Parameters:
                item (Any): Item to get
            
            Returns:
                Any: Item
        """
        ...
    def __contains__(self, item: Any) -> JEBool:
        """
            Check if the object contains the item (if supported)

            Parameters:
                item (Any): Item to check

            Returns:
                JEBool: Whether the item is in the object
        """
        ...
    def __bool__(self) -> bool:
        """
            Returns the boolean value of the object (if supported)

            Returns:
                bool: Boolean value of the object
        """
        ...
    def __reversed__(self) -> Iterator[Any]:
        """
            Iterate over the reversed object (if supported)

            Returns:
                Iterator[Any]: Iterator
        """
        ...
    def map(self, func: Callable[[Any], Any]) -> list[Any]:
        """
            Map the object (if supported)

            Parameters:
                func (Callable[[Any], Any]): Function to apply to the object

            Returns:
                list[Any]: Mapping of the object
        """
        ...
    def filter(self, func: Callable[[Any], bool]) -> list[Any]:
        """
            Filter the object (if supported)

            Parameters:
                func (Callable[[Any], bool]): Function to apply to the object

            Returns:
                list[Any] Filtered object
        """
        ...
    def any(self) -> JEBool:
        """
            Return True if bool(x) is True for any x in the iterable (False if empty)(if supported)

            Returns:
                JEBool: Whether any element of the object is True
        """
        ...
    def all(self) -> JEBool:
        """
            Return True if bool(x) is True for all x in the iterable (False if empty)(if supported)

            Returns:
                JEBool: Whether all elements of the object are True
        """
        ...
    def count(self, value: Any) -> int:
        """
            Count value occurrence in the object (if supported)

            Parameters:
                value (Any): Value to count

            Returns:
                int: Count value
        """
        ...
    def index(self, value: Any) -> int:
        """
            Get the index of the value (if supported)

            Parameters:
                value (Any): Value to index

            Returns:
                int: Index of the value
        """
        ...
    def keys(self) -> KeysView:
        """
            Get the keys view of the object (if supported)

            Returns:
                KeysView: Keys view of the object
        """
        ...
    def values(self) -> ValuesView:
        """
            Get the values view of the object (if supported)

            Returns:
                ValuesView: Values view of the object
        """
        ...
    def items(self) -> ItemsView:
        """
            Get the items view of the object (if supported)

            Returns:
                ItemsView: Items view of the object
        """
        ...
    def get(self, key: Any, default: Any = None) -> Any:
        """
            Get an item from the object (if supported)

            Parameters:
                key (Any): Key of the item to get
                default (Any): Default value to return if the key is not found (raise an error if not found)

            Returns:
                Any: Item from the object
        """
        ...
    def __list__(self) -> list[Any]:
        """
            Get the list version of the object (if supported)

            Returns:
                list[Any]: List
        """
        ...
    def to_dict(self) -> dict[Any, Any]:
        """
            Get the dict version of the object (if supported)

            Returns:
                dict[Any, Any]: Dict
        """
        ...
    def clone(self) -> JEImmutable[T]:
        """
            Clone the immutable object

            Returns:
                JEImmutable[T]: Copy of the object (still as immutable)
        """
        ...
    def __eq__(self, other: Any) -> JEBool:
        """
            Check if the object is equal to another object

            Parameters:
                other (Any): Object to be compared with

            Returns:
                JEBool: Whether the object is equal to another object
        """
        ...
