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

from typing import Callable, Optional, Iterator

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.games.game import JEGame
from jarengine.events.manager import JEEvent
from jarengine.systems.bool import JEBool

class JEEventCode(JEInternBaseClass):
    def __init__(self, event: Optional[int]):
        """
            JEEventCode

            Parameters:
                event (Optional[int]): Event code
        """
        ...
    def __int__(self) -> int:
        """
            Get event code

            Returns:
                int: Event code
        """
        ...
    def __str__(self) -> str:
        """
        Get event name

            Returns:
                str: Event name
        """
        ...
    @property
    def name(self) -> str:
        """
        Get event name

            Returns:
                str: Event name
        """
        ...
    def __or__(self, other: JEEventCode) -> JEEventCodeGroup:
        """
        Create event group out of "Event1 | Event2"

            Parameters:
                other (JEEventCode): Events to store together

            Returns:
                JEEventCodeGroup: Event group
        """
        ...
    def __eq__(self, other: JEEventCode) -> JEBool:
        """
        Compare 2 events

            Parameters:
                other (JEEventCode): Event to compare with

            Returns:
                JEBool: True if they are equal, False otherwise
        """
        ...
    def __hash__(self) -> int:
        """
        Hash event (for future use)

            Returns:
                int: Event code hash
        """
        ...

class JEEventCodeGroup(JEInternBaseClass):
    def __init__(self, events: list[JEEventCode]):
        """
            JEEventCodeGroup

            Parameters:
                events (list[JEEventCode]): Events to store together
        """
        ...
    def __or__(self, other: JEEventCode | JEEventCodeGroup) -> JEEventCodeGroup:
        """
        Create event group out of "Event1 | Event2 | Event3"

            Parameters:
                other (JEEventCode | JEEventCodeGroup): Events to store together

            Returns:
                JEEventCodeGroup: Event group
        """
        ...
    def __iter__(self) -> Iterator[JEEventCode]:
        """
        Iterate over events

            Returns:
                Iterator[JEEventCode]: Iterator
        """
        ...
    @property
    def events(self) -> list[JEEventCode]:
        """
        Get events

            Returns:
                list[JEEventCode]: List of events
        """
        ...

class JEEventWatcher(JEInternBaseClass):
    def __init__(self, on: JEEventCode | list[JEEventCode] | JEEventCodeGroup, do: Callable[[JEGame, JEEvent], None]):
        """
            JEEventWatcher

            Parameters:
                on (JEEventCode | list[JEEventCode] | JEEventCodeGroup): Trigger event(s)
                do (Callable[[JEGame, JEEvent], None]): Action to do once triggered
        """
        ...
    def match(self, event: JEEvent) -> bool:
        """
            Look for a match of the events with the event

            Parameters:
                event (JEEvent): Event to look for

            Returns:
                bool: True if event matches, False otherwise
        """
        ...
    def __call__(self, game: JEGame, event: JEEvent):
        """
            Call the "do" function of the watcher
            
            Parameters:
                game (JEGame): Game
                event (JEEvent): Current Event
        """
        ...
    @property
    def on(self) -> JEEventCodeGroup:
        """
            Get the "on" event group of the watcher

            Returns:
                JEEventCodeGroup: Event group
        """
        ...
    @property
    def do(self) -> str:
        """
            Get the string representation of the "do" function of the watcher

            Returns:
                str: String representation
        """
        ...
