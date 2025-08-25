from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from src.security.idempotency.idempotency_handler import handlerIdempotency

# part feacture
from src.feacture.users.entity.user import User
from src.feacture.multimedia.entity.multimedia import Multimedia

# part routes
from src.feacture.users.routes import routesUser
from src.feacture.multimedia.routes import multimedia 

# part config
from src.config.db.db import dataBaseTurso, Base
from src.config.cloudinary.config import config

from src.shared.utils.encrypt.encrypt import key
from src.shared.middleware.hanlerValidation import validation_Exception_handler
from src.security.jwt.jwt_handler import HandleJwt,MiddlwareJWT

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(
#     handlerIdempotency,
#     ttl=60
# )
##handler_jwt = HandleJwt() 

## app.add_middleware(BaseHTTPMiddleware,dispatch=MiddlwareJWT(handler_jwt,['/api/user/login','api/user/register']))

# Creacion de tablas
Base.metadata.create_all(bind=dataBaseTurso.get_instance())

# method healt data base 
dataBaseTurso.test_connection() 

## apartado de rutas
app.include_router(routesUser.moduleRouterUser(), prefix='/api',tags=['users']) 
app.include_router(multimedia.routeMultimedia(), prefix='/api',tags=['Multimedia'])

## middlerware handler error validation
app.add_exception_handler(RequestValidationError,validation_Exception_handler)  # type: ignore

@app.get('/ping')
def get_health():
    return { "message":" pong "}

#ruta de mi herma y prog steven
@app.get('/hello')
def get_hello():
    return{"message":"konichiwa"}
