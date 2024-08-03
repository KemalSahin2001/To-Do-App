import json
from datetime import datetime
from todo_app.task import Task
from todo_app.task_manager import TaskManager

class Storage:
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename

    def save_tasks(self, task_manager: TaskManager):
        """Saves the current tasks to a JSON file."""
        tasks_data = [
            {
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date.isoformat() if task.due_date else None,
                "completed": task.completed
            }
            for task in task_manager.tasks
        ]
        
        with open(self.filename, 'w') as file:
            json.dump(tasks_data, file, indent=4)
        
        print(f"Tasks saved to {self.filename}.")


    def load_tasks(self, task_manager: TaskManager):
        """Loads tasks from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                
                for task_data in tasks_data:
                    due_date = datetime.fromisoformat(task_data["due_date"]) if task_data["due_date"] else None
                    task = Task(
                        title=task_data["title"],
                        description=task_data["description"],
                        due_date=due_date
                    )
                    if task_data["completed"]:
                        task.mark_complete()
                    
                    task_manager.tasks.append(task)
            
            print(f"Tasks loaded from {self.filename}.")
        except FileNotFoundError:
            print(f"No existing file found. Starting with an empty task list.")
        except json.JSONDecodeError:
            print("Error decoding the task file. Starting with an empty task list.")

