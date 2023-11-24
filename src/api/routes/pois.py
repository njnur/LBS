from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorCollection
from src.dependencies import get_poi_collection
from src.models.poi_model import POIModel, POIUpdateModel


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=POIModel)
async def create_poi(poi: POIModel, collection: AsyncIOMotorCollection = Depends(get_poi_collection)):
    result = await collection.insert_one(poi.dict())
    if result.inserted_id:
        return {**poi.dict(), "_id": result.inserted_id}
    raise HTTPException(status_code=400, detail="Failed to create POI")


@router.get("/{poi_id}", response_model=POIModel)
async def get_poi(poi_id: str, collection: AsyncIOMotorCollection = Depends(get_poi_collection)):
    poi = await collection.find_one({"_id": poi_id})
    if poi:
        return poi
    raise HTTPException(status_code=404, detail="POI not found")


@router.put("/{poi_id}", response_model=POIModel)
async def update_poi(poi_id: str, poi_update: POIUpdateModel,
                     collection: AsyncIOMotorCollection = Depends(get_poi_collection)):
    updated_poi = await collection.find_one_and_update({"_id": poi_id}, {"$set": poi_update.dict()},
                                                       return_document=True)
    if updated_poi:
        return updated_poi
    raise HTTPException(status_code=404, detail="POI not found")


@router.delete("/{poi_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_poi(poi_id: str, collection: AsyncIOMotorCollection = Depends(get_poi_collection)):
    result = await collection.delete_one({"_id": poi_id})
    if result.deleted_count:
        return
    raise HTTPException(status_code=404, detail="POI not found")
