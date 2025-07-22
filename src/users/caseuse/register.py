from src.users.dtos.user import userDtoRegiter
from src.shared.utils.result import SuccessProccess,FailureProccess
from src.shared.interfaces.result.result import ISuccessProcess,IFailureProcess
from typing import Any

class caseUseCreateUser():
    def __init__(self) -> None:
        pass
    
    async def createUser(self, user: userDtoRegiter) :
        try:
            # Your user creation logic here
            # For example, if successful:
            return SuccessProccess(200,'todo salio bien')
        except Exception as e:
            return FailureProccess(500,'Error internal sever')
    