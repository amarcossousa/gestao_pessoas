from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infra.sqlalchemy.config.database import criar_bd
from routers import rotas_pessoas

criar_bd()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rotas_pessoas.router)





