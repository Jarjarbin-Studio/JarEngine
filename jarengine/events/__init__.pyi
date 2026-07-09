from __future__ import annotations

# Public API exports

# Submodules
from . import manager as EventManager
from . import event as Event
from . import keyboard as EventKeyboard
from . import mouse as EventMouse

__all__: list[str] = [
    "EventManager",
    "Event",
    "EventKeyboard",
    "EventMouse"
]
