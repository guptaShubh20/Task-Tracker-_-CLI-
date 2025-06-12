# main.py

from task_manager import add_task, list_tasks, complete_task, delete_task,pending_task
from storage import load_tasks, save_tasks
from datetime import datetime

import pandas as pd 

def show_menu():
    print("\nTask Tracker CLI")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Move task to Pending")
    print("5. Delete Task")
    print("6. Exit")
    
    
# show_menu()

def main():
    tasks = load_tasks()
    
    
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
 
        
        if choice == "1":
           title = input("Please Enter your task title: ")
           description = input("Please Enter description (optional): ")

           while True:
                due_date_input = input("Please Enter Due Date in dd/mm/yyyy format: ")
                try:
                  due_date_obj = datetime.strptime(due_date_input, "%d/%m/%Y")
              
                  today = datetime.today().date()
                  print(due_date_obj, today)

                  if due_date_obj.date() < today:
                    print("Due date cannot be in the past. Please enter a future date.")
                  else:                    
                   due_date = due_date_input
                #    print(due_date)
                   break
              
                except ValueError:
                  print("Invalid date format. Please use dd/mm/yyyy.")
      
           task = add_task(tasks, title,due_date, description)
           save_tasks(tasks)
           print(f"Task added with ID: {task['id']}")
        
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                df = pd.DataFrame(tasks)
                
                df["Due Date"] = pd.to_datetime(df["Due Date"], format="%d/%m/%Y", errors="coerce")           
                df.sort_values(by="Due Date", inplace=True)   #sorting task by due date(earliest first)   
                df["Due Date"] = df["Due Date"].dt.strftime("%d/%m/%Y")

                df.index = range(1, len(df) + 1)
                df.index.name = "S.No"
                print(df.to_markdown())
               
                
        elif choice == "3":            
            task_id = input("PLease Enter Task ID to mark as completed: ")
            # print(tasks)
            if complete_task(tasks, task_id):
                # print(tasks)
                save_tasks(tasks)
                print("Task marked as completed.")
            else:
                print("Task not found.")
                
                
        elif choice == "4":            
            task_id = input("Please Enter Task ID to mark as Pending: ")
            # print(tasks)
            if pending_task(tasks, task_id):
                # print(tasks)
                save_tasks(tasks)
                print("Task marked as pending.")
            else:
                print("Task not found.")               
    
         
        elif choice == "5":
            task_id = input("Please Enter yoour Task ID to delete: ")
            if delete_task(tasks, task_id):
                save_tasks(tasks)
                print("Task deleted.")
            else:
                print("Task not found.")
        
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved. Exiting.....")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

