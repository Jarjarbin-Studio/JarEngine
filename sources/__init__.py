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

__all__ = [
    ##Imports##
    #Interns
    'Interns',
    #Audios
    #Games
    "JEGame",
    "JEWindow",
    "EventManager",
    "Event",
    "Keyboard",
    "Mouse",
    #Graphics
    'JESprite',
    'JETexture',
    #Systems
    'Vector',
    'JEColor',
    'JEBool',
    'JEContainer',
    'JEImmutable',
    ##Functions##
    'Init',
    'Quit',
    ##Shortcuts##
    'JETrue',
    'JEFalse'
]

##Imports##
import sources.interns as Interns
from sources.audios import *
from sources.games import *
from sources.graphics import *
from sources.systems import *

##Functions##
def Init() -> tuple[int, int]:
    return interns.PGIntern.init()

def Quit() -> None:
    interns.PGIntern.quit()

##Shortcuts##
JEFalse: JEBool = JEBool(0)
JETrue: JEBool = JEBool(1)
