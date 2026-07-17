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

from jarengine.systems.bool import JEBool
from jarengine.events.event import JEEventCode
from jarengine.events.keyboard import JEKeyCode
from jarengine.events.mouse import JEMouseCode
from jarengine.systems.version import JEVersion

# Versions #
JEVersion_JarEngine: JEVersion
JEVersion_PyGame: JEVersion
JEVersion_SDL: JEVersion
JEVersion_Python: JEVersion

# Booleans #
JEFalse: JEBool
JETrue: JEBool

# Events #
JEEvtQuit: JEEventCode
JEEvtHidden: JEEventCode
JEEvtKeyDown: JEEventCode
JEEvtKeyUp: JEEventCode
JEEvtMouseDown: JEEventCode
JEEvtMouseUp: JEEventCode

# Keys #
JEKey_A: JEKeyCode
JEKey_B: JEKeyCode
JEKey_C: JEKeyCode
JEKey_D: JEKeyCode
JEKey_E: JEKeyCode
JEKey_F: JEKeyCode
JEKey_G: JEKeyCode
JEKey_H: JEKeyCode
JEKey_I: JEKeyCode
JEKey_J: JEKeyCode
JEKey_K: JEKeyCode
JEKey_L: JEKeyCode
JEKey_M: JEKeyCode
JEKey_N: JEKeyCode
JEKey_O: JEKeyCode
JEKey_P: JEKeyCode
JEKey_Q: JEKeyCode
JEKey_R: JEKeyCode
JEKey_S: JEKeyCode
JEKey_T: JEKeyCode
JEKey_U: JEKeyCode
JEKey_V: JEKeyCode
JEKey_W: JEKeyCode
JEKey_X: JEKeyCode
JEKey_Y: JEKeyCode
JEKey_Z: JEKeyCode
JEKey_0: JEKeyCode
JEKey_1: JEKeyCode
JEKey_2: JEKeyCode
JEKey_3: JEKeyCode
JEKey_4: JEKeyCode
JEKey_5: JEKeyCode
JEKey_6: JEKeyCode
JEKey_7: JEKeyCode
JEKey_8: JEKeyCode
JEKey_9: JEKeyCode
JEKey_Enter: JEKeyCode
JEKey_Space: JEKeyCode
JEKey_Backspace: JEKeyCode
JEKey_Delete: JEKeyCode
JEKey_Tab: JEKeyCode
JEKey_Escape: JEKeyCode
JEKey_Up: JEKeyCode
JEKey_Down: JEKeyCode
JEKey_Left: JEKeyCode
JEKey_Right: JEKeyCode

# Mouses #
JEMse_Left: JEMouseCode
JEMse_Middle: JEMouseCode
JEMse_Right: JEMouseCode
