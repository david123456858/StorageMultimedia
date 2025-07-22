from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from src.users.routes import routesUser
from src.images.routes import images
from src.config.db.db import dataBaseTurso, Base
from src.users.entity.user import User
from src.shared.middleware.hanlerValidation import validation_Exception_handler
from src.config.cloudinary.config import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creacion de tablas
Base.metadata.create_all(bind=dataBaseTurso.get_instance())

# method healt data base 
dataBaseTurso.test_connection() 


## apartado de rutas
app.include_router(routesUser.moduleRouterUser(), prefix='/api',tags=['users'])
app.include_router(images.routeImages(), prefix='/api',tags=['images']) 

## middlerware handler error validation
app.add_exception_handler(RequestValidationError,validation_Exception_handler)  # type: ignore

@app.get('/ping')
def get_health():
    return { "message":" pong "}

#ruta de mi herma y prog steven
@app.get('/hello')
def get_hello():
    return{"message":"konichiwa"}
