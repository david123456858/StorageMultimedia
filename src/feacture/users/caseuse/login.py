from datetime import timedelta
from src.feacture.users.repository.user import repositoryUser
from src.shared.utils.result import SuccessProccess,FailureProccess
from src.feacture.users.dtos.user import userDtoLogin
from src.shared.utils.encrypt.hashed import hashing_hashlib,verify_password
from src.security.jwt.jwt_handler import HandleJwt

class caseUseUserLogin():
    
    def __init__(self,repository:repositoryUser) -> None:
        self.repo = repository
        self.hanler_jwt = HandleJwt()
        pass
    def createLogin(self,userDto:userDtoLogin):
        try:
            # getattr(user_find,'password',None)
            # Obtiene lo que tiene de resultado un objeto en este caso
            # seria que va a scar user_find.password y lo convertira en un str 
            
            email_hashed = hashing_hashlib(userDto.email)
            
            user_find = self.repo.find_by_email(email_hashed)
            
            if not user_find:
                return FailureProccess(404,'Not Found')
            
            password_hash = getattr(user_find,'password',None)
            
            if not isinstance(password_hash, str) or password_hash is None:
                return FailureProccess(500, 'Contraseña inválida en base de datos')
            
            result_verify = verify_password(userDto.password,password_hash)
            
            if not result_verify:
                FailureProccess(401,'Contraseña incorrecta')
            
            result = self.hanler_jwt.create_token({"id":user_find.id},timedelta(minutes=30))
            return SuccessProccess(200,result)
        except Exception as e:
            print(e)
            return FailureProccess(500,f'Error internal sever {e}')