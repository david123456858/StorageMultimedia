
from src.shared.interfaces.result.result import ISuccessProcess, IFailureProcess

from typing import TypeVar

T = TypeVar('T')


def SuccessProccess(statusCode:int,value:str):
    response = {
        "value": value,
        "success": True,
        "statusCode": statusCode
    }
    return response

# class SuccessProccess(ISuccessProcess[str]):
#     """Class that show of informations it's procesos

#     Args:
#         ISuccessProcess (_type_): Interface with the contratc
#     """
#     def __init__(self,value : str,code : int):
#         self._success = True 
#         self._value = value
#         self._code = code
        
#     @property
#     def value(self) -> str :
#         return self.value
    
#     @property
#     def code(self) -> int:
#         return self.code
    
def FailureProccess(statusCode:int,error:str):
    response = {
        "error": error,
        "success": True,
        "statusCode": statusCode
    }
    return response
# class FailureProccess(IFailureProcess[str]):
#     """class that show of informations it's procesos

#     Args:
#         IFailureProcess (_type_): Interface with the contratc
#     """
#     def __init__(self,error : str,code : int  ) -> None:
#         self._error = error
#         self._code = code
#         self._success = False
    
#     @property
#     def value(self) -> str :
#         return self.value
    
#     @property
#     def code(self) -> int:
#         return self.code
            