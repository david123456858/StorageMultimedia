
from src.shared.interfaces.result.result import ISuccessProcess, IFailureProcess

def SuccessProccess(statusCode:int,value):
    response = {
        "value": value,
        "success": True,
        "statusCode": statusCode
    }
    return response

def FailureProccess(statusCode:int,error):
    response = {
        "error": error,
        "success": False,
        "statusCode": statusCode
    }
    return response