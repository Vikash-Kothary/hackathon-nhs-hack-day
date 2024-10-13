from nhs_hack_day.repositories.impl import google_sheets

tasks = {}

def list_tasks():
    return list(tasks.values())

def create_new_task(task):
    global tasks
    tasks[task.task_id] = task
    return task
