from __future__ import annotations

# Public API exports
from sources.systems.color import JEColor
from sources.systems.bool import JEBool
from sources.systems.container import JEContainer
from sources.systems.immutable import JEImmutable

# Submodules
import sources.systems.vector as Vector

__all__: list[str] = [
    'Vector',
    'JEColor',
    'JEBool',
    'JEContainer',
    'JEImmutable'
]
