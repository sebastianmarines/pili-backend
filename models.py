from datetime import datetime, date
import pydantic
from beanie import Document


class Drug(Document):
    hospital: str | None = None
    name: str
    quantity: int
    lot: str

    class Collection:
        name = "drugs"

    class Config:
        schema_extra = {
            "example": {
                "hospital": "Hospital 1",
                "name": "Ibuprofen",
                "quantity": 100,
                "lot": "123456789",
            }

        }


class DrugData(pydantic.BaseModel):
    hospital: str | None = None
    name: str
    quantity: int
    lot: str
