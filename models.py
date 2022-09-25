from datetime import datetime, date
import pydantic
from beanie import Document


class Drug(Document):
    first_name: str
    last_name: str
    business_name: str | None = None
    email: str
    hospital: str
    name: str
    quantity: int
    lot: str
    #expiration: datetime.fromordinal(int(str))
    expiration: datetime

    class Collection:
        name = "drugs"

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Maya",
                "last_name": "Biendonado",
                "business_name": "Maya's Pharmacy",
                "email": "a@b.tec.mx",
                "hospital": "Hospital 1",
                "name": "Ibuprofen",
                "quantity": 100,
                "lot": "123456789",
                "expiration": "2022-12-04"
            }
        }


class DrugData(pydantic.BaseModel):
    first_name: str
    last_name: str
    business_name: str | None = None
    email: str
    hospital: str | None = None
    name: str
    quantity: int
    lot: str
    #expiration: datetime.fromordinal(int(str))
    expiration: datetime
