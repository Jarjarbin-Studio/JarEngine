# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
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
from uuid import uuid4 as _uuid4

##Metadata##
__author__ = 'Nathan Jarjarbin'
__email__ = 'nathan.amaraggi@epitech.eu'
__version__ = "1.10.3"
__config_version__ = "0.2.0"
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
_start_time = None
_session = _uuid4().hex

def _title_color(title):

    text = Interns.JTKExternConsole.Text.Text
    color = Interns.JTKExternConsole.ANSI.Color

    return color.rgb_fg(70, 160, 255) + text(str(title)) + color(color.C_RESET)

def _version_color(version):

    text = Interns.JTKExternConsole.Text.Text
    color = Interns.JTKExternConsole.ANSI.Color

    return color.rgb_fg(150, 150, 150) + text(str(version)) + color(color.C_RESET)

def init(project_path):
    global _start_time, _session

    _start_time = _datetime.now()

    project_path = project_path.removesuffix("/")

    Interns.Config.JEInternConfig.project_path = f"{project_path}"
    Interns.Config.JEInternConfig.config_path = f"{project_path}/.je-config"
    Interns.Config.JEInternConfig.state_path = f"{project_path}/.je-state"
    Interns.Log.JEInternLog.project_path = f"{project_path}"
    Interns.Log.JEInternLog.log_path = f"{project_path}/.je-log"

    Interns.Config.init_all()

    name = Interns.Config.get('project', 'PROJECT', 'name', str, "Unnamed Project")
    version = Interns.Config.get('project', 'PROJECT', 'version', str, "0.0.0")
    author = Interns.Config.get('project', 'AUTHOR', 'name', str, None)

    Interns.JTKExternConsole.Console.print(
        f"{_title_color(name)} {_version_color(version)} {(f'(by {author})' if author else "")}"
    )

    if not Interns.Config.get("state", "LAST_RUN", "clean_exit", bool, True):
        Interns.Helpers.warning("Previous run crashed")

    Interns.Config.set("engine", "ENGINE", "version", str(JEVersion_JarEngine))
    Interns.Config.set("engine", "CONFIG", "version", str(JEVersion_Config))
    Interns.Config.set("state", "LAST_RUN", "start", _start_time)
    Interns.Config.set("state", "LAST_RUN", "clean_exit", False)
    Interns.Config.set("state", "SESSION", "launches",  Interns.Config.get("state", "SESSION", "launches", int, 0) + 1)
    Interns.Config.set("state", "SESSION", "id", _session)
    Interns.Config._Checks.compatibility()

    log_levels = Interns.Log._log_levels
    Interns.Log._log_levels = log_levels[log_levels.index(Interns.Config.get('debug', 'LOG', 'level', str, "") or "INFO"):]

    if Interns.Helpers.enabled("debug", "LOG"):
        Interns.Log.JEInternLog(Interns.Config.get('debug', 'LOG', 'file', str, "tmp")).delete()
        Interns.Log.JEInternLog(Interns.Config.get('debug', 'LOG', 'file', str, "tmp") + "_cleaned").delete()
        Interns.Log.JEInternLog(Interns.Config.get('debug', 'LOG', 'file', str, "") or str(_start_time))

    ret = Interns.PGExtern.init()

    Interns.Log.log("INFO", "ENGINE", f"JarEngine version {JEVersion_JarEngine} initialized")
    Interns.Log.log("INFO", "ENGINE", f"Current session: {_session}")

    from jarengine import constants

    globals().update({
        name: getattr(constants, name)
        for name in constants.__all__
    })

    Interns.Log.save()

    return ret

def run(main, *args):
    ret = None

    try:
        ret = main(*args)
        Interns.Log.save()

    except Interns.JTKExternError.BaseError as error:
        Interns.Helpers.warning(error, True, False)
        print(Interns.JTKExternError.BaseError("An error occurred", error="Caught exception"))

        quit(False)
        exit(84)

    except Exception as error:
        Interns.Helpers.warning(error, True, False)
        print(Interns.JTKExternError.BaseError("An unexpected error occurred", error="Uncaught exception"))

        quit(False)
        exit(1)

    except (KeyboardInterrupt, SystemExit):
        error = Interns.JTKExternError.BaseError("Game interrupted", error="KeyboardInterrupt")
        Interns.Helpers.warning(error, False, False)

        quit()

    finally:
        return ret

def quit(_clean = True):
    global _session, _start_time

    if _start_time is not None and _session is not None:
        _end = _datetime.now()
        duration = (_end - _start_time).total_seconds()

        Interns.Config.set("state", "LAST_RUN", "end", _end)
        Interns.Config.set("state", "LAST_RUN", "duration", duration)

        total_runtime = Interns.Config.get("state", "STATISTICS", "total_runtime", float, 0.0)
        launches = Interns.Config.get("state", "SESSION", "launches", int, 1)
        longest_session = Interns.Config.get("state", "STATISTICS", "longest_session", float, 0.0)
        shortest_session = Interns.Config.get("state", "STATISTICS", "shortest_session", float, 0.0)

        new_total_runtime = total_runtime + duration
        average_session = new_total_runtime / launches

        if duration > longest_session:
            longest_session = duration

        if shortest_session == 0 or duration < shortest_session:
            shortest_session = duration

        Interns.Config.set("state", "STATISTICS", "total_runtime", new_total_runtime)
        Interns.Config.set("state", "STATISTICS", "average_session", average_session)
        Interns.Config.set("state", "STATISTICS", "longest_session", longest_session)
        Interns.Config.set("state", "STATISTICS", "shortest_session", shortest_session)

    Interns.Log.log("INFO", "ENGINE", "Engine quit")
    Interns.Log.save()
    Interns.Log.close()

    if _clean:
        Interns.Config.set("state", "LAST_RUN", "clean_exit", True)

    Interns.PGExtern.quit()

    _start_time = None
    _session = None

def _banner():

    Interns.JTKExternConsole.init(banner=False)

    ansi = Interns.JTKExternConsole.ANSI
    Interns.JTKExternConsole.Console.print(
        ansi.Line.clear_previous_line(2) +
        f"{_title_color("JarEngine")} {_version_color(JEVersion_JarEngine)} ({_title_color("PyGame")} {_version_color(JEVersion_PyGame)}, {_title_color("SDL")} {_version_color(JEVersion_SDL)}, {_title_color("Python")} {_version_color(JEVersion_Python)})"
    )

__all__ = [
    ## Special ##
    "__author__",
    "__email__",
    "__version__",
    "__config_version__",
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
    'run',
    'quit',
    ## Constants ##
    # Versions #
    'JEVersion_JarEngine',
    'JEVersion_Config',
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
