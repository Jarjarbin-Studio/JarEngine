from __future__ import annotations

# Public API exports
from sources.games.window import JEWindow
from sources.games.game import JEGame
from sources.games.input import JEInput

# Submodules
import sources.games.systems as Systems

__all__: list[str] = [
    'JEGame',
    'JEWindow',
    'JEInput',
    'Systems'
]
