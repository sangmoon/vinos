import os
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from dotenv import load_dotenv

load_dotenv()


class MongoDB:
    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
        self.engine = AIOEngine(client=self.client, database=os.getenv("MONGO_DB_NAME"))
        print("DB 와 연결되었습니다.")

    def close(self):
        self.client.close()

    @property
    def wine_collection(self):
        return self.client[os.getenv("MONGO_DB_NAME")]["wine"]


mongodb = MongoDB()
