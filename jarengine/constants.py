"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.6
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

from jarengine.interns import PGExtern as _PGExtern
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.events.event import JEEventCode as _JEEventCode
from jarengine.events.keyboard import JEKeyCode as _JEKeyCode
from jarengine.events.mouse import JEMouseCode as _JEMouseCode
from jarengine.systems.version import JEVersion
from jarengine import __version__ as _jarengine_version
from sys import version_info as _python_version

# Versions #
_pygame_version = _PGExtern.version.vernum
_sdl_version = _PGExtern.version.SDL

JEVersion_JarEngine = JEVersion(*([int(v) for v in _jarengine_version.split('.') if v] + [0, 0, 0])[0:3])
JEVersion_PyGame = JEVersion(_pygame_version.major, _pygame_version.minor, _pygame_version.patch)
JEVersion_SDL = JEVersion(_sdl_version.major, _sdl_version.minor, _sdl_version.patch)
JEVersion_Python = JEVersion(*_python_version[0:3])

# Booleans #
JEFalse = _JEBool(0)
JETrue = _JEBool(1)

# Events #
JEEvtQuit = _JEEventCode(_PGExtern.QUIT)
JEEvtHidden = _JEEventCode(_PGExtern.HIDDEN)
JEEvtKeyDown = _JEEventCode(_PGExtern.KEYDOWN)
JEEvtKeyUp = _JEEventCode(_PGExtern.KEYUP)
JEEvtMouseDown = _JEEventCode(_PGExtern.MOUSEBUTTONDOWN)
JEEvtMouseUp = _JEEventCode(_PGExtern.MOUSEBUTTONUP)

# Keys #
JEKey_A = _JEKeyCode(_PGExtern.K_a)
JEKey_B = _JEKeyCode(_PGExtern.K_b)
JEKey_C = _JEKeyCode(_PGExtern.K_c)
JEKey_D = _JEKeyCode(_PGExtern.K_d)
JEKey_E = _JEKeyCode(_PGExtern.K_e)
JEKey_F = _JEKeyCode(_PGExtern.K_f)
JEKey_G = _JEKeyCode(_PGExtern.K_g)
JEKey_H = _JEKeyCode(_PGExtern.K_h)
JEKey_I = _JEKeyCode(_PGExtern.K_i)
JEKey_J = _JEKeyCode(_PGExtern.K_j)
JEKey_K = _JEKeyCode(_PGExtern.K_k)
JEKey_L = _JEKeyCode(_PGExtern.K_l)
JEKey_M = _JEKeyCode(_PGExtern.K_m)
JEKey_N = _JEKeyCode(_PGExtern.K_n)
JEKey_O = _JEKeyCode(_PGExtern.K_o)
JEKey_P = _JEKeyCode(_PGExtern.K_p)
JEKey_Q = _JEKeyCode(_PGExtern.K_q)
JEKey_R = _JEKeyCode(_PGExtern.K_r)
JEKey_S = _JEKeyCode(_PGExtern.K_s)
JEKey_T = _JEKeyCode(_PGExtern.K_t)
JEKey_U = _JEKeyCode(_PGExtern.K_u)
JEKey_V = _JEKeyCode(_PGExtern.K_v)
JEKey_W = _JEKeyCode(_PGExtern.K_w)
JEKey_X = _JEKeyCode(_PGExtern.K_x)
JEKey_Y = _JEKeyCode(_PGExtern.K_y)
JEKey_Z = _JEKeyCode(_PGExtern.K_z)
JEKey_0 = _JEKeyCode(_PGExtern.K_0)
JEKey_1 = _JEKeyCode(_PGExtern.K_1)
JEKey_2 = _JEKeyCode(_PGExtern.K_2)
JEKey_3 = _JEKeyCode(_PGExtern.K_3)
JEKey_4 = _JEKeyCode(_PGExtern.K_4)
JEKey_5 = _JEKeyCode(_PGExtern.K_5)
JEKey_6 = _JEKeyCode(_PGExtern.K_6)
JEKey_7 = _JEKeyCode(_PGExtern.K_7)
JEKey_8 = _JEKeyCode(_PGExtern.K_8)
JEKey_9 = _JEKeyCode(_PGExtern.K_9)
JEKey_Enter = _JEKeyCode(_PGExtern.K_RETURN)
JEKey_Backspace = _JEKeyCode(_PGExtern.K_BACKSPACE)
JEKey_Delete = _JEKeyCode(_PGExtern.K_DELETE)
JEKey_Tab = _JEKeyCode(_PGExtern.K_TAB)
JEKey_Escape = _JEKeyCode(_PGExtern.K_ESCAPE,)
JEKey_Up = _JEKeyCode(_PGExtern.K_UP)
JEKey_Down = _JEKeyCode(_PGExtern.K_DOWN)
JEKey_Left = _JEKeyCode(_PGExtern.K_LEFT)
JEKey_Right = _JEKeyCode(_PGExtern.K_RIGHT)

# Mouses #
JEMse_Left = _JEMouseCode(_PGExtern.BUTTON_LEFT)
JEMse_Middle = _JEMouseCode(_PGExtern.BUTTON_MIDDLE)
JEMse_Right = _JEMouseCode(_PGExtern.BUTTON_RIGHT)
