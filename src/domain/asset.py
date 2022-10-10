from typing import Final

class Asset:
    name: Final[str]
    value: Final[int]
    def __init__(self, name: str, value: int):
        if (len(name) <= 0):
            raise ValueError('asset name must not be null or empty')
        if (value < 0):
            raise ValueError('asset value must not be negative')
        self.name = name
        self.value = value
    def __str__(self) -> str:
        return f'{{{self.name}: {self.value}}}'
    def __repr__(self) -> str:
        return f'Asset(name={self.name}, value={self.value})'
