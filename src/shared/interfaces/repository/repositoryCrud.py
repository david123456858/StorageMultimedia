from abc import abstractmethod
from typing import TypeVar

from src.shared.interfaces.repository.respositorySeach import ISearchRepository

T = TypeVar('T')
# clases abstractas y metodos abtractos 
# decoradores


class repositoryCrud(ISearchRepository[T]):
    
    @abstractmethod
    def save(self,entity:T):
        pass
    
    @abstractmethod
    def update(self,entity:T)-> T:
        pass
    
    @abstractmethod
    def delete(self, id:str)-> T:
        pass
