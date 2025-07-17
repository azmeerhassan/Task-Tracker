# 📝 Task Tracker CLI

A simple and lightweight Command-Line Interface (CLI) application to manage your tasks and to-do list using Python.  
All tasks are stored in a local `tasks.json` file. No external libraries or frameworks required.

---

## 🚀 Features

- ✅ Add new tasks
- 📝 Update existing tasks
- 🗑️ Delete tasks
- 🔄 Mark tasks as `in-progress`
- ✅ Mark tasks as `done`
- 📋 List all tasks
- 🎯 Filter tasks by status (`todo`, `in-progress`, `done`)

---

## 🖥️ Requirements

- Python 3.x installed
- Basic terminal or command prompt

---

## 📦 Installation

1. Clone the repository or download the code.
2. Navigate to the project folder:
   ```bash
   cd task-tracker-cli
   ```
3. Make sure you're using Python 3:
   ```bash
   python --version
   ```

---

## ⚙️ Usage

### ▶️ Add a new task
```bash
python task_cli.py add "Buy groceries"
```

### 📝 Update a task
```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### 🗑️ Delete a task
```bash
python task_cli.py delete 1
```

### 🔄 Mark as in-progress
```bash
python task_cli.py mark-in-progress 2
```

### ✅ Mark as done
```bash
python task_cli.py mark-done 3
```

### 📋 List all tasks
```bash
python task_cli.py list
```

### 🎯 Filter tasks by status
```bash
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

---

## 📁 Data Format

All tasks are saved in a `tasks.json` file with this structure:

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2025-07-17T10:30:00",
    "updatedAt": "2025-07-17T10:30:00"
  }
]
```

---

## 🤝 Contributing

This is a beginner-friendly project.  
Feel free to improve it — add search, priorities, deadlines, or even build a web version!

---

## 📚 License

This project is open-source and free to use for learning purposes.

---

## 👨‍💻 Author

Built with 💙 by Azmeer Hassan Ammad  
Student of Computer Systems Engineering  
Dawood University of Engineering and Technology