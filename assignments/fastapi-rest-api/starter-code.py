from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a simple in-memory store
items = {}

class Item(BaseModel):
    name: str
    description: str | None = None

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items.get(item_id, {})

@app.post("/items/", status_code=201)
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item.dict()
    return {"id": item_id, **items[item_id]}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in items:
        items[item_id] = item.dict()
        return items[item_id]
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return items.pop(item_id, {"error": "Item not found"})
