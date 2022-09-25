from datetime import datetime
from fastapi import FastAPI
from config import initiate_db
from models import Drug

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await initiate_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    new_drug = Drug(
        name="Ibuprofen", quantity=100, lot="123456789", expiration=datetime.utcnow()
    )
    await new_drug.save()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
