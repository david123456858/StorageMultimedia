from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.users.routes import routesUser

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routesUser.moduleRouterUser(), prefix='/api',tags=['users'])

@app.get('/ping')
def get_health():
    return { "message":" pong "}