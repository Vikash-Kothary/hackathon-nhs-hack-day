from fastapi import FastAPI
from pydantic import BaseModel

from nhs_hack_day.repositories import user_repository

app = FastAPI(
    docs_url="/"
)

class User(BaseModel):
    user_id: str
    name: str
    email: str

@app.get("/api/v1/users")
def list_users():
    return user_repository.list_users()

@app.post("/api/v1/users")
def create_new_user(user: User):
    new_user = user_repository.create_new_user(user)
    return new_user.user_id