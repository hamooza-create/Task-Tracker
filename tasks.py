#--------------------------Libraries-----------------------------

from asyncio import Task
import json
import os
from datetime import datetime
import sys

#------------------saving and loading with json------------------
def  save_task():
    with open("tasks.json", "w") as f :
        json.dump(task_cli, f, indent=4)

def load_task():
    if os.path.isfile("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

task_cli = load_task()

#--------------------------Functions-----------------------------
def add(description):
    new_id = len(task_cli) + 1
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {
        "id": new_id,
        "Description": description,
        "Status": "To-do",
        "CreatedAt": time_now,
        "UpdatedAt": time_now
    }
    task_cli.append(new_task)
    save_task()
    print("Task added successfully (ID: ",new_id,")")


def Upd_status(tsk_id, new_status):
    for tsk in task_cli :
        if tsk["id"] == tsk_id :
            tsk["Status"] = new_status
            tsk["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_task()
            print("Task", tsk_id, "marked as", new_status)

def Upd_desc(tsk1_id,Dscrp):
    for tsk1 in task_cli :
        if tsk1["id"] == tsk1_id :
            tsk1["Description"] = Dscrp
            tsk1["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_task()
            print("Task", tsk1_id, "New description", Dscrp)

def del_task(tsk2_id) :
    for tsk2 in task_cli:
        if tsk2["id"] == tsk2_id :
            task_cli.remove(tsk2)
            for index, task in enumerate(task_cli):
                task["id"] = index + 1
            save_task()
            print("Task with id:",tsk2_id," deleted successfully")

def list_tasks():
    for tasks in task_cli :
        print(
                f"\nID: {tasks['id']}, "
                f"\nDescription: {tasks['Description']}, "
                f"\nStatus: {tasks['Status']}, "
                f"\nCreated At: {tasks['CreatedAt']}, "
                f"\nUpdated At: {tasks['UpdatedAt']}"
) 
        
def tsk_sts(tsk_status):
    for tasks in task_cli :
        if tasks["Status"] == tsk_status :
            print(
                    f"\nID: {tasks['id']}, "
                    f"\nDescription: {tasks['Description']}, "
                    f"\nStatus: {tasks['Status']}, "
                    f"\nCreated At: {tasks['CreatedAt']}, "
                    f"\nUpdated At: {tasks['UpdatedAt']}"
) 

def show_help():
    print("""
==================== TASK CLI - CHEAT SHEET ====================

  add "description"
      Add a new task
      Example: task_cli.py add "Buy groceries"

  update-status <id> <status>
      Change a task's status (todo / in-progress / done)
      Example: task_cli.py update-status 1 done

  update-description <id> "new description"
      Change a task's description
      Example: task_cli.py update-description 1 "Buy milk"

  delete-task <id>
      Delete a task by its ID
      Example: task_cli.py delete-task 1

  list-tasks
      Show all tasks

  list-tasks-status <status>
      Show only tasks with a specific status
      Example: task_cli.py list-tasks-status done

  help
      Show this message

===================================================================
""")
    
def main():
        
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: please provide a task description")
            return
        description = sys.argv[2]
        add(description)

    elif command == "update-status" :
        if len(sys.argv) < 3 :
            print("Error: please provide a task ID and a new status")
            return
        tsk_id = int(sys.argv[2])
        new_status = (sys.argv[3])

        sts = ["todo", "in-progress", "done"]
        if new_status not in sts :
            print("error: choose a valide status"
                    "\nto-do   or   in-progress   or   done")  
        else : 
            Upd_status(tsk_id,new_status)                  
            if new_status == "done":
                A_n = input("do you want to delete this task y/n :")
                if A_n == "y" :
                    del_task(tsk_id) 
                else :
                    print()

    elif command == "update-description" :

        if len(sys.argv) < 3 :
            print("Error: please provide a task ID and a new description")
            return
        tsk1_id = int(sys.argv[2])
        description = sys.argv[3]
        Upd_desc(tsk1_id,description)
    
    elif command == "delete-task" :
        if len(sys.argv) < 3 :
            print("Error: please provide a task ID to delete")
            return
        tsk2_id = int(sys.argv[2])
        del_task(tsk2_id) 

    elif command == "list-tasks" :
        list_tasks()

    elif command == "list-tasks-status" :
        if len(sys.argv) < 3 :
            print("Error: please provide a status")
            return
        tsk_status = (sys.argv[2])
        tsk_sts(tsk_status) 

    elif command == "help" :
        if len(sys.argv) < 2:
            return
        show_help()       
    
    else:
        print("Error: unknown command")
        show_help()

    
if __name__ == "__main__":
    main()
    