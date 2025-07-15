from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.users.routes import routesUser
from src.config.db.db import engine, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
## Creacion de tablas
Base.metadata.create_all(bind=engine)


## apartado de rutas
app.include_router(routesUser.moduleRouterUser(), prefix='/api',tags=['users'])

@app.get('/ping')
def get_health():
    return { "message":" pong "}