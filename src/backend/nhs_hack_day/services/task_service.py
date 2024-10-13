import uuid

from nhs_hack_day.models import Speciality
from nhs_hack_day.repositories import task_repository

def get_speciality(speciality_string: str) -> Speciality:
    speciality_string = speciality_string.lower()
    
    if "resp" in speciality_string or "respiratory" in speciality_string:
        return Speciality.RESPIRATORY_MEDICINE
    elif "gastro" in speciality_string or "gastroenterology" in speciality_string:
        return Speciality.GASTROENTEROLOGY
    elif "micro" in speciality_string or "microbiology" in speciality_string:
        return Speciality.MICROBIOLOGY
    return Speciality.UNKNOWN


def create_new_task(task_description: str):
    task = {}
    task['task_id'] = str(uuid.uuid4())
    task['description'] = task_description
    task['speciality'] = get_speciality(task_description)
    # task['name'] = get_task_name()
    task_repository.create_new_task(task)
    return task
