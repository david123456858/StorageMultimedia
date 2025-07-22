from src.users.dtos.user import userDtoRegiter
from src.shared.utils.result import SuccessProccess,FailureProccess

class caseUseCreateUser():
    def __init__(self) -> None:
        pass
    
    async def createUser(self, user: userDtoRegiter) :
        try:
            print(user)
            return SuccessProccess(200,'todo salio bien')
        except Exception as e:
            return FailureProccess(500,'Error internal sever')
    