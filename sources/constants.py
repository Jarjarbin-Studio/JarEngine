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

from sources.interns import PGIntern as _PGIntern
from sources.systems.bool import JEBool as _JEBool
from sources.events.event import JEEventCode as _JEEventCode
from sources.events.keyboard import JEKeyCode as _JEKeyCode
from sources.events.mouse import JEMouseCode as _JEMouseCode

# Bools #
JEFalse: _JEBool = _JEBool(0)
JETrue: _JEBool = _JEBool(1)

# Events #
JEEvtQuit: _JEEventCode = _JEEventCode(_PGIntern.QUIT)
JEEvtHidden: _JEEventCode = _JEEventCode(_PGIntern.HIDDEN)
JEEvtKeyDown: _JEEventCode = _JEEventCode(_PGIntern.KEYDOWN)
JEEvtKeyUp: _JEEventCode = _JEEventCode(_PGIntern.KEYUP)
JEEvtMouseDown: _JEEventCode = _JEEventCode(_PGIntern.MOUSEBUTTONDOWN)
JEEvtMouseUp: _JEEventCode = _JEEventCode(_PGIntern.MOUSEBUTTONUP)

# Keys #
JEKey_A: _JEKeyCode = _JEKeyCode(_PGIntern.K_a)
JEKey_B: _JEKeyCode = _JEKeyCode(_PGIntern.K_b)
JEKey_C: _JEKeyCode = _JEKeyCode(_PGIntern.K_c)
JEKey_D: _JEKeyCode = _JEKeyCode(_PGIntern.K_d)
JEKey_E: _JEKeyCode = _JEKeyCode(_PGIntern.K_e)
JEKey_F: _JEKeyCode = _JEKeyCode(_PGIntern.K_f)
JEKey_G: _JEKeyCode = _JEKeyCode(_PGIntern.K_g)
JEKey_H: _JEKeyCode = _JEKeyCode(_PGIntern.K_h)
JEKey_I: _JEKeyCode = _JEKeyCode(_PGIntern.K_i)
JEKey_J: _JEKeyCode = _JEKeyCode(_PGIntern.K_j)
JEKey_K: _JEKeyCode = _JEKeyCode(_PGIntern.K_k)
JEKey_L: _JEKeyCode = _JEKeyCode(_PGIntern.K_l)
JEKey_M: _JEKeyCode = _JEKeyCode(_PGIntern.K_m)
JEKey_N: _JEKeyCode = _JEKeyCode(_PGIntern.K_n)
JEKey_O: _JEKeyCode = _JEKeyCode(_PGIntern.K_o)
JEKey_P: _JEKeyCode = _JEKeyCode(_PGIntern.K_p)
JEKey_Q: _JEKeyCode = _JEKeyCode(_PGIntern.K_q)
JEKey_R: _JEKeyCode = _JEKeyCode(_PGIntern.K_r)
JEKey_S: _JEKeyCode = _JEKeyCode(_PGIntern.K_s)
JEKey_T: _JEKeyCode = _JEKeyCode(_PGIntern.K_t)
JEKey_U: _JEKeyCode = _JEKeyCode(_PGIntern.K_u)
JEKey_V: _JEKeyCode = _JEKeyCode(_PGIntern.K_v)
JEKey_W: _JEKeyCode = _JEKeyCode(_PGIntern.K_w)
JEKey_X: _JEKeyCode = _JEKeyCode(_PGIntern.K_x)
JEKey_Y: _JEKeyCode = _JEKeyCode(_PGIntern.K_y)
JEKey_Z: _JEKeyCode = _JEKeyCode(_PGIntern.K_z)
JEKey_0: _JEKeyCode = _JEKeyCode(_PGIntern.K_0)
JEKey_1: _JEKeyCode = _JEKeyCode(_PGIntern.K_1)
JEKey_2: _JEKeyCode = _JEKeyCode(_PGIntern.K_2)
JEKey_3: _JEKeyCode = _JEKeyCode(_PGIntern.K_3)
JEKey_4: _JEKeyCode = _JEKeyCode(_PGIntern.K_4)
JEKey_5: _JEKeyCode = _JEKeyCode(_PGIntern.K_5)
JEKey_6: _JEKeyCode = _JEKeyCode(_PGIntern.K_6)
JEKey_7: _JEKeyCode = _JEKeyCode(_PGIntern.K_7)
JEKey_8: _JEKeyCode = _JEKeyCode(_PGIntern.K_8)
JEKey_9: _JEKeyCode = _JEKeyCode(_PGIntern.K_9)
JEKey_Enter: _JEKeyCode = _JEKeyCode(_PGIntern.K_RETURN)
JEKey_Backspace: _JEKeyCode = _JEKeyCode(_PGIntern.K_BACKSPACE)
JEKey_Delete: _JEKeyCode = _JEKeyCode(_PGIntern.K_DELETE)
JEKey_Tab: _JEKeyCode = _JEKeyCode(_PGIntern.K_TAB)
JEKey_Escape: _JEKeyCode = _JEKeyCode(_PGIntern.K_ESCAPE,)
JEKey_Up: _JEKeyCode = _JEKeyCode(_PGIntern.K_UP)
JEKey_Down: _JEKeyCode = _JEKeyCode(_PGIntern.K_DOWN)
JEKey_Left: _JEKeyCode = _JEKeyCode(_PGIntern.K_LEFT)
JEKey_Right: _JEKeyCode = _JEKeyCode(_PGIntern.K_RIGHT)

# Mouses #
JEMouse_Left: _JEMouseCode = _JEMouseCode(_PGIntern.BUTTON_LEFT)
JEMouse_Middle: _JEMouseCode = _JEMouseCode(_PGIntern.BUTTON_MIDDLE)
JEMouse_Right: _JEMouseCode = _JEMouseCode(_PGIntern.BUTTON_RIGHT)
