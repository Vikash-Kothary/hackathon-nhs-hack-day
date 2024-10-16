from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader

from nhs_hack_day.models import TaskType
from nhs_hack_day.services import task_service
from nhs_hack_day.services import automate_service
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
    description: str


class Patient(BaseModel):
    patient_id: str
    patient_number: str
    full_name: str


def task_type_to_string(x):
    x['task_type'] = str(x.get('task_type', TaskType.UNKNOWN))
    return x


@app.get("/app", response_class=HTMLResponse)
async def read_root():
    template = env.get_template("index.html")
    users = user_repository.list_users()
    tasks = list(map(task_type_to_string, task_repository.list_tasks()))
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
    new_task = task_service.create_new_task(task.description)
    return new_task['task_id']


@app.post("/api/v1/tasks/{task_id}/automate")
async def automate_task(task_id: str):
    task = task_repository.get_task_by_id(task_id)
    if (task['task_type'] == TaskType.ADD_ON_BLOODS_TEST):
        automate_service.automate_blood_tests(task)

@app.get("/api/v1/patients")
def list_patients():
    return patient_repository.list_patients()


@app.post("/api/v1/patients")
def create_new_patient(patient: Patient):
    new_patient = patient_repository.create_new_patient(patient)
    return new_patient.patient_id
