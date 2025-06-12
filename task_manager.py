# task_manager.py

import uuid
import json

def add_task(tasks, title,due_date, description=""):

    task = {
        "uuid": str(uuid.uuid4()) ,
        "id" : str(len(tasks) + 1),         
        "title": title,
        "description": description,
        "status": "Pending",
        "Due Date": due_date 
        
    }
    tasks.append(task)
    return task


 


def list_tasks(tasks):
    return tasks

 

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            return True
    return False

def pending_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Pending"
            return True
    return False

def delete_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return True
    return False
