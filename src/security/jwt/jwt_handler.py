from fastapi import Request, Response,HTTPException
from dotenv import load_dotenv
from fastapi import  Security
from fastapi.responses import JSONResponse
from datetime import timedelta,datetime,timezone
from typing import Optional
from jose import jwt,JWTError
import os

from src.shared.utils.response.response_factory import ResponseFactory
from src.shared.utils.result import FailureProccess

##load_dotenv()

##SECRET_KEY = os.environ.get('SECRET_KEY')


class HandleJwt():
    def __init__(self) -> None:
        self.secret =  'hola'##os.environ.get('SECRET_KEY') 
        self.algoritm = 'HS256'
        self.expire_minutes = 30
        
        if not self.secret:
            raise ValueError("SECRET_KEY no encontrada en variables de entorno")
    
    def create_token(self,data : dict,expire_time:Optional[timedelta]):
        to_code = data.copy()
        print(to_code, data)
        if expire_time:
            expire = datetime.now(timezone.utc) + expire_time
        else:
            expire = datetime.now(timezone.utc)+ timedelta(minutes=self.expire_minutes)    
            
        to_code.update({"exp":expire})
        if not self.secret:
            return 
        encode_jwt = jwt.encode(to_code,self.secret,algorithm=self.algoritm)
            
        return encode_jwt
    
    
    def verify_token(self,token:str):
        try:
            if not self.secret:
                return 
            payload = jwt.decode(token,self.secret,algorithms=self.algoritm)
            return payload
        except JWTError as e:
            return

class MiddlwareJWT():
    def __init__(self,jwtHanler:HandleJwt,exclude_paths:Optional[list]=None) :
        self.jwt = jwtHanler
        self.exclude_path = exclude_paths or ['/user/login','/register']
        pass
    async def __call__(self, request:Request,next_call) -> Response: 
        try:
            for value in self.exclude_path:
                print(value)
                print(request.url.path)
                if request.url.path.startswith(value):
                    return await next_call(request)
        
            autorization = request.headers.get('authorization')      
            if not autorization:
                return ResponseFactory().create_process(FailureProccess(401,'Header Authorization requerido'))
        
            token = autorization.split(' ')[1]
            
            payload = self.jwt.verify_token(token)
            if payload:
                return await next_call(request)
            
            
            return JSONResponse('Token inválido o expirado',401)
        except HTTPException as e:
            return ResponseFactory().create_process(FailureProccess(e.status_code,e.detail))
        except Exception as e:
            return ResponseFactory().create_process(FailureProccess(500,'Error internal server'))