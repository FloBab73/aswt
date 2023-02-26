"""
EventHandler is a class to manage multiple events.
usage:
eh = EventHandler()       #Create EventHandler
eh.add("event", func)     #Add function to "event" map
eh("event")               #Fire event "event" -> call all function in "event" map
eh.remove("event", funct) #remove function from "event" map
"""


class EventHandler:
    def __init__(self):
        self._events = {}

    def add(self, event, func):
        if event not in self._events:
            self._events[event] = {func}    #new map
        else:
            self._events[event].append(func)

    def remove(self, event, func):
        if event in self._events:
            self._events[event].remove(func)
        else:
            print("EventHandler.remove(): event '", event, "' not in _events")

    def __call__(self, event, *args, **kwargs):
        if event in self._events:
            for func in self._events[event]:
                func(*args, **kwargs)
        else:
            print("EventHandler(): event '", event, "' not in _events")
