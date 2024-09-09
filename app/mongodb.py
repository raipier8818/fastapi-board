from config import config
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

class MongoDB:
    def __init__(self):
        self.client = None
    
    def connect(self):
        self.client = AsyncIOMotorClient(config.mongodb.MONGO_URI)
        self.engine = AIOEngine(client=self.client, database=config.mongodb.MONGO_DB_NAME)
        print("Connected to MongoDB")
        
    def close(self):
        self.client.close()
        print("Closed connection to MongoDB")
        
mongodb = MongoDB()