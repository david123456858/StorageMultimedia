
def SuccessProccess(statusCode:int,value):
    return {
        "value": value,
        "success": True,
        "statusCode": statusCode
    }
   

def FailureProccess(statusCode:int,error):
    return {
        "error": error,
        "success": False,
        "statusCode": statusCode
    }
    
