from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorCollection
from src.dependencies import get_user_collection
from src.models.user_model import UserModel, UserUpdateModel


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserModel)
async def create_user(user: UserModel, collection: AsyncIOMotorCollection = Depends(get_user_collection)):
    result = await collection.insert_one(user.dict())
    if result.inserted_id:
        return {**user.dict(), "_id": result.inserted_id}
    raise HTTPException(status_code=400, detail="Failed to create user")


@router.get("/{user_id}", response_model=UserModel)
async def get_user(user_id: str, collection: AsyncIOMotorCollection = Depends(get_user_collection)):
    user = await collection.find_one({"_id": user_id})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{user_id}", response_model=UserModel)
async def update_user(user_id: str, user_update: UserUpdateModel,
                      collection: AsyncIOMotorCollection = Depends(get_user_collection)):
    updated_user = await collection.find_one_and_update({"_id": user_id}, {"$set": user_update.dict()},
                                                        return_document=True)
    if updated_user:
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, collection: AsyncIOMotorCollection = Depends(get_user_collection)):
    result = await collection.delete_one({"_id": user_id})
    if result.deleted_count:
        return
    raise HTTPException(status_code=404, detail="User not found")
