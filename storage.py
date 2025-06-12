# storage.py

import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    # print(tasks)
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
