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

from __future__ import annotations

import inspect
from os.path import exists, join
from pathlib import Path

from jarengine.interns.config import (
    get as _get,
    JEInternConfig as _JEInternConfig, JEInternConfig
)
from jarengine.interns import JTKExternError as _JTKExternError


_ENGINE_ROOT = Path(__file__).resolve().parents[1]


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

def _links_to_string(links):
    strings = []

    for link in links:
        strings.append(f"File {link[0]}, line {link[1]}")

    return strings

def traceback(links):
    if not links:
        return

    print(
        _JTKExternError.BaseError(
            f'\n{"\n".join(_links_to_string(links))}',
            error="JarEngine Traceback"
        )
    )

def error(err):
    mode = _get("engine", "ENGINE", "exception_mode", str, "strict")

    if mode == "strict":
        links = _caller_location()
        traceback(links)
        raise err

    elif mode == "warning":
        links = _caller_location()

        if len(links) > 1:
            traceback(links[1:])

        if isinstance(err, _JTKExternError.BaseError):
            err.error = f"WARNING - {err.error}"
            err.link_data = links[0] if len(links) > 1 else None
            err.create_link()
            print(err)
        else:
            print(_JTKExternError.BaseError(f"\n{err.strip()}", error = "WARNING", link = links[0] if len(links) > 1 else None))

def warning(err):
    if _get("engine", "ENGINE", "exception_mode", str, "strict") != "silent":
        links = _caller_location()

        if len(links) > 1:
            traceback(links[1:])

        if isinstance(err, _JTKExternError.BaseError):
            err.error = f"WARNING - {err.error}"
            err.link_data = links[0] if len(links) > 1 else None
            err.create_link()
            print(err)
        else:
            print(_JTKExternError.BaseError(f"{err.strip()}", error = "WARNING", link = links[0] if len(links) > 1 else None))

def assertion(condition, message, strict = False, _depth = 2):
    if not condition:

        links = _caller_location(_depth)

        err = _JTKExternError.BaseError(f"{message}", error = "ErrorAssertion", link = links[0] if len(links) > 1 else None)

        if strict or _get("engine", "ENGINE", "safe_mode", bool, True):
            error(err)
        else:
            if len(links) > 1:
                traceback(links[1:])

            print(err)

def assertion_type(value, _type, message, strict = False):
    assertion(isinstance(value, _type), f"{message} (current: {type(value).__name__})", strict, _depth=3)
    return value

def assertion_class(value, _class, message, strict = False):
    assertion(issubclass(value, _class), f"{message} (current: {value.__name__})", strict, _depth=3)
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
        links = _caller_location()

        error(_JTKExternError.Special.ErrorSpecialConfig(f"\nMissing resource: {path}", link = links[0]))

def validate_value(value, allowed, name):
    if value not in allowed:
        links = _caller_location()

        error(_JTKExternError.Error.ErrorValue(f"\nInvalid {name}: {value}", link = links[0]))

def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))

def safe_mode():
    return _get("engine", "ENGINE", "safe_mode", bool, False)

def error_handling():
    try:
        return _get("engine", "ENGINE", "error_handling", bool, True)
    except _JTKExternError.BaseError:
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
            error(_JTKExternError.Error.ErrorType(f"\nCast failed due to invalid type"))
            return value
    return value
