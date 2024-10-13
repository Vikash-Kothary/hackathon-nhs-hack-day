from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader

from nhs_hack_day.repositories import user_repository
from nhs_hack_day.repositories import task_repository
from nhs_hack_day.repositories import patient_repository

app = FastAPI(
    docs_url="/"
)
app.mount("/app/static", StaticFiles(directory="src/backend/nhs_hack_day/routes/static"), name="static")

env = Environment(loader=FileSystemLoader("src/backend/nhs_hack_day/routes/templates"))

class User(BaseModel):
    user_id: str
    name: str
    email: str


class Task(BaseModel):
    task_id: str
    task_type: str
    name: str
    description: str


class Patient(BaseModel):
    patient_id: str
    patient_number: str
    full_name: str


@app.get("/app", response_class=HTMLResponse)
async def read_root():
    template = env.get_template("index.html")
    users = user_repository.list_users()
    tasks = task_repository.list_tasks()
    return template.render(tasks=tasks, users=users)


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


@app.get("/api/v1/patients")
def list_patients():
    return patient_repository.list_patients()


@app.post("/api/v1/patients")
def create_new_patient(patient: Patient):
    new_patient = patient_repository.create_new_patient(patient)
    return new_patient.patient_id
