from src.shared.interfaces.repository.repositoryCrud import repositoryCrud
from src.users.entity.user import User
from src.config.db.db import dataBaseTurso

class repositoryUser(repositoryCrud[User]):
    """_summary_

    Args:
        repositoryCrud (User): this is class that did CRUD with database
    """
    def __init__(self) -> None:
        self.session = dataBaseTurso._sessionLocal()
        super().__init__()
        
    def save(self, entity: User):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()
        
    
    def update(self, entity: User):
        return super().update(entity)
    
    def findAll(self) -> list[User]:
        return self.session.query(User).all()
    
    def findById(self, id: str) -> (User | None):
        return self.session.query(User).filter(User.id == id).first()
    
    def delete(self, id: str):
        return super().delete(id)