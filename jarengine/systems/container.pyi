from __future__ import annotations

from typing import TypeVar, Optional, Iterator, Any, Generic

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.systems.bool import JEBool

T = TypeVar("T", bound=JEInternBaseClass)

class JEContainer(Generic[T], JEInternBaseClass):
    def __init__(self, allowed_type: type, allow_subclass: JEBool = JEBool(0)):
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
                obj (<allowed_type>): Object to add
        """
        ...
    def __getitem__(self, value: str | T | type) -> T:
        """
            Get an item from the container (automatically reroute to the proper getter)
            
            Parameters:
                value (str | type | <allowed_type>): Name / JEID / instance / type of the object
            
            Returns:
                <allowed_type>: Object
        """
        ...
    def get(self, *, name: Optional[str] = None, jeid: Optional[str] = None, instance: Optional[T] = None, _type: Optional[type] = None, default: Any = NotImplemented) -> T:
        """
            Get an item from the container

            Parameters:
                name (Optional[str]) = None: Name of the object
                jeid (Optional[str]) = None: JEID of the object
                instance (Optional[<allowed_type>]) = None: instance
                _type (Optional[type]) = None: Type of the object
                default (Any) = NotImplemented: Default value to return if object not found (raise an error if leaved as such)

            Returns:
                <allowed_type>: Object
        """
        ...
    def rm(self, *, name: Optional[str] = None, jeid: Optional[str] = None, instance: Optional[T] = None, _type: Optional[type] = None) -> T:
        """
            Remove an item from the container

            Parameters:
                name (Optional[str]) = None: Name of the object
                jeid (Optional[str]) = None: JEID of the object
                instance (Optional[<allowed_type>]) = None: instance
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
                Iterator[<allowed_type>]: Iterator of objects
        """
        ...
    @property
    def data(self) -> dict[str, T]:
        """
            Get the raw data of the container

            Returns:
                dict[str, <allowed_type>]: Dictionary of objects
        """
        ...
