from typing import Final

import datetime

from .obtained_time import ObtainedTime

class Asset:
    name: Final[str]
    value: Final[int]
    time: Final[ObtainedTime]

    def __init__(self, name: str, value: int, time: ObtainedTime):
        non_negative = value
        if (len(name) <= 0):
            raise ValueError('asset name must not be null or empty')
        if (value < 0):
            non_negative = 0
        self.name = name
        self.value = non_negative
        self.time = time

    def __str__(self) -> str:
        return f'{{{self.name}: {self.value}}}'

    def __repr__(self) -> str:
        return f'Asset(name={self.name}, value={self.value})'
