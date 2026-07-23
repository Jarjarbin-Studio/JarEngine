# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
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

from typing import Optional, Any, TypeVar

from jarengine.systems.version import JEVersion

def error(err: Exception | str, do_traceback: bool = True):
    """
        Show an error

        Parameters:
            err (Exception | str): error
            do_traceback (bool) = True: show traceback if True
    """
    ...


def warning(message: Exception | str, do_traceback: bool = False):
    """
        Show a warning

        Parameters:
            message (Exception | str): message
            do_traceback (bool) = False: show traceback if True
    """
    ...
def assertion(condition: bool | Any, message: str, strict: bool = False, do_traceback: bool = True):
    """
        Run an assertion
        
        Parameters:
            condition (bool): condition
            message (str): message
            strict (bool): force the exception raise if True
            do_traceback (bool) = True: show traceback if True
    """
    ...
def assertion_type(value: Any, _type: type | TypeVar | tuple[type | TypeVar, ...], message: str, strict: bool = False, do_traceback: bool = True):
    """
        Run a type assertion

        Parameters:
            value (Any): condition
            _type (type | tuple[type, ...]): type
            message (str): message
            strict (bool): force the exception raise if True
            do_traceback (bool) = True: show traceback if True
    """
    ...
def assertion_class(value: Any, _class: type | TypeVar | tuple[type | TypeVar, ...], message: str, strict: bool = False, do_traceback: bool = True):
    """
        Run a subclass assertion

        Parameters:
            value (Any): condition
            _class (type | tuple[type, ...]): class
            message (str): message
            strict (bool): force the exception raise if True
            do_traceback (bool) = True: show traceback if True
    """
    ...
def enabled(config: str, section: str, setting: str = "enabled") -> bool:
    """
        Check if a feature is enabled

        Parameters:
            config (str): config file name
            section (str): section name
            setting (str) = "enabled": setting name

        Returns:
            bool: True or False
    """
    ...
def project_path(*paths: str) -> str:
    """
        Get a project path

        Parameters:
            *paths (list[str]): paths

        Returns:
            str: path
    """
    ...
def asset_path(*paths: str) -> str:
    """
        Get a asset path

        Parameters:
            *paths (list[str]): paths

        Returns:
            str: path
    """
    ...
def require_exists(path: str):
    """
        Requires a path to exist (raise an error if invalid)

        Parameters:
            path (str): path
    """
    ...
def validate_value(value: Any, allowed: list[Any] | tuple[Any], name: str):
    """
        Validate a value (raise an error if invalid)
        
        Parameters:
            value (Any): value to validate
            allowed (list[Any] | tuple[Any]): allowed values
            name (str): name of the value
    """
    ...
def clamp(value: float | int, minimum: float | int, maximum: float | int) -> float | int :
    """
        Clamp a value

        Parameters:
            value (float | int): value to clamp
            minimum (float | int): minimum value
            maximum (float | int): maximum value

        Returns:
            float | int: clamped value
    """
    ...
def safe_mode() -> bool:
    """
        Get safe mode

        Returns:
            bool: True or False
    """
    ...
def debug_enabled(feature: Optional[str] = None) -> bool:
    """
        Check if debug features are enabled
        
        Parameters:
            feature (Optional[str]): feature name (global debug if None)
        
        Returns:
            bool: True or False
    """
    ...
def version(config: str, section: str, key: str) -> JEVersion:
    """
        Get a version from a config
        
        Parameters:
            config (str): config file name
            section (str): section name
            key (str): key
        
        Returns:
            JEVersion: Version
    """
    ...
def safe_cast(value: Any, _type: type) -> Any:
    """
        Cast a value

        Parameters:
            value (str): Value to cast
            _type (str): Type to cast in

        Returns:
            Any: Cast value
    """
    ...
