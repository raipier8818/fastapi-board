from contextlib import asynccontextmanager
from config import config
from motor.motor_asyncio import AsyncIOMotorClient

class MongoDB:
    def __init__(self):
        self.client = None

    def connect(self):
        self.client = AsyncIOMotorClient(config.mongodb.MONGO_URI)
        self.db = self.client[config.mongodb.MONGO_DB_NAME]
        print("Connected to MongoDB")

    def close(self):
        self.client.close()
        print("Closed connection to MongoDB")

    def collection(self, collection_name: str):
        return self.db[collection_name]

    async def get_all_collections(self):
        return await self.db.list_collection_names()


mongodb = MongoDB()
