from abc import ABC, abstractmethod

from src.domain.asset import Asset

class IDataStore(ABC):
    @abstractmethod
    def save(self, asset: Asset) -> None:
        raise NotImplementedError()
