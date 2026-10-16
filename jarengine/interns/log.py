# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v2
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

import re
from typing import final as _final

from jarbin_toolkit_log import (
    Log as _JTKExternLog,
    LogLevel as _LogLevel,
    LogType as _LogType,
)

from jarengine.interns.config import get as _get
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.interns.decorators import documentation as _documentation

_current_log = None
_log_levels = ["DEBUG", "INFO", "NOTICE", "WARN", "ERROR", "CRIT"]
_ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


@_documentation
@_final
class JEInternLog(_JTKExternLog, _JEInternBaseClass):

    project_path = None
    log_path = None

    def __init__(self, name, _session):
        from jarengine.interns.helpers import enabled as _enabled
        from jarengine.interns.config import get as _get

        global _current_log

        self._enabled = _enabled

        excluded = _get("debug", "LOG", "excluded", str, [])
        self._excluded = [
            entry.lower()
            for entry in (
                excluded.split(";") if excluded else []
            )
        ]

        if not self._enabled("debug", "LOG"):
            return

        if not JEInternLog.project_path or not JEInternLog.log_path:
            raise _JTKExternError.JErrorRuntime(
                "JarEngine.init(path) must be called first"
            )

        _JTKExternLog.__init__(
            self,
            JEInternLog.log_path,
            name,
            type=_LogType.JAR_LOG,
            metadata={
                "application": _get('project', 'PROJECT', 'name', str, "Unnamed Project"),
                "version": _get('project', 'PROJECT', 'version', str, "0.0.0"),
            },
            run_id=_session,
        )
        _JEInternBaseClass.__init__(self)

        _current_log = self

def _clean_text(text):
    if isinstance(text, _JTKExternError.BaseJError):
        return f"{text.error}{''.join([f'\n    {line}' for line in text.message.removeprefix("\n").split("\n")])}"
    text.strip().replace("  ", " ")
    if "\033" in text:
        return _ansi_escape.sub("", text)
    return text

def log(status, title, description, jeid=None, *values):
    if _current_log is None:
        return

    status = status.upper()
    title = title.upper()
    description = _clean_text(description)

    _description = description.lower()

    for word in _current_log._excluded:
        if word and word in _description:
            return

    if (
        jeid is not None
        and _current_log._enabled("debug", "LOG", "show_jeid")
    ):
        description += f" (JEID:{jeid})"

    if (
        values
        and _current_log._enabled("debug", "LOG", "show_values")
    ):
        description += f" (VALUES:{', '.join(map(repr, values))})"

    if (
        status not in _log_levels
        or not _current_log._enabled(
            "debug",
            "LOG - CATEGORY",
            title.lower(),
        )
    ):
        return

    _current_log.log(
        _LogLevel(status),
        description,
        scope=title,
    )

def comment(string):
    if _current_log is not None:
        _current_log.comment(_clean_text(string))


def save():
    if _current_log is None:
        return

    _current_log.flush()

def close():
    global _current_log

    if _current_log is None:
        return

    current_log = _current_log

    if current_log._enabled("debug", "LOG", "clean"):
        # Cleaning must be reimplemented for the new jar-log format.
        pass

    current_log.close()
    _current_log = None
