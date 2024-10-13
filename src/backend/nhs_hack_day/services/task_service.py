import uuid

from nhs_hack_day.models import TaskType
from nhs_hack_day.repositories import task_repository

def get_task_type(speciality_string: str) -> TaskType:
    speciality_string = speciality_string.lower()
    
    if "resp" in speciality_string or "respiratory" in speciality_string:
        return TaskType.RESPIRATORY_MEDICINE
    elif "gastro" in speciality_string or "gastroenterology" in speciality_string:
        return TaskType.GASTROENTEROLOGY
    elif "micro" in speciality_string or "microbiology" in speciality_string:
        return TaskType.MICROBIOLOGY
    elif "add" in speciality_string or "blood" in speciality_string:
        return TaskType.ADD_ON_BLOODS_TEST
    elif "refer" in speciality_string and ("inpatient" in speciality_string or "d/c" in speciality_string or "r/f" in speciality_string):
        return TaskType.REFER_INPATIENT_MEDICAL_SPECIALITY
    elif "outpatient" in speciality_string or "clinic" in speciality_string or "appointment" in speciality_string:
        return TaskType.REFER_OUTPATIENT_CLINIC
    elif ("prescribe" in speciality_string or "drug" in speciality_string or 
          "iv" in speciality_string or "antibiotics" in speciality_string or 
          "abx" in speciality_string or "analgesia" in speciality_string or 
          "anti-emetic" in speciality_string or "laxative" in speciality_string):
        return TaskType.DECIDE_ON_PRESCRIPTION
    
    return TaskType.UNKNOWN


def create_new_task(task_description: str):
    task = {}
    task['task_id'] = str(uuid.uuid4())
    task['description'] = task_description
    task['task_type'] = get_task_type(task_description)
    # task['name'] = get_task_name()
    task_repository.create_new_task(task)
    return task
