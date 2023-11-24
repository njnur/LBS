from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import settings


class DataBase:
    client: AsyncIOMotorClient = None
    db = None


db = DataBase()


async def connect_to_mongo():
    """
    Establishes an asynchronous connection to MongoDB.
    """
    db.client = AsyncIOMotorClient(settings.MONGODB_URL)
    db.db = db.client[settings.MONGODB_DB_NAME]
    print("Connected to MongoDB asynchronously")


async def close_mongo_connection():
    """
    Closes the asynchronous MongoDB connection.
    """
    db.client.close()
    print("Disconnected from MongoDB asynchronously")


async def get_database():
    """
    Returns the asynchronous database instance for use in routes.
    This function can be used as a dependency in FastAPI routes.
    """
    return db.db
