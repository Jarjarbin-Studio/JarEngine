# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v2
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

import inspect
import sys
from os.path import exists, join
from pathlib import Path

from jarengine.interns.config import (
    get as _get,
    JEInternConfig as _JEInternConfig
)
from jarengine.interns import JTKExternError as _JTKExternError
import jarengine.interns.log as _log

_ENGINE_ROOT = Path(__file__).resolve().parents[1]

def _exception_handler(exc_type, exc, traceback):
    if issubclass(exc_type, _JTKExternError.BaseJError):
        print(exc)
    else:
        sys.__excepthook__(exc_type, exc, traceback)

sys.excepthook = _exception_handler

def _caller_location(depth = 2):
    frame = inspect.currentframe()

    for _ in range(depth):
        if frame is None:
            return []

        frame = frame.f_back

    user_frames = []
    engine_frames = []

    while frame:
        filename = Path(frame.f_code.co_filename).resolve()
        location = (filename, frame.f_lineno)

        try:
            filename.relative_to(_ENGINE_ROOT)
            engine_frames.append(location)

        except ValueError:
            user_frames.append(location)

        frame = frame.f_back

    if not user_frames:
        return engine_frames[:1]

    if _get("engine", "ENGINE", "error_traceback", bool, False):
        return user_frames + engine_frames

    return user_frames[:1]

def _link_data(location):
    if location is None:
        return None

    filename, line = location

    return {
        "file": str(filename),
        "line": line,
    }


def _set_error_link(err, location):
    if location is not None:
        err._link = _JTKExternError._ErrorLink(**_link_data(location))

    return err

def _links_to_string(links):
    strings = []

    for link in links:
        strings.append(f"File {link[0]}, line {link[1]}")

    return strings

def traceback(links):
    if not links:
        return

    err = _JTKExternError.BaseJError(
        f'{"\n".join(_links_to_string(links))}\n↓↓↓↓↓',
        error="JarEngine Traceback",
        link=_link_data(links[0]),
    )

    _log.log("WARN", "ENGINE", "A traceback has been generated")
    _log.comment(err)
    _log.save()

    print(err)

def error(err, do_traceback=True, _error_title=True):
    mode = _get("engine", "ENGINE", "exception_mode", str, "strict")

    if mode == "silent":
        return

    if mode == "warning":
        warning(err, do_traceback, _warn_title=_error_title)
        return

    if mode != "strict":
        return

    links = _caller_location()

    if len(links) > 1 and do_traceback:
        traceback(links[1:])

    location = links[0] if links and do_traceback else None

    if isinstance(err, _JTKExternError.BaseJError):
        err.message = f"{err.message.strip()}"
        err.error = f"{'ERROR - ' if _error_title else ''}{err.error}"
        _set_error_link(err, location)
    else:
        err = _JTKExternError.BaseJError(
            f"{str(err).strip()}",
            error="ERROR",
            link=_link_data(location),
        )

    _log.comment(err)
    _log.save()

    raise err

def warning(err, do_traceback=False, _warn_title=True):
    if _get("engine", "ENGINE", "exception_mode", str, "strict") == "silent":
        return

    links = _caller_location()

    if len(links) > 1 and do_traceback:
        traceback(links[1:])

    location = links[0] if links and do_traceback else None

    if isinstance(err, _JTKExternError.BaseJError):
        err.message = f"{err.message.strip()}"
        err.error = f"{'WARNING - ' if _warn_title else ''}{err.error}"
        _set_error_link(err, location)
    else:
        err = _JTKExternError.BaseJError(
            f"{str(err).strip()}",
            error="WARNING",
            link=_link_data(location),
        )

    _log.comment(err)
    _log.save()

    print(err)

def assertion(condition, message, strict = False, do_traceback = True, _depth = 2):
    if not condition:

        err = _JTKExternError.BaseJError(f"{message}", error = "ErrorAssertion")

        if strict or _get("engine", "ENGINE", "safe_mode", bool, True):
            error(err, do_traceback)
        else:
            warning(err, do_traceback)

        _log.log("WARN", "CORE", f"Assertion failed: {message}")
        _log.comment(err)
        _log.save()

def assertion_type(value, _type, message, strict = False, do_traceback = True):
    assertion(isinstance(value, _type), f"{message} (current: {type(value).__name__})", strict, do_traceback, _depth=3)
    return value

def assertion_class(value, _class, message, strict = False, do_traceback = True):
    assertion(issubclass(value, _class), f"{message} (current: {value.__name__})", strict, do_traceback, _depth=3)
    return value

def enabled(config, section, setting = "enabled"):
    return _get(config, section, setting, bool, False)

def project_path(*paths):
    return join(_JEInternConfig.project_path, *paths)

def asset_path(*paths):
    base = _get("assets", "ASSETS", "path")

    return join(base, *paths)

def require_exists(path):
    if not exists(path):
        error(
            _JTKExternError.JErrorFileNotFound(
                f"Missing resource: {path}"
            )
        )


def validate_value(value, allowed, name):
    if value not in allowed:
        error(
            _JTKExternError.JErrorValue(
                f"\nInvalid {name}: {value}"
            )
        )

def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))

def safe_mode():
    return _get("engine", "ENGINE", "safe_mode", bool, False)

def error_handling():
    try:
        return _get("engine", "ENGINE", "error_handling", bool, True)
    except _JTKExternError.BaseJError:
        return False

def debug_enabled(feature=None):
    if not _get("debug", "DEBUG", "enabled", bool, False):
        return False

    if feature:
        return _get("debug", "DISPLAY", feature, bool, False)

    return True

def version(config, section, key):
    from jarengine.systems.version import JEVersion as _JEVersion

    return _JEVersion(*[int(v) for v in _get(config, section, key).split(".")])

def safe_cast(value, _type):
    if error_handling():
        try:
            return _type(value)
        except (TypeError, ValueError):
            error(_JTKExternError.JErrorType(f"\nCast failed due to invalid type"))
            return value
    return _type(value)
