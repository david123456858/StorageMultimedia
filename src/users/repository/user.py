from src.shared.interfaces.repository.repositoryCrud import repositoryCrud
from src.users.dtos.user import user

class repositoryUser(repositoryCrud[user]):
    def save(self, entity: user):
        return super().save(entity)
    
    def update(self, entity: user) -> user:
        return super().update(entity)
    
    def findAll(self) -> list[user]:
        return super().findAll()
    
    def findById(self, id: str) -> user:
        return super().findById(id)
    
    def delete(self, id: str) -> user:
        return super().delete(id)