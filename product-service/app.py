from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Basit bir veritabanı simülasyonu
products = {}

class Product(BaseModel):
    name: str
    price: float

@app.post("/api/products")
async def create_product(product: Product):
    products[len(products) + 1] = product
    return {"id": len(products), "product": product}

@app.get("/api/products")
async def get_products():
    return products 