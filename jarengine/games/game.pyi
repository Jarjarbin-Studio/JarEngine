from __future__ import annotations

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.games.window import JEWindow
from jarengine.games.input import JEInput
from jarengine.events.manager import JEEventHandler
from jarengine.events.keyboard import JEKeyCode
from jarengine.events.mouse import JEMouseCode
from jarengine.entities.entity import JEEntity
from jarengine.systems.container import JEContainer
from jarengine.interns.high_classes import JEInternSystems
from jarengine.interns.final_classes import JEInternResources
from jarengine.systems.bool import JEBool
from jarengine.systems.clock import JEClock

class JEGame(JEInternBaseClass):
    def __init__(self, *, use_clock: JEBool = JEBool(0), use_input: JEBool = JEBool(0)):
        """
            JEGame

            Parameters:
                use_clock (JEBool) = JEBool(0): Activate clock handler
                use_input (JEBool) = JEBool(0): Activate input handler
        """
        ...
    def set_window(self, window: JEWindow):
        """
            Set game window

            Parameters:
                window (JEWindow): Window
        """
        ...
    @property
    def wdw(self) -> JEWindow:
        """
            Get window
            
            Returns:
                JEWindow: Window
        """
        ...
    @property
    def input(self) -> JEInput:
        """
            Get input handler (needs use_input = JETrue)

            Returns:
                JEInput: Input handler
        """
        ...
    def is_key_down(self, key: JEKeyCode) -> bool:
        """
            Check if a key is down (needs use_input = JETrue)
            
            Parameters:
                key (JEKeyCode): Key
            
            Returns:
                bool; True if key is down, False otherwise
        """
        ...
    def is_mouse_down(self, button: JEMouseCode) -> bool:
        """
            Check if a mouse button is down (needs use_input = JETrue)

            Parameters:
                button (JEMouseCode): Mouse

            Returns:
                bool; True if mouse button is down, False otherwise
        """
        ...
    @property
    def clock(self) -> JEClock:
        """
            Get game clock (needs use_clock = JETrue)

            Returns:
                JEClock: Game clock
        """
        ...
    @property
    def dt(self) -> float:
        """
            Get game clock (needs use_clock = JETrue)

            Returns:
                JEClock: Game clock
        """
        ...
    @property
    def event(self) -> JEEventHandler:
        """
            Get event handler

            Returns:
                JEEventHandler: Event handler
        """
        ...
    @property
    def is_open(self) -> JEBool:
        """
            Check if game is open

            Returns:
                JEBool: True if game is open, False otherwise
        """
        ...
    def close(self):
        """
            Close game
        """
        ...
    @property
    def ressource(self) -> JEInternResources:
        """
            Get game resources storage

            Returns:
                JEInternResources: Game resources
        """
        ...
    def refresh(self):
        """
            Refresh game info, systems' cache, and other sub systems (HIGH COST ON CPU)
        """
        ...
    def add_entity(self, entity: JEEntity):
        """
            Add an entity to the game (do not use if you want manual handling of the entity)

            Parameters:
                entity (JEEntity): Entity to add
        """
        ...
    @property
    def entities(self) -> JEContainer[JEEntity]:
        """
            Get entity container

            Returns:
                JEContainer[JEEntity]: Entity container
        """
        ...
    def add_system(self, system: JEInternSystems):
        """
            Add a system to the game

            Parameters:
                system (JEInternSystems): Entity to add
        """
        ...
    @property
    def systems(self) -> JEContainer[JEInternSystems]:
        """
            Get system container

            Returns:
                JEContainer[JEInternSystems]: System container
        """
        ...
    def update(self):
        """
            Update entities through added systems
        """
        ...
    def display(self):
        """
            Display window
        """
        ...
