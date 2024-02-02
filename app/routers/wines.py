
from fastapi import APIRouter
from app.db import mongodb
from app.db.models import Wine

router = APIRouter()

@router.get("/wines/")
async def list() -> list[Wine]:
    wines = []
    async for document in mongodb.wine_collection.find():
        wines.append(document)
    return wines

@router.post("/wines/")
async def insert(wine: Wine) -> Wine:
    new_wine = await mongodb.wine_collection.insert_one(wine.model_dump(by_alias=True, exclude=["id"]))
    created_wine = await mongodb.wine_collection.find_one(
        {"_id": new_wine.inserted_id}
    )
    return created_wine
