from pydantic import BaseSettings
import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import Drug


class Settings(BaseSettings):
    DATABASE_URL: str | None = None

    class Config:
        env_file = ".env"
        orm_mode = True


async def initiate_db():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    if client:
        await init_beanie(
            database=client.get_default_database(), document_models=[Drug]
        )
        print("Connected to database")
    else:
        print("Could not connect to database")
        os._exit(1)
