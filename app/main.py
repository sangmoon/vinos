from fastapi import FastAPI

from contextlib import asynccontextmanager
from app.db import mongodb

from app.routers import wines

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongodb.connect()
    yield
    mongodb.close()

app = FastAPI(lifespan=lifespan)
app.include_router(wines.router)

