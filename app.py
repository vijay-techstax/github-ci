import uvicorn
from fastapi import FastAPI

try:
    from settings import PORT
except ImportError:
    raise

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
