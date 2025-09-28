from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo para los items
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

# Lista en memoria
items_db = []

@app.get("/items")
def get_items():
    return items_db

@app.post("/items")
def create_item(item: Item):
    items_db.append(item.dict())
    return {"message": "Item creado", "item": item}
