import sys
import json
import os

# File where tasks will be saved
TASK_FILE = "tasks.json"

# Load tasks from file (if it exists)
if os.path.exists(TASK_FILE):
    with open(TASK_FILE, "r") as file:
        tasks = json.load(file)
else:
    tasks = []

def save_tasks():
    """Saves tasks to the file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

def show_help():
    """Displays available commands to the user."""
    print("""
Task Manager CLI:
    add <task>     - Add a new task
    list           - List all tasks
    remove <num>   - Remove a task by its number
    help           - Show this help message
    """)

def add_task(task):
    """Adds a new task to the list and saves it."""
    tasks.append(task)
    save_tasks()
    print(f"Added task: {task}")

def list_tasks():
    """Displays all tasks in the list."""
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(task_num):
    """Removes a task by its number and saves the updated list."""
    try:
        task = tasks.pop(task_num - 1)
        save_tasks()
        print(f"Removed task: {task}")
    except IndexError:
        print("Invalid task number.")

# Command-line interface logic
if len(sys.argv) < 2:
    show_help()
else:
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task to add.")
        else:
            add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "remove":
        if len(sys.argv) < 3:
            print("Please provide a task number to remove.")
        else:
            try:
                remove_task(int(sys.argv[2]))
            except ValueError:
                print("Task number should be a valid integer.")
    else:
        show_help()
