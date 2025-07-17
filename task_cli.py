import sys             # For reading command-line arguments
import json            # For reading/writing JSON file
import os              # To check if file exists
from datetime import datetime  # For timestamping tasks


# 🔧 Function to add a new task
def add_task(description):
    tasks = []  # Initialize task list

    # Load existing tasks if tasks.json exists
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                tasks = json.load(f)  # Try reading the file
            except json.JSONDecodeError:
                tasks = []  # If file is empty or corrupt, start fresh

    # Generate a new ID based on max existing ID
    new_id = max([task['id'] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()  # Current timestamp

    # Create new task dictionary
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    # Add new task to list and save back to file
    tasks.append(new_task)
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

    print(f"✅ Task added (ID: {new_id})")


# 📋 Function to list all tasks
def list_tasks():
    if not os.path.exists("tasks.json"):
        print("No tasks found.")
        return

    with open("tasks.json", "r") as f:
        tasks = json.load(f)

    if not tasks:
        print("No tasks found.")
        return

    # Display each task nicely
    for task in tasks:
        print(f"[{task['id']}] ({task['status']}) - {task['description']}")


# 🚀 Entry point of the script
def main():
    if len(sys.argv) < 2:
        print("❗ Usage: python task_cli.py <command> [task description]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("❗ Please enter a task description.")
        else:
            # Join all words after 'add' as one description string
            description = " ".join(sys.argv[2:])
            add_task(description)

    elif command == "list":
        list_tasks()

    else:
        print(f"❌ Unknown command: {command}")


# 📌 Run the main function if this file is executed
if __name__ == "__main__":
    main()
