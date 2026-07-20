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
from jarengine import __version__

@_documentation
@_final
class JEInternConfig(_JTKInternConfig, _JEInternBaseClass):
    __recursive__ = False

    project_path = None
    config_path = None
    configs = {}

    def __init__(self, name, data = None):
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
                "version": __version__,                             #Version of JarEngine when the config was created.
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
    JEInternConfig(
        "engine",
        {
            "ENGINE": {
                "name": "JarEngine",                                #Engine display name.
                "version": __version__,                             #Current JarEngine version.
                "auto_init": True,                                  #Automatically initialize required engine systems.
                "safe_mode": False,                                 #Enable additional safety checks and restricted behavior.
                "auto_update": True,                                #Automatically updates internal engine states every frame
                "error_handling": True,                             #Enables internal error handling and recovery mechanisms
                "exception_mode": "strict",                         #Defines exception behavior mode (strict, warning, silent)
            },

            "THREAD": {
                "enabled": False,                                   #Enable or disable multithreaded engine execution.
                "max_threads": 4,                                   #Maximum number of worker threads available.
            },

            "SYSTEM": {
                "auto_register": True,                              #Automatically register compatible engine systems.
                "system_sorting": True,                             #Automatically sort systems by execution order.
                "entity_cache": True,                               #Cache entities matching system requirements.
                "parallel_execution": False,                        #Enables or disables parallel execution of engine systems
                "execution_order": "automatic",                     #Defines how systems execution order is determined
            },

            "MEMORY": {
                "garbage_collection": True,                         #Automatically perform memory cleanup operations.
                "resource_cache": True,                             #Keep loaded resources cached for faster reuse.
                "cache_limit": 1024,                                #Maximum number of cached resources allowed.
                "resource_unload": True,                            #Automatically unloads unused resources from memory
                "entity_cleanup": True,                             #Automatically removes unused or destroyed entities
            },

            "COMPATIBILITY": {
                "jarengine_version_check": True,                    #Checks if the installed JarEngine version is compatible
                "pygame_version_check": True,                       #Checks if the installed PyGame version is compatible
                "python_version_check": True,                       #Checks if the current Python version is compatible
            },
        }
    )

    JEInternConfig(
        "project",
        {
            "PROJECT": {
                "name": "Unnamed Project",                          #Defines the display name of the project
                "path": JEInternConfig.project_path,                #Defines the absolute path where the project is located
                "version": "0.1.0",                                 #Defines the absolute path where the project is located
                "engine_version": __version__                       #Defines the JarEngine version required by the project
            },

            "AUTHOR": {
                "name": "",                                         #Defines the name of the project author
                "company": "",                                      #Defines the company or organization associated with the project
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
                "vsync": False,                                     #Synchronizes rendering with the monitor refresh rate.
                "fps": 60,                                          #Maximum target frames per second.
                "depth": 32,                                        #Color depth of the display surface in bits.
            },

            "TITLE": {
                "text": "JarEngine Application",                    #Text displayed in the application window title bar.
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
                "renderer": "pygame",                               #Rendering backend used by the engine.
                "clear_each_frame": True,                           #Clears the render surface before drawing each frame.
            },

            "BACKGROUND": {
                "color": "20,15,20,255",                            #Default background color applied when clearing the render surface (RGBA format).
            },

            "ALPHA": {
                "enabled": True,                                    #Enables transparency support in the rendering pipeline.
                "surface_format": "RGBA",                           #Pixel format used by rendering surfaces.
                "premultiplied": False,                             #Enables or disables premultiplied alpha blending.
            },

            "LAYER": {
                "enabled": True,                                    #Enables the layer-based rendering system.
                "automatic_sort": True,                             #Automatically sorts entities by their rendering layer.
                "min": 0,                                           #Minimum allowed rendering layer value.
                "max": 999999,                                      #Maximum allowed rendering layer value.
            },

            "TEXT": {
                "antialias": True,                                  #Enables font smoothing when rendering text.
            },

            "TEXTURE": {
                "smooth_scaling": True,                             #Enables filtered texture scaling to reduce pixelation.
            },

            "DEBUG": {
                "show_fps": False,                                  #Displays the current frames per second counter.
                "show_hitboxes": False,                             #Displays collision or object boundaries for debugging.
                "show_layers": False,                               #Displays entity rendering layers for debugging.
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
                "animation": "animations",                          #Directory containing animation assets.
                "sound": "sounds",                                  #Directory containing sound effect files.
                "music": "musics",                                  #Directory containing background music files.
                "shader": "shaders",                                #Directory containing shader source files.
                "scene": "scenes",                                  #Directory containing scene definitions.
                "prefab": "prefabs",                                #Directory containing reusable prefab definitions.
            },

            "LOADER": {
                "recursive": True,                                  #Search asset directories recursively.
                "lazy_loading": True,                               #Load assets only when first requested.
                "cache": True,                                      #Keep loaded assets cached in memory.
            },

            "TEXTURE": {
                "extensions": "png,jpg,jpeg,bmp",                      #Comma-separated list of supported texture formats.
            },

            "AUDIO": {
                "extensions": "wav,ogg,mp3",                           #Comma-separated list of supported audio formats.
            },
        }
    )

    JEInternConfig(
        "input",
        {
            "INPUT": {
                "enabled": True,                                    #Enables or disables the global input management system
            },

            "MOUSE": {
                "enabled": True,                                    #Enables or disables mouse input handling
                "visible": True,                                    #Controls whether the mouse cursor is visible inside the window
                "relative": False,                                  #Enables or disables relative mouse movement mode
            },

            "KEYBOARD": {
                "enabled": True,                                    #Enables or disables keyboard input handling
                "repeat": False,                                    #Enables or disables repeated key events while holding a key
            },

            "GAMEPAD": {
                "enabled": False,                                   #Enables or disables gamepad input handling
                "max_devices": 4,                                   #Defines the maximum number of supported gamepad devices
            },

            "BINDING": {
                "move_up": "z",                                     #Defines the key used for moving upward
                "move_down": "s",                                   #Defines the key used for moving downward
                "move_left": "q",                                   #Defines the key used for moving left
                "move_right": "d",                                  #Defines the key used for moving right
            },
        }
    )

    JEInternConfig(
        "audio",
        {
            "AUDIO": {
                "enabled": True,                                    #Enable or disable the entire audio system.
                "master_volume": 1.0,                               #Global volume multiplier applied to all audio.
            },

            "MUSIC": {
                "enabled": True,                                    #Enable or disable background music playback.
                "volume": 0.8,                                      #Default music volume multiplier.
            },

            "SOUND": {
                "enabled": True,                                    #Enable or disable sound effect playback.
                "volume": 1.0,                                      #Default sound effect volume multiplier.
            },

            "DEVICE": {
                "channels": 32,                                     #Number of simultaneous audio channels available.
                "frequency": 44100,                                 #Audio output sample rate in Hz.
            },
        }
    )

    JEInternConfig(
        "debug",
        {
            "DEBUG": {
                "enabled": False,                                   #Enable or disable all debug features.
            },

            "LOG": {
                "enabled": True,                                    #Enable or disable engine logging.
                "level": "INFO",                                    #Minimum log severity to record.
                "file": "jarengine.log",                            #Log file name.
            },

            "ASSERT": {
                "enabled": True,                                    #Enable or disable runtime assertions.
            },

            "PROFILE": {
                "enabled": False,                                   #Enable or disable performance profiling.
            },

            "MEMORY": {
                "track_entities": False,                            #Track entity allocation and lifetime.
                "track_resources": False,                           #Track resource allocation and lifetime.
            },

            "DISPLAY": {
                "show_fps": False,                                  #Display the current FPS on screen.
                "show_entity_count": False,                         #Display the current number of loaded entities.
                "show_components": False,                           #Display the current number of loaded entities.
            },
        }
    )

    JEInternConfig(
        "physics",
        {
            "PHYSICS": {
                "enabled": False,                                   #Enables or disables the physics simulation system.
            },

            "WORLD": {
                "gravity_x": 0,                                     #Horizontal gravity acceleration applied to physics objects.
                "gravity_y": 9.81,                                  #Vertical gravity acceleration applied to physics objects.
            },

            "TIME": {
                "fixed_update": True,                               #Uses a fixed timestep update loop for deterministic physics simulation.
                "timestep": 1 / 60,                                 #Fixed physics update interval in seconds.
            },

            "COLLISION": {
                "enabled": True,                                    #Enables collision detection and response.
                "layers": True,                                     #Enables collision layers filtering between object groups.
            },
        }
    )

    JEInternConfig(
        "event",
        {
            "EVENT": {
                "enabled": True,                                    #Enables or disables the event management system
                "event_broadcast": False,                           #Allows events to be automatically broadcasted to registered listeners
            },

            "QUEUE": {
                "enabled": True,                                    #Enables the internal event queue system
                "max_size": 1000,                                   #Maximum number of events stored in the queue before overflow
            },

            "DEBUG": {
                "log_events": False,                                #Logs emitted and processed events for debugging purposes
            },
        }
    )
