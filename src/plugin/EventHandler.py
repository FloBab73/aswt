"""
EventHandler is a class to manage multiple events.
usage:
eh = EventHandler()       #Create EventHandler
eh.add("event", func)     #Add function to "event" map
eh("event")               #Fire event "event" -> call all function in "event" map
eh.remove("event", funct) #remove function from "event" map
"""

from enum import Enum


class EventHandler:
    class Events(Enum):
        PICKUP_HEALTH = 0
        PICKUP_KEY = 1
        MONEY = 2
        REMOVE_BLOCK = 3
        DOOR = 4
        MOVE_PLAYER = 5
        MOVE_ENEMIES = 6
        DRAW = 7
        RESET = 8
        PAUSE = 9
        KEY_PRESSED = 10
        DAMAGE = 11
        QUIT = 255

    def __init__(self):
        self._eventDict = {}

    def add(self, event, func):
        if event not in self._eventDict:
            self._eventDict[event] = {func}  # new map
        else:
            self._eventDict[event].add(func)

    def remove(self, event, func):
        if event in self._eventDict:
            self._eventDict[event].remove(func)
        else:
            print("EventHandler.remove(): event '", event, "' not in _events")

    def __call__(self, event, *args, **kwargs):
        if event in self._eventDict:
            for func in self._eventDict[event]:
                func(*args, **kwargs)
        else:
            print("EventHandler(): event '", event, "' not in _events")
