from datetime import date
from fastapi import FastAPI
from config import initiate_db, Settings
from models import Drug, DrugData
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await initiate_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/drugs")
async def create_drug(drug: DrugData):
    # print(drug.expiration)
    drug = Drug(**drug.dict())
    await drug.save()
    return drug


@app.get("/drugs")
async def get_drugs():
    drugs = await Drug.find_all()
    return drugs


@app.get("/drugs/{drug_id}")
async def get_drug(drug_id: str):
    drug = await Drug.find_one(Drug.id == drug_id)
    return drug


@app.put("/drugs/{drug_id}")
async def update_drug(drug_id: str, drug: DrugData):
    drug = await Drug.find_one(Drug.id == drug_id)
    drug.name = drug.name
    drug.quantity = drug.quantity
    drug.lot = drug.lot
    await drug.save()
    return drug


@app.get("/drugs")
async def search_drugs(name: str):
    drugs = await Drug.find(Drug.name == name)
    return drugs


@app.patch("/drugs/{drug_id}")
async def update_drug(drug_id: str, drug: DrugData):
    drug = await Drug.find_one(Drug.id == drug_id)
    drug.name = drug.name
    drug.quantity = drug.quantity
    drug.lot = drug.lot
    await drug.save()
    return drug


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=Settings().PORT, reload=True)
