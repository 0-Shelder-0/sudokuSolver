from enum import Enum


class Status(Enum):
    UNKNOWN = 0
    CREATED = 1
    WAITING = 2
    IN_PROGRESS = 3
    SOLVED = 4
    ERROR = 5

    def __int__(self):
        return self.value
