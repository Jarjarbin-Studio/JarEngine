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

from collections import OrderedDict
import re
from os.path import exists
from os import mkdir
from typing import final as _final

from jarbin_toolkit_log import Log as _JTKExternLog

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.interns.decorators import documentation as _documentation

_current_log = None
_log_levels = ["DEBUG", "INFO", "VALID", "WARN", "ERROR", "CRIT"]
_ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

@_documentation
@_final
class JEInternLog(_JTKExternLog, _JEInternBaseClass):

    project_path = None
    log_path = None

    def __init__(self, name):
        from jarengine.interns.helpers import enabled as _enabled
        from jarengine.interns.config import get as _get

        global _current_log

        self._enabled = _enabled

        excluded = _get("debug", "LOG", "excluded", str, [])
        self._excluded = [e.lower() for e in (excluded.split(";") if excluded else excluded)]

        if not self._enabled("debug", "LOG"):
            return

        log_path = JEInternLog.log_path

        if (not JEInternLog.project_path) or (not JEInternLog.log_path):
            raise _JTKExternError.State.ErrorStateNotInitialized("\nJarEngine.init(path) must be called first")
        if not exists(log_path):
            mkdir(log_path)

        super().__init__(
            log_path,
            file_name=f"je-log-{name}"
        )

        _current_log = self

        self.comment("#############################")
        self.comment("###     JarEngine Log     ###")
        self.comment("#############################")

        self._buffer = []

        def _log_to_buffer(log):
            self._buffer.append(log)

        self._func = _log_to_buffer

    @property
    def buffer(self):
        b = self._buffer
        self._buffer = []
        return b

def _clean_text(text):
    if isinstance(text, _JTKExternError.BaseError):
        return f"{text.error}\n{text.message[1:]}"
    text.strip().replace("  ", " ")
    if "\033" in text:
        return _ansi_escape.sub("", text)
    return text

def log(status, title, description, jeid = None, *values):

    if _current_log is None:
        return

    status = status.upper()
    title = title.upper()
    description = _clean_text(description)
    _description = description.lower()

    for word in _current_log._excluded:
        if _description.startswith(word) or word in _description:
            return

    if jeid is not None and _current_log._enabled("debug", "LOG", "show_jeid"):
        description += f" (JEID:{jeid})"

    if len(values) > 0 and _current_log._enabled("debug", "LOG", "show_values"):
        description += f" (VALUES:{', '.join(map(lambda e: repr(e), values))})"

    if status in _log_levels and _current_log._enabled("debug", "LOG - CATEGORY", title.lower()):
        _current_log.log(status, title, description, _current_log._func)

def comment(string):
    if _current_log is not None:
        _current_log.comment(_clean_text(string), _current_log._func)

def save():
    if _current_log is not None:
        _current_log.save_batch(_current_log.buffer)

def clean():
    if _current_log is None:
        return

    log = _current_log.read()

    start = log.index("---START---") + len("---START---")
    end = log.index("----END----")

    lines = [
        line
        for line in log[start:end].splitlines()
        if line.strip()
    ]

    cleaned = []

    creation_group = OrderedDict()
    creation_header = None

    def flush_creation_group():
        nonlocal creation_header

        if not creation_group:
            return

        timestamp = next(iter(creation_group.values()))["timestamp"]

        classes = []

        for cls, amount in creation_group.items():
            count = amount["count"]

            if count == 1:
                classes.append(cls)
            else:
                classes.append(f"{cls} [x{count}]")

        cleaned.append(
            f"{timestamp} | {creation_header} | Created: {', '.join(classes)}"
        )

        creation_group.clear()
        creation_header = None

    for line in lines:
        line = re.sub(r" \(JEID:[^)]+\)", "", line)
        line = re.sub(r" \(VALUES:.*\)$", "", line)

        parts = line.split(" | ")

        if len(parts) != 3:
            flush_creation_group()
            cleaned.append(line)
            continue

        timestamp, header, message = parts

        if message.endswith(": Created"):
            cls = message[:-9]

            if creation_header is None:
                creation_header = header

            creation_group.setdefault(
                cls,
                {
                    "timestamp": timestamp,
                    "count": 0
                }
            )

            creation_group[cls]["count"] += 1
            continue

        flush_creation_group()

        if cleaned:
            previous = cleaned[-1].split(" | ", 2)

            if len(previous) == 3 and previous[1:] == [header, message]:
                if cleaned[-1].endswith("]"):
                    cleaned[-1] = re.sub(
                        r"\[x(\d+)]$",
                        lambda m: f"[x{int(m.group(1)) + 1}]",
                        cleaned[-1]
                    )
                else:
                    cleaned[-1] += " [x2]"
                continue

        cleaned.append(line)

    flush_creation_group()

    result = "\n".join(cleaned)

    with open(
        f"{_current_log.log_path}{_current_log.log_file_name}_cleaned.jar-log",
        "w"
    ) as file:
        file.write(
            "   date          time      | [TYPE]  title      | detail\n\n"
            "---START---\n"
        )
        file.write(result)
        file.write("\n----END----\n")

def close():
    if _current_log is None:
        return

    _current_log.close()
    if _current_log._enabled("debug", "LOG", "clean"):
        clean()
