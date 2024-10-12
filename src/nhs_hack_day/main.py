from fastapi import FastAPI
from pydantic import BaseModel

from nhs_hack_day.repositories import user_repository
from nhs_hack_day.repositories import task_repository

app = FastAPI(
    docs_url="/"
)

class User(BaseModel):
    user_id: str
    name: str
    email: str


class Task(BaseModel):
    task_id: str
    name: str
    description: str


class Patient(BaseModel):
    patient_id: str
    patient_number: str
    full_name: str


@app.get("/api/v1/users")
def list_users():
    return user_repository.list_users()


@app.post("/api/v1/users")
def create_new_user(user: User):
    new_user = user_repository.create_new_user(user)
    return new_user.user_id


@app.get("/api/v1/tasks")
def list_tasks():
    return task_repository.list_tasks()


@app.post("/api/v1/tasks")
def create_new_task(task: Task):
    new_task = task_repository.create_new_task(task)
    return new_task.task_id
