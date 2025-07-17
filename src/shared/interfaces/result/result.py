from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')
# interfaces uniformes para el resultado 

class ISuccessProcess(ABC,Generic[T]):
    @property
    @abstractmethod
    def value (self) -> T:
        pass
    
    @property
    @abstractmethod
    def code (self) -> int:
        pass
    
    @abstractmethod
    def success(self) -> bool:
        pass

class IFailureProcess(ABC,Generic[T]):
    @property
    @abstractmethod
    def error (self) -> T:
        pass
    
    @property
    @abstractmethod
    def code (self) -> int:
        pass
    
    @property
    @abstractmethod
    def success(self) -> bool:
        pass