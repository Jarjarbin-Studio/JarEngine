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
    ## Imports ##
    'Interns',
    'Audios',
    'Entities',
    'Events',
    'Games',
    'Resources',
    'Systems',
    ## Functions ##
    'Init',
    'Quit',
    ## Constants ##
    'JEFalse',
    'JETrue',
    'JEEvtQuit',
    'JEEvtHidden',
    'JEEvtKeyDown',
    'JEEvtKeyUp',
    'JEEvtMouseDown',
    'JEEvtMouseUp',
    'JEKey_A',
    'JEKey_B',
    'JEKey_C',
    'JEKey_D',
    'JEKey_E',
    'JEKey_F',
    'JEKey_G',
    'JEKey_H',
    'JEKey_I',
    'JEKey_J',
    'JEKey_K',
    'JEKey_L',
    'JEKey_M',
    'JEKey_N',
    'JEKey_O',
    'JEKey_P',
    'JEKey_Q',
    'JEKey_R',
    'JEKey_S',
    'JEKey_T',
    'JEKey_U',
    'JEKey_V',
    'JEKey_V',
    'JEKey_W',
    'JEKey_X',
    'JEKey_Y',
    'JEKey_Z',
    'JEKey_0',
    'JEKey_1',
    'JEKey_2',
    'JEKey_3',
    'JEKey_4',
    'JEKey_5',
    'JEKey_6',
    'JEKey_7',
    'JEKey_8',
    'JEKey_9',
    'JEKey_Enter',
    'JEKey_Backspace',
    'JEKey_Delete',
    'JEKey_Tab',
    'JEKey_Escape',
    'JEKey_Up',
    'JEKey_Down',
    'JEKey_Left',
    'JEKey_Right',
    'JEMse_Left',
    'JEMse_Middle',
    'JEMse_Right'
]

##Imports##
import sources.interns as Interns
import sources.audios as Audios
import sources.entities as Entities
import sources.events as Events
import sources.games as Games
import sources.resources as Resources
import sources.systems as Systems
from sources.constants import *

##Functions##
def Init() -> tuple[int, int]:
    return Interns.PGIntern.init()

def Quit() -> None:
    Interns.PGIntern.quit()
