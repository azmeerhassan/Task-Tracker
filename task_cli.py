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

def update_task(task_id, new_description):
    if not os.path.exists("tasks.json"):
        print("❗ No tasks found.")
        return

    with open("tasks.json", "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            print("❗ Failed to read task list.")
            return

    # Flag to track if any task was updated
    updated = False

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            updated = True
            break

    if updated:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)
        print(f"✅ Task {task_id} updated successfully.")
    else:
        print(f"❌ Task with ID {task_id} not found.")

def delete_task(task_id):
    if not os.path.exists("tasks.json"):
        print("❗ No tasks file found.")
        return

    with open("tasks.json", "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            print("❗ Could not read tasks file.")
            return

    # Remove task with matching ID
    original_length = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == original_length:
        print(f"❌ Task with ID {task_id} not found.")
        return

    # Save updated list
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

    print(f"🗑️ Task {task_id} deleted successfully.")

def mark_in_progress(task_id):
    if not os.path.exists("tasks.json"):
        print("❗ No tasks file found.")
        return

    with open("tasks.json", "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            print("❗ Could not read tasks file.")
            return

    updated = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            updated = True
            break

    if updated:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)
        print(f"🔄 Task {task_id} marked as 'in-progress'.")
    else:
        print(f"❌ Task with ID {task_id} not found.")


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

    elif command == "update":
        if len(sys.argv) < 4:
            print("❗ Usage: python task_cli.py update <task_id> <new_description>")
        else:
            try:
                task_id = int(sys.argv[2])
                new_description = " ".join(sys.argv[3:])
                update_task(task_id, new_description)
            except ValueError:
                print("❌ Task ID must be an integer.")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("❗ Usage: python task_cli.py delete <task_id>")
        else:
            try:
                task_id = int(sys.argv[2])
                delete_task(task_id)
            except ValueError:
                print("❌ Task ID must be an integer.")

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("❗ Usage: python task_cli.py mark-in-progress <task_id>")
        else:
            try:
                task_id = int(sys.argv[2])
                mark_in_progress(task_id)
            except ValueError:
                print("❌ Task ID must be an integer.")


    else:
        print(f"❌ Unknown command: {command}")


# 📌 Run the main function if this file is executed
if __name__ == "__main__":
    main()
