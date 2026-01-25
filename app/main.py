from fastapi import FastAPI
from app.api.v1 import users, games

app = FastAPI()

BASE_API_URL = "/api/v1"

app.include_router(users.router, prefix=BASE_API_URL)
app.include_router(games.router, prefix=BASE_API_URL)
