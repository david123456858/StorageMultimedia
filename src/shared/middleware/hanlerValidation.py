from fastapi import Request
from fastapi.responses import JSONResponse, Response
from fastapi.exceptions import RequestValidationError


def validation_Exception_handler(req:Request,exc:RequestValidationError) -> Response:
    """Hanler error for validatios Dto"""
    errors = [
        {
            "field":".".join(map(str,err["loc"][1:])),
            "error":err["msg"]
        }
        for err in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content={"details":errors}
    )
    