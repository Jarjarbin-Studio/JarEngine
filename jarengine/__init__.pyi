# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
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

"""
JarEngine core module.

Provides the main interface of the engine, including game management,
systems, entities, resources, events, and engine-wide utilities.
"""

from __future__ import annotations

# Public API
from . import interns as Interns
from . import entity as Entity
from . import events as Events
from . import games as Games
from . import resources as Resources
from . import systems as Systems
from . import widgets as Widgets

def init(project_path: str) -> tuple[int, int]:
    """
        Initialize the engine and set the different configurations paths

        Parameters:
            project_path (str): The path of the current project (full path from root, not local path)

        Returns:
            tuple[int, int]: PyGame numpass, numfail
    """
    ...
def quit():
    """
        Quit the engine
    """
    ...

# Constants
from .constants import *

__author__: str
__email__: str
__version__: str
__license__: str

__all__: list[str] = [
    ## Special ##
    "__author__",
    "__email__",
    "__version__",
    "__license__",
    ## Imports ##
    'Interns',
    'Entity',
    'Events',
    'Games',
    'Resources',
    'Systems',
    'Widgets',
    ## Functions ##
    'init',
    'quit',
    ## Constants ##
    # Versions #
    'JEVersion_JarEngine',
    'JEVersion_PyGame',
    'JEVersion_SDL',
    'JEVersion_Python',
    # Booleans #
    'JEFalse',
    'JETrue',
    # Events #
    'JEEvtQuit',
    'JEEvtHidden',
    'JEEvtKeyDown',
    'JEEvtKeyUp',
    'JEEvtMouseDown',
    'JEEvtMouseUp',
    # Keys #
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
    'JEKey_Space',
    'JEKey_Backspace',
    'JEKey_Delete',
    'JEKey_Tab',
    'JEKey_Escape',
    'JEKey_Up',
    'JEKey_Down',
    'JEKey_Left',
    'JEKey_Right',
    # Mouses #
    'JEMse_Left',
    'JEMse_Middle',
    'JEMse_Right'
]
