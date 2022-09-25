from fastapi import FastAPI
from config import initiate_db

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await initiate_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
