from nhs_hack_day.repositories.impl import google_sheets

tasks = {}

def list_tasks():
    return google_sheets.get_google_sheets_client()

def create_new_task(task):
    global tasks
    tasks[task.task_id] = task
    return task
