
from src.shared.interfaces.result.result import ISuccessProcess, IFailureProcess


class SuccessProccess(ISuccessProcess[str]):
    def __init__(self,value:str,code:int):
        self._success = True 
        self._value = value
        self._code = code
        
    @property
    def value(self) -> str :
        return self.value
    
    @property
    def code(self) -> int:
        return self.code
    
    
            