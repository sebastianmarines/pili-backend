from datetime import date
from fastapi import FastAPI
from config import initiate_db
from models import Drug, DrugData

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await initiate_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/drugs")
async def create_drug(drug: DrugData):
    print(drug.expiration)
    drug = Drug(**drug.dict())
    await drug.save()
    return drug

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


