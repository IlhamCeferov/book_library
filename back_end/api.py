from fastapi import FastAPI
import uvicorn

from service.service import get_book_info

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/{item_id}")
def get_book_data(item_id: str):
    return get_book_info(item_id)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)