from fastapi import Header, HTTPException, Query
from src.db.mongodb import get_database
from motor.motor_asyncio import AsyncIOMotorCollection


async def get_token_header(x_token: str = Header(...)):
    """
    Dependency to validate a token in the header of a request.
    """
    if x_token != "expected-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str = Query(...)):
    """
    Dependency to validate a token sent as a query parameter.
    """
    if token != "expected-query-token":
        raise HTTPException(status_code=400, detail="Invalid query token")


async def get_poi_collection() -> AsyncIOMotorCollection:
    """
    Dependency to get the POI collection from the database asynchronously.
    This can be used in route handlers to interact with the POI collection.
    """
    db = await get_database()
    return db["poi_collection"]


async def get_user_collection() -> AsyncIOMotorCollection:
    """
    Dependency to get the User collection from the database asynchronously.
    This can be used in route handlers to interact with the User collection.
    """
    db = await get_database()
    return db["user_collection"]
