from src.shared.interfaces.result.result import ISuccessProcess, IFailureProcess
from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse

class ResponseBuiler(ABC):
    """
    clase abstracta con el fin de tener el contrato con los productos
    """
    @abstractmethod
    def build(self)-> JSONResponse:
        pass
    
    
class ResponseSuccessProcess(ResponseBuiler):
    """
    clase que representa el producto de proceso recuelto correctamente
    """
    def __init__(self, status_code:int , value ) -> None:
        self.status_code = status_code
        self.value = value 
        super().__init__()
        
    def build(self) -> JSONResponse:
        return JSONResponse(self.value , self.status_code)   
    
class ResponseFailureProcess(ResponseBuiler):
    """
    clase que representa el producto de proceso resulto malo
    """
    def __init__(self, status_code:int , error) -> None:
        self.status_code = status_code
        self.error = error
        super().__init__()
        
    def build(self) -> JSONResponse:
        return JSONResponse(self.error,self.status_code)
    
class ResponseFactory:
    """ Clase factory que arroga el tipo de respuesta correspondiente al que viene de el success
    """
    @staticmethod
    def create_process(success:bool ,data, status_code=200):
        if success:
            return ResponseSuccessProcess(status_code,data).build()
        return ResponseFailureProcess(status_code,data).build()