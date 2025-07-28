from src.users.repository.user import repositoryUser
from src.shared.utils.result import SuccessProccess,FailureProccess
from src.users.dtos.user import userDtoLogin
from src.shared.utils.encrypt.hashed import verifyHashed
class caseUseUserLogin():
    
    def __init__(self,repository:repositoryUser) -> None:
        self.repo = repository
        pass
    def createLogin(self,userDto:userDtoLogin):
        try:
            #*
            # getattr(user_find,'password',None)
            # Obtiene lo que tiene de resultado un objeto en este caso
            # seria que va a scar user_find.password y lo convertira en un str 
            
            user_find = self.repo.find_by_email(userDto.email)
            password_hash = getattr(user_find,'password',None)
        
            if not isinstance(password_hash, str) or password_hash is None:
                return FailureProccess(500, 'Contraseña inválida en base de datos')
            
            result_verify = verifyHashed(userDto.password,password_hash)
            if not result_verify:
                FailureProccess(401,'Contraseña incorrecta')
            
            return SuccessProccess(200,'OK')
        except Exception as e:
            print(e)
            return FailureProccess(500,f'Error internal sever {e}')