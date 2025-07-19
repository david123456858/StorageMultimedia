from src.shared.interfaces.repository.repositoryCrud import repositoryCrud
from src.users.entity.user import User

class repositoryUser(repositoryCrud[User]):
    """_summary_

    Args:
        repositoryCrud (User): this is class that did CRUD with database
    """
    def save(self, entity: User):
        return super().save(entity)
    
    def update(self, entity: User) -> User:
        return super().update(entity)
    
    def findAll(self) -> list[User]:
        return super().findAll()
    
    def findById(self, id: str) -> User:
        return super().findById(id)
    
    def delete(self, id: str) -> User:
        return super().delete(id)