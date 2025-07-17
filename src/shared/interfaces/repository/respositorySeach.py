from abc import ABC,abstractmethod
from typing import Generic,TypeVar


T = TypeVar('T')

class ISearchRepository(ABC,Generic[T]):
    
    @abstractmethod
    def findAll(self) -> list[T]:
        pass
    
    @abstractmethod
    def findById(self,id : str) -> T:
        pass
    