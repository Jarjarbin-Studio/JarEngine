# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
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

from datetime import datetime as _datetime

##Metadata##
__author__ = 'Nathan Jarjarbin'
__email__ = 'nathan.amaraggi@epitech.eu'
__version__ = "1.8.0"
__license__ = "GPL"

##Imports##
import jarengine.interns as Interns
import jarengine.entity as Entity
import jarengine.events as Events
import jarengine.games as Games
import jarengine.resources as Resources
import jarengine.systems as Systems
import jarengine.widgets as Widgets
from jarengine.constants import *

##Special##
_start_time: _datetime | None = None

def init(project_path) -> tuple[int, int]:
    global _start_time

    _start_time = _datetime.now()

    Interns.Config.JEInternConfig.project_path = f"{project_path.removesuffix("/")}"
    Interns.Config.JEInternConfig.config_path = f"{Interns.Config.JEInternConfig.project_path}/.je-config"
    Interns.Config.init_all()
    Interns.JTKExternConsole.init(banner=False)
    return Interns.PGExtern.init()

def quit():
    if _start_time is not None:
        duration = _datetime.now() - _start_time
        Interns.Config.set('session', 'LAST_RUN', 'duration', str(duration))
    Interns.PGExtern.quit()

def _banner():
    ansi = Interns.JTKExternConsole.ANSI
    Interns.JTKExternConsole.Console.print(
        ansi.Line.clear_previous_line(2).s +
        f"JarEngine {JEVersion_JarEngine} (PyGame {JEVersion_PyGame}, SDL {JEVersion_SDL}, Python {JEVersion_Python})"
    )

__all__ = [
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

_banner()
