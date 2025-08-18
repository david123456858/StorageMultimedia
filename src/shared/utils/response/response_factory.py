from src.shared.interfaces.result.result import ISuccessProcess, IFailureProcess
from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse

class ResponseBuiler(ABC):
    """
    abstract class with finally of have the contract with the products
    """
    @abstractmethod
    def build(self)-> JSONResponse:
        pass
    
    
class ResponseSuccessProcess(ResponseBuiler):
    """
    class that which represents the product of process successfully
    """
    def __init__(self, status_code:int , value:any ) -> None: # type: ignore
        self.status_code = status_code
        self.value = value 
        super().__init__()
        
    def build(self) -> JSONResponse:
        return JSONResponse({"message":self.value},self.status_code)
    
class ResponseFailureProcess(ResponseBuiler):
    """
    class that which represents the product of process Failure
    """
    def __init__(self, status_code:int , error) -> None:
        self.status_code = status_code
        self.error = error
        super().__init__()
        
    def build(self) -> JSONResponse:
        return JSONResponse({"error": self.error},self.status_code)
    
class ResponseFactory:
    """
    factory class that send the type of answer
    """
    @staticmethod
    def create_process(response):
        if response['success']:
            return ResponseSuccessProcess(response['statusCode'],response['value']).build()
        return ResponseFailureProcess(response['statusCode'],response['error']).build()