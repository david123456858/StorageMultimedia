from src.users.dtos.user import userDtoRegiter
from src.shared.utils.result import SuccessProccess,FailureProccess
from src.users.repository.user import repositoryUser
from src.users.entity.user import User

class caseUseCreateUser():
    def __init__(self,repository:repositoryUser) -> None:
        self.repo = repository
        pass
    
    def createUser(self, userDto: userDtoRegiter) :
        try:
            
            # response = self.repo.save(user)
            # user = User()
            
            
            print(userDto)
            return SuccessProccess(200,'todo salio bien')
        except Exception as e:
            return FailureProccess(500,'Error internal sever')
    