from dataclasses import dataclass

from typing import get_args, get_origin, get_type_hints, Generic, Protocol, TypeVar


class Message:
    def __init__(self, message, priority):
        self.message = message
        self.priority = priority

    def __str__(self):
        return self.message + " has priority " + str(self.priority)

    def __cmp__(self, other):
        return self.priority < other.priority
