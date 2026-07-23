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

from jarengine.systems.bool import JEBool as _JEBool
from jarengine.widgets.widget import JEWidget as _JEWidget
from jarengine.entity.components_graphics import (
    JESurfaceComponent as _JESurfaceComponent,
    JETextComponent as _JETextComponent,
    JEFontComponent as _JEFontComponent,
    JEColorComponent as _JEColorComponent,
    JETextureComponent as _JETextureComponent,
    JEFlipComponent as _JEFlipComponent
)
from jarengine.systems.vector import JEVector2D as _JEVector2D
from jarengine.systems.color import JEColor as _JEColor
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns import (
    PGExtern as _PGExtern,
    JTKExternError as _JTKExternError
)
import jarengine.interns.log as _log

@_documentation
class JESprite(_JEWidget):

    def __init__(self, texture, *, flip = (_JEBool(0), _JEBool(0)), name = "JESprite", position = _JEVector2D(0, 0), size = _JEVector2D(0, 0), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JETextureComponent(self, texture)
        _JEFlipComponent(self, flip)

        _log.log("DEBUG", "OBJECT", f"JESprite: Created", self.jeid, texture, flip)

@_documentation
class JEText(_JEWidget):

    def __init__(self, text, font, *, color = None, flip = (_JEBool(0), _JEBool(0)), name = "JEText", position = _JEVector2D(0, 0), size = _JEVector2D(0, 0), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JETextComponent(self, text)
        _JEFontComponent(self, font)
        _JEFlipComponent(self, flip)
        if color:
            _JEColorComponent(self, color)

        if len(text) > 50:
            text = f"{text[:47]}..."
        _log.log("DEBUG", "OBJECT", f"JEText: Created", self.jeid, text, font, color, flip)

@_documentation
class JERectangle(_JEWidget):

    def __init__(self, size, *, color = _JEColor(255, 255, 255, 255), outline_color = None, outline_size = None, name = "JERectangle", position = _JEVector2D(0, 0), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        surface = _PGExtern.Surface(
            list(size),
            _PGExtern.SRCALPHA
        )

        surface.fill(color.rgba if isinstance(color, _JEColor) else color)

        if outline_color and outline_size:
            _PGExtern.draw.rect(
                surface,
                outline_color,
                surface.get_rect(),
                outline_size
            )

        _JESurfaceComponent(self, surface)

        _log.log("DEBUG", "OBJECT", f"JERectangle: Created", self.jeid, size, color, outline_color, outline_size)

@_documentation
class JECircle(_JEWidget):

    def __init__(self, radius, *, color = _JEColor(255, 255, 255, 255), outline_color = None, outline_size = None, name = "JECircle", position = _JEVector2D(0, 0), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        diameter = radius * 2

        super().__init__(name=name, position=position, size=_JEVector2D(diameter, diameter), rotation=rotation, layer=layer, visibility=visibility)

        surface = _PGExtern.Surface((diameter, diameter), _PGExtern.SRCALPHA)

        _PGExtern.draw.circle(surface, color, (radius, radius), radius)

        if outline_color and outline_size:
            _PGExtern.draw.circle(surface, outline_color, (radius, radius), radius, outline_size)

        _JESurfaceComponent(self, surface)

        _log.log("DEBUG", "OBJECT", f"JECircle: Created", self.jeid, radius, color, outline_color, outline_size)

@_documentation
class JELine(_JEWidget):

    def __init__(self, start, end, *, color = _JEColor(255, 255, 255, 255), width = 1, name = "JELine", rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        start = list(start)
        end = list(end)

        min_x = min(start[0], end[0])
        min_y = min(start[1], end[1])

        local_start = (start[0] - min_x, start[1] - min_y)
        local_end = (end[0] - min_x, end[1] - min_y)

        size = _JEVector2D(abs(end[0] - start[0]) + width, abs(end[1] - start[1]) + width)

        super().__init__(name=name, position=_JEVector2D(0, 0) + _JEVector2D(min_x, min_y), size=size, rotation=rotation, layer=layer, visibility=visibility)

        surface = _PGExtern.Surface((int(size.x), int(size.y)), _PGExtern.SRCALPHA)

        _PGExtern.draw.line(surface, color, local_start, local_end, width)

        _JESurfaceComponent(self, surface)

        _log.log("DEBUG", "OBJECT", f"JELine: Created", self.jeid, start, end, color, width)

@_documentation
class JEPolygon(_JEWidget):

    def __init__(self, points, *, color = _JEColor(255, 255, 255, 255), outline_color = None, outline_size = None, name = "JEPolygon", rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        raw_points = [tuple(point) for point in points]

        if len(raw_points) < 3:
            raise _JTKExternError.Error.ErrorValue("\nJEPolygon requires at least 3 points.")

        min_x = min(point[0] for point in raw_points)
        min_y = min(point[1] for point in raw_points)
        max_x = max(point[0] for point in raw_points)
        max_y = max(point[1] for point in raw_points)

        local_points = [(point[0] - min_x, point[1] - min_y) for point in raw_points]
        size = _JEVector2D(max_x - min_x, max_y - min_y)

        super().__init__(name=name, position=_JEVector2D(0, 0) + _JEVector2D(min_x, min_y), size=size, rotation=rotation, layer=layer, visibility=visibility)

        surface = _PGExtern.Surface((int(size.x), int(size.y)), _PGExtern.SRCALPHA)

        _PGExtern.draw.polygon(surface, color, local_points)

        if outline_color and outline_size:
            _PGExtern.draw.polygon(surface, outline_color, local_points, outline_size)

        _JESurfaceComponent(self, surface)

        _log.log("DEBUG", "OBJECT", f"JEPolygon: Created", self.jeid, points, color, outline_color, outline_size)
