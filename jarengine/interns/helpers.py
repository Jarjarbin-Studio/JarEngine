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

from os.path import exists, join

from jarengine.interns.config import (
    get as _get,
    JEInternConfig as _JEInternConfig
)
from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.systems.version import JEVersion as _JEVersion

def assertion(condition, message):
    if not condition:
        error = _JTKExternError.BaseError(f"\n{message}", error = "ErrorAssertion")

        if _get("engine", "ENGINE", "safe_mode", bool, False):
            raise error
        print(error)

def error(err):
    mode = _get("engine", "ENGINE", "exception_mode", str, "strict")

    if mode == "strict":
        raise err

    elif mode == "warning":
        if isinstance(err, _JTKExternError.BaseError):
            print(err)
        else:
            _JTKExternError.BaseError(str(err), error = "WARNING")

def warning(message):
    if _get("engine", "ENGINE", "exception_mode", str, "strict") != "silent":
        print(_JTKExternError.BaseError(f"\n{message}", error="Warning"))

def enabled(config, section, setting = "enabled"):
    return _get(config, section, setting, bool, False)

def project_path(*paths):
    return join(_JEInternConfig.project_path, *paths)

def asset_path(*paths):
    base = _get("assets", "ASSETS", "path")

    return join(base, *paths)

def require_exists(path):
    if not exists(path):
        raise _JTKExternError.Special.ErrorSpecialConfig(f"\nMissing resource: {path}")

def validate_value(value, allowed, name):
    if value not in allowed:
        raise _JTKExternError.Error.ErrorValue(f"\nInvalid {name}: {value}")

def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))

def safe_mode():
    return _get("engine", "ENGINE", "safe_mode", bool, False)

def debug_enabled(feature=None):
    if not _get("debug", "DEBUG", "enabled", bool, False):
        return False

    if feature:
        return _get("debug", "DISPLAY", feature, bool, False)

    return True

def version(config, section, key):
    return _JEVersion(*[int(v) for v in _get(config, section, key).split(".")])
