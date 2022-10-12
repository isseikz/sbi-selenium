from datetime import datetime
from time import strftime
from typing import Final


class ObtainedTime:
    __FORMAT = '%Y-%m-%d %H:%M:%S'
    time: Final[datetime]

    def __init__(self, time: datetime) -> None:
        self.time = time

    def __str__(self) -> str:
        return self.time.strftime(self.__FORMAT)
