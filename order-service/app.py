from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

# Basit bir veritabanı simülasyonu
orders = {}

class Order(BaseModel):
    username: str
    product_names: List[str]
    total: float

@app.post("/api/orders")
async def create_order(order: Order):
    # Kullanıcı kontrolü
    try:
        users_response = requests.get("http://user-service:8001/api/users")
        users = users_response.json()
        user_exists = False
        for user_id, user_data in users.items():
            if user_data.get("name") == order.username:
                user_exists = True
                break
        if not user_exists:
            raise HTTPException(status_code=404, detail=f"Kullanıcı bulunamadı: {order.username}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Kullanıcı servisi hatası: {str(e)}")

    # Ürün kontrolü
    try:
        products_response = requests.get("http://product-service:8002/api/products")
        products = products_response.json()
        for product_name in order.product_names:
            product_exists = False
            for product_id, product_data in products.items():
                if product_data.get("name") == product_name:
                    product_exists = True
                    break
            if not product_exists:
                raise HTTPException(status_code=404, detail=f"Ürün bulunamadı: {product_name}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ürün servisi hatası: {str(e)}")

    # Sipariş oluştur
    order_id = len(orders) + 1
    orders[order_id] = order
    return {"id": order_id, "order": order}

@app.get("/api/orders")
async def get_orders():
    return orders