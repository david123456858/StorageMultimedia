from src.users.dtos.user import userDtoRegiter
from src.shared.utils.result import SuccessProccess,FailureProccess
from src.users.repository.user import repositoryUser
from src.users.entity.user import User
from src.shared.utils.encrypt.hashed import hashing
from src.shared.utils.encrypt.encrypt import encrypt

class caseUseCreateUser():
    def __init__(self,repository:repositoryUser) -> None:
        self.repo = repository
        pass
    ## it´s funtion have the objetive of create the user of the app
    def createUser(self, userDto: userDtoRegiter) :
        try:
            
            user = User(
                id=userDto.id,
                name= userDto.name,
                email= encrypt(userDto.email),
                password= hashing(userDto.password),
                emailhash= hashing(userDto.email)
                        )
            self.repo.save(user)
            return SuccessProccess(200,'todo salio bien')
        except Exception as e:
            print(e)
            return FailureProccess(500,'Error internal sever') 
    