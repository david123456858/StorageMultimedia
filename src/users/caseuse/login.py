from src.users.repository.user import repositoryUser
from src.shared.utils.result import SuccessProccess,FailureProccess
class caseUseUserLogin():
    
    def __init__(self,repository:repositoryUser) -> None:
        self. repo = repository
        pass
    def createLogin(self,userDto):
        try:
            

            return SuccessProccess(200,'OK')
        except Exception as e:
            return FailureProccess(500,'Error internal sever')