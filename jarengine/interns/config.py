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

from os.path import exists
from os import mkdir
from typing import final as _final
from datetime import datetime as _datetime

from jarbin_toolkit_config import Config as _JTKInternConfig

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEInternConfig(_JTKInternConfig, _JEInternBaseClass):
    __recursive__ = False

    project_path = None
    config_path = None
    configs = {}

    def __init__(self, name, data = None):
        from constants import (
            JEVersion_JarEngine as _JEVersion_JarEngine,
            JEVersion_Config as _JEVersion_Config
        )

        if not JEInternConfig.project_path or  not JEInternConfig.config_path:
            raise _JTKExternError.State.ErrorStateNotInitialized("\nJarEngine.init(path) must be called first")
        if not exists(JEInternConfig.config_path):
            mkdir(JEInternConfig.config_path)

        if not data:
            data = {}

        super().__init__(JEInternConfig.config_path, {
            "INFO": {
                "name": name,                                       #Configuration file identifier.
                "creation": _datetime.now(),                        #Timestamp when this config was first created.
                "jarengine_version": str(_JEVersion_JarEngine),     #Version of JarEngine when the config was created.
                "config_version": str(_JEVersion_Config),           #Version of configuration when the config was created
            }
        } | data, file_name=f"je-{name}.ini")
        JEInternConfig.configs[name] = self

def get(name, section, setting, _type = str, default = None):
    if name not in JEInternConfig.configs:
        raise _JTKExternError.Special.ErrorSpecialConfig(f"\nNo config named {name} is opened")

    _GETTERS = {
        str: lambda c, s, o: c.get(s, o),
        bool: lambda c, s, o: c.get_bool(s, o),
        int: lambda c, s, o: c.get_int(s, o),
        float: lambda c, s, o: c.get_float(s, o),
    }

    config = JEInternConfig.configs[name]

    try:
        getter = _GETTERS.get(_type)

        if getter:
            return getter(config, section, setting)

        return config.get(section, setting, _type)

    except ValueError as e:
        if default is not None:
            return default
        raise _JTKExternError.Special.ErrorSpecialConfig("\nInvalid value type") from e

    except Exception as e:
        if default is not None:
            return default
        raise _JTKExternError.Special.ErrorSpecialConfig("\nSection or setting not found") from e

def set(name, section, setting, value):
    if not name in JEInternConfig.configs:
        raise _JTKExternError.Special.ErrorSpecialConfig(f"\nNo config named {name} is opened")

    try:
        JEInternConfig.configs[name].set(section, setting, value)

    except Exception:
        raise _JTKExternError.Special.ErrorSpecialConfig("\nSection or setting not found")

def init_all():
    from constants import (
        JEVersion_JarEngine as _JEVersion_JarEngine,
        JEVersion_Config as _JEVersion_Config,
        JEVersion_PyGame as _JEVersion_PyGame,
        JEVersion_Python as _JEVersion_Python
    )

    config = JEInternConfig(
        "engine",
        {
            "ENGINE": {
                "name": "JarEngine",                                #Engine display name. #Unused
                "version": "",                                      #Current JarEngine version. #Unused
                "safe_mode": False,                                 #Enable additional safety checks and restricted behavior.
                "auto_update": True,                                #Automatically updates internal engine states every frame #Unused
                "error_handling": False,                            #Enables internal error handling and recovery mechanisms
                "exception_mode": "strict",                         #Defines exception behavior mode (strict, warning, silent)
            },

            "CONFIG": {
                "version": "",                                      #Current Config version. #Unused
            },

            "THREAD": {
                "enabled": False,                                   #Enable or disable multithreaded engine execution. #Unused
                "max_threads": 4,                                   #Maximum number of worker threads available. #Unused
            },

            "SYSTEM": {
                "auto_register": True,                              #Automatically register compatible engine systems. #Unused
                "system_sorting": True,                             #Automatically sort systems by execution order. #Unused
                "entity_cache": True,                               #Cache entities matching system requirements. #Unused
                "parallel_execution": False,                        #Enables or disables parallel execution of engine systems #Unused
                "execution_order": "automatic",                     #Defines how systems execution order is determined #Unused
            },

            "MEMORY": {
                "garbage_collection": True,                         #Automatically perform memory cleanup operations. #Unused
                "resource_cache": True,                             #Keep loaded resources cached for faster reuse. #Unused
                "cache_limit": 1024,                                #Maximum number of cached resources allowed. #Unused
                "resource_unload": True,                            #Automatically unloads unused resources from memory #Unused
                "entity_cleanup": True,                             #Automatically removes unused or destroyed entities #Unused
            },

            "COMPATIBILITY": {
                "jarengine_version_check": True,                    #Checks if the installed JarEngine version is compatible
                "config_version_check": True,                       #Checks if each config version are compatible
                "pygame_version_check": True,                       #Checks if the installed PyGame version is compatible #Unused
                "python_version_check": True,                       #Checks if the current Python version is compatible #Unused
            },
        }
    )

    config.set(
        "ENGINE",
        "version",
        str(_JEVersion_JarEngine)
    )

    config.set(
        "CONFIG",
        "version",
        str(_JEVersion_Config)
    )

    JEInternConfig(
        "project",
        {
            "PROJECT": {
                "name": "Unnamed Project",                          #Defines the display name of the project #Unused
                "path": JEInternConfig.project_path,                #Defines the absolute path where the project is located #Unused
                "version": "0.1.0",                                 #Defines the current game version
                "jarengine_version": str(_JEVersion_JarEngine),     #Defines the required JarEngine version
                "config_version": str(_JEVersion_Config),           #Defines the required Config version
                "pygame_version": str(_JEVersion_PyGame),           #Defines the required PyGame version
                "python_version": str(_JEVersion_Python),           #Defines the required Python version
            },

            "AUTHOR": {
                "name": "",                                         #Defines the name of the project author #Unused
                "company": "",                                      #Defines the company or organization associated with the project #Unused
            },
        }
    )

    session = JEInternConfig(
        "session",
        {
            "FIRST_RUN": {
                "timestamp": _datetime.now(),                       #Timestamp of the first time the project was launched.
            },

            "LAST_RUN": {
                "timestamp": "",                                    #Timestamp when the project was last launched.
                "duration": "",                                     #Duration of the previous project execution session.
            },
        }
    )

    session.set(
        "LAST_RUN",
        "timestamp",
        _datetime.now()
    )

    JEInternConfig(
        "window",
        {
            "WINDOW": {
                "width": 1200,                                      #Width of the application window in pixels.
                "height": 700,                                      #Height of the application window in pixels.
                "fullscreen": False,                                #Enables or disables fullscreen display mode.
                "resizable": True,                                  #Allows the user to resize the application window.
                "borderless": False,                                #Removes the operating system window decorations.
            },

            "DISPLAY": {
                "display": 0,                                       #Display where the window will be created
                "vsync": False,                                     #Synchronizes rendering with the monitor refresh rate.
                "fps": 60,                                          #Maximum target frames per second.
                "depth": 32,                                        #Color depth of the display surface in bits.
            },

            "TITLE": {
                "text": "JarEngine Application",                    #Text displayed in the application window title bar. #Unused
            },

            "POSITION": {
                "center": True,                                     #Automatically centers the window on the screen.
                "x": 0,                                             #Horizontal position of the window when not centered.
                "y": 0,                                             #Vertical position of the window when not centered.
            },

            "ICON": {
                "enabled": False,                                   #Enables the use of a custom application icon.
                "path": "",                                         #Path to the image file used as the window icon.
            },
        }
    )

    JEInternConfig(
        "render",
        {
            "RENDER": {
                "mode": "buffered",                                 #Rendering mode: buffered or direct
                "renderer": "pygame",                               #Rendering backend used by the engine.
                "double_buffer": False,                             #Enables double buffering for smoother rendering (only if using opengl renderer).
                "clear_each_frame": True,                           #Clears the render surface before drawing each frame. #Unused
            },

            "BACKGROUND": {
                "color": "20,15,20,255",                            #Default background color applied when clearing the render surface (RGBA format). #Unused
            },

            "ALPHA": {
                "enabled": True,                                    #Enables transparency support in the rendering pipeline.
                "surface_format": "RGBA",                           #Pixel format used by rendering surfaces. #Unused
                "premultiplied": False,                             #Enables or disables premultiplied alpha blending. #Unused
            },

            "LAYER": {
                "enabled": True,                                    #Enables the layer-based rendering system. #Unused
                "automatic_sort": True,                             #Automatically sorts entities by their rendering layer. #Unused
                "min": 0,                                           #Minimum allowed rendering layer value. #Unused
                "max": 999999,                                      #Maximum allowed rendering layer value. #Unused
            },

            "TEXT": {
                "antialias": True,                                  #Enables font smoothing when rendering text. #Unused
            },

            "TEXTURE": {
                "smooth_scaling": True,                             #Enables filtered texture scaling to reduce pixelation. #Unused
            },

            "DEBUG": {
                "show_fps": False,                                  #Displays the current frames per second counter. #Unused
                "show_hitboxes": False,                             #Displays collision or object boundaries for debugging. #Unused
                "show_layers": False,                               #Displays entity rendering layers for debugging. #Unused
            },
        }
    )

    JEInternConfig(
        "assets",
        {
            "ASSETS": {
                "path": f"{JEInternConfig.project_path}/assets",    #Root directory containing all project assets.
            },

            "DIRECTORY": {
                "font": "fonts",                                    #Directory containing font files.
                "texture": "textures",                              #Directory containing texture and image files.
                "animation": "animations",                          #Directory containing animation assets. #Unused
                "sound": "sounds",                                  #Directory containing sound effect files.
                "music": "musics",                                  #Directory containing background music files.
                "shader": "shaders",                                #Directory containing shader source files. #Unused
                "scene": "scenes",                                  #Directory containing scene definitions. #Unused
                "prefab": "prefabs",                                #Directory containing reusable prefab definitions. #Unused
            },

            "LOADER": {
                "recursive": True,                                  #Search asset directories recursively. #Unused
                "lazy_loading": True,                               #Load assets only when first requested. #Unused
                "cache": True,                                      #Keep loaded assets cached in memory. #Unused
            },

            "TEXTURE": {
                "extensions": "png,jpg,jpeg,bmp",                      #Comma-separated list of supported texture formats. #Unused
            },

            "AUDIO": {
                "extensions": "wav,ogg,mp3",                           #Comma-separated list of supported audio formats. #Unused
            },
        }
    )

    JEInternConfig(
        "input",
        {
            "INPUT": {
                "enabled": True,                                    #Enables or disables the global input management system #Unused
            },

            "MOUSE": {
                "enabled": True,                                    #Enables or disables mouse input handling #Unused
                "visible": True,                                    #Controls whether the mouse cursor is visible inside the window #Unused
                "relative": False,                                  #Enables or disables relative mouse movement mode #Unused
            },

            "KEYBOARD": {
                "enabled": True,                                    #Enables or disables keyboard input handling #Unused
                "repeat": False,                                    #Enables or disables repeated key events while holding a key #Unused
            },

            "GAMEPAD": {
                "enabled": False,                                   #Enables or disables gamepad input handling #Unused
                "max_devices": 4,                                   #Defines the maximum number of supported gamepad devices #Unused
            },

            "BINDING": {
                "move_up": "z",                                     #Defines the key used for moving upward #Unused
                "move_down": "s",                                   #Defines the key used for moving downward #Unused
                "move_left": "q",                                   #Defines the key used for moving left #Unused
                "move_right": "d",                                  #Defines the key used for moving right #Unused
            },
        }
    )

    JEInternConfig(
        "audio",
        {
            "AUDIO": {
                "enabled": True,                                    #Enable or disable the entire audio system. #Unused
                "master_volume": 1.0,                               #Global volume multiplier applied to all audio. #Unused
            },

            "MUSIC": {
                "enabled": True,                                    #Enable or disable background music playback. #Unused
                "volume": 0.8,                                      #Default music volume multiplier. #Unused
            },

            "SOUND": {
                "enabled": True,                                    #Enable or disable sound effect playback. #Unused
                "volume": 1.0,                                      #Default sound effect volume multiplier. #Unused
            },

            "DEVICE": {
                "channels": 32,                                     #Number of simultaneous audio channels available. #Unused
                "frequency": 44100,                                 #Audio output sample rate in Hz. #Unused
            },
        }
    )

    JEInternConfig(
        "debug",
        {
            "DEBUG": {
                "enabled": False,                                   #Enable or disable all debug features. #Unused
            },

            "LOG": {
                "enabled": True,                                    #Enable or disable engine logging. #Unused
                "level": "INFO",                                    #Minimum log severity to record. #Unused
                "file": "jarengine.log",                            #Log file name. #Unused
            },

            "ASSERT": {
                "enabled": True,                                    #Enable or disable runtime assertions. #Unused
            },

            "PROFILE": {
                "enabled": False,                                   #Enable or disable performance profiling. #Unused
            },

            "MEMORY": {
                "track_entities": False,                            #Track entity allocation and lifetime. #Unused
                "track_resources": False,                           #Track resource allocation and lifetime. #Unused
            },

            "DISPLAY": {
                "show_fps": False,                                  #Display the current FPS on screen. #Unused
                "show_entity_count": False,                         #Display the current number of loaded entities. #Unused
                "show_components": False,                           #Display the current number of loaded entities. #Unused
            },
        }
    )

    JEInternConfig(
        "physics",
        {
            "PHYSICS": {
                "enabled": False,                                   #Enables or disables the physics simulation system. #Unused
            },

            "WORLD": {
                "gravity_x": 0,                                     #Horizontal gravity acceleration applied to physics objects. #Unused
                "gravity_y": 9.81,                                  #Vertical gravity acceleration applied to physics objects. #Unused
            },

            "TIME": {
                "fixed_update": True,                               #Uses a fixed timestep update loop for deterministic physics simulation. #Unused
                "timestep": 1 / 60,                                 #Fixed physics update interval in seconds. #Unused
            },

            "COLLISION": {
                "enabled": True,                                    #Enables collision detection and response. #Unused
                "layers": True,                                     #Enables collision layers filtering between object groups. #Unused
            },
        }
    )

    JEInternConfig(
        "event",
        {
            "EVENT": {
                "enabled": True,                                    #Enables or disables the event management system #Unused
                "event_broadcast": False,                           #Allows events to be automatically broadcasted to registered listeners #Unused
            },

            "QUEUE": {
                "enabled": True,                                    #Enables the internal event queue system #Unused
                "max_size": 1000,                                   #Maximum number of events stored in the queue before overflow #Unused
            },

            "DEBUG": {
                "log_events": False,                                #Logs emitted and processed events for debugging purposes #Unused
            },
        }
    )

class _Checks:

    @staticmethod
    def compatibility():
        from jarengine.interns.helpers import (
            version as _version,
            enabled as _enabled,
            error as _error,
            warning as _warning,
        )
        from constants import (
            JEVersion_JarEngine as _JEVersion_JarEngine,
            JEVersion_Config as _JEVersion_Config,
            JEVersion_PyGame as _JEVersion_PyGame,
            JEVersion_Python as _JEVersion_Python
        )
        from jarengine.systems.version import JECompatibility as _JECompatibility

        def _check(current, required, name):
            status = current.compatibility(required)
            err = _JTKExternError.Special.ErrorSpecialConfig(
                f"\nCompatibility failure on {name} "
                f"(current: {current}, required: {required})"
            )

            if status == _JECompatibility.ERROR:
                _error(err)

            elif status == _JECompatibility.WARNING:
                _warning(err)

        required_engine = _version("project", "PROJECT", "jarengine_version")
        required_config = _version("project", "PROJECT", "config_version")
        required_pygame = _version("project", "PROJECT", "pygame_version")
        required_python = _version("project", "PROJECT", "python_version")

        if _enabled("engine", "COMPATIBILITY", "jarengine_version_check"):
            _check(_JEVersion_JarEngine, required_engine, "JarEngine version")

        if _enabled("engine", "COMPATIBILITY", "config_version_check"):
            _check(_JEVersion_Config, required_config, "Config version")

        if _enabled("engine", "COMPATIBILITY", "pygame_version_check"):
            _check(_JEVersion_PyGame, required_pygame, "Pygame version")

        if _enabled("engine", "COMPATIBILITY", "python_version_check"):
            _check(_JEVersion_Python, required_python, "Python version")

        for config in JEInternConfig.configs:

            if _enabled("engine", "COMPATIBILITY", "jarengine_version_check"):
                _check(
                    _version(config, "INFO", "jarengine_version"),
                    required_engine,
                    f"{get(config, 'INFO', 'name')} JarEngine version"
                )

            if _enabled("engine", "COMPATIBILITY", "config_version_check"):
                _check(
                    _version(config, "INFO", "config_version"),
                    required_config,
                    f"{get(config, 'INFO', 'name')} config version"
                )
