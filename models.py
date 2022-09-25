from datetime import datetime
import pydantic
from beanie import Document


class Drug(Document):
    name: str
    quantity: int
    lot: str
    expiration: datetime

    class Collection:
        name = "drugs"

    class Config:
        schema_extra = {
            "example": {
                "name": "Ibuprofen",
                "quantity": 100,
                "lot": "123456789",
                "expiration": datetime(2021, 12, 31),
            }
        }


class DrugData(pydantic.BaseModel):
    name: str
    quantity: int
    lot: str
    expiration: datetime
