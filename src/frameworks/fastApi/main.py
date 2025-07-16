from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.users.routes import routesUser
from src.images.routes import images
from src.config.db.db import dataBaseTurso, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# Creacion de tablas
Base.metadata.create_all(bind=dataBaseTurso.get_instance())


## apartado de rutas
app.include_router(routesUser.moduleRouterUser(), prefix='/api',tags=['users'])
app.include_router(images.routeImages(), prefix='/api',tags=['Images'])

@app.get('/ping')
def get_health():
    return { "message":" pong "}