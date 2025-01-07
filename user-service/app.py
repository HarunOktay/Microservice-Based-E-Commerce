from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Basit bir veritabanı simülasyonu
users = {}

class User(BaseModel):
    name: str
    email: str

@app.post("/api/users")
async def create_user(user: User):
    users[len(users) + 1] = user
    return {"id": len(users), "user": user}

@app.get("/api/users")
async def get_users():
    return users 