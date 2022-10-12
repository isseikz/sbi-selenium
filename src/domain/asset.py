from typing import Final

import datetime

from .obtained_time import ObtainedTime

class Asset:
    name: Final[str]
    value: Final[int]
    time: Final[ObtainedTime]

    def __init__(self, name: str, value: int, time: ObtainedTime):
        if (len(name) <= 0):
            raise ValueError('asset name must not be null or empty')
        if (value < 0):
            raise ValueError('asset value must not be negative')
        self.name = name
        self.value = value
        self.time = time

    def __str__(self) -> str:
        return f'{{{self.name}: {self.value}}}'

    def __repr__(self) -> str:
        return f'Asset(name={self.name}, value={self.value})'
