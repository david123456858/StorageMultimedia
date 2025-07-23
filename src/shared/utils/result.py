
from src.shared.interfaces.result.result import ISuccessProcess, IFailureProcess

def SuccessProccess(statusCode:int,value:str):
    response = {
        "value": value,
        "success": True,
        "statusCode": statusCode
    }
    return response

def FailureProccess(statusCode:int,error:str):
    response = {
        "error": error,
        "success": True,
        "statusCode": statusCode
    }
    return response