from datetime import datetime
from todo_app.task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str, description: str = "", due_date: datetime = None):
        """Adds a new task to the manager."""
        task = Task(title, description, due_date)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.")

    def remove_task(self, index: int):
        """Removes a task by its index."""
        try:
            task = self.tasks.pop(index)
            print(f"Task '{task.title}' removed successfully.")
        except IndexError:
            print("Invalid index. Task not found.")

    def get_task(self, index: int):
        """Gets a task by its index."""
        try:
            return self.tasks[index]
        except IndexError:
            print("Invalid index. Task not found.")
            return None

    def update_task(self, index: int, title: str = None, description: str = None, due_date: datetime = None):
        """Updates the details of a task."""
        task = self.get_task(index)
        if task:
            if title:
                task.update_title(title)
            if description:
                task.update_description(description)
            if due_date:
                task.update_due_date(due_date)
            print(f"Task '{task.title}' updated successfully.")

    def mark_task_complete(self, index: int):
        """Marks a task as completed."""
        task = self.get_task(index)
        if task:
            task.mark_complete()
            print(f"Task '{task.title}' marked as completed.")

    def mark_task_incomplete(self, index: int):
        """Marks a task as incomplete."""
        task = self.get_task(index)
        if task:
            task.mark_incomplete()
            print(f"Task '{task.title}' marked as incomplete.")


    def list_tasks(self):
        """Lists all tasks with their details."""
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"Task {index + 1}:\n{task}")

    def list_completed_tasks(self):
        """Lists all completed tasks."""
        completed_tasks = [task for task in self.tasks if task.completed]
        if not completed_tasks:
            print("No completed tasks available.")
        else:
            print("Completed Tasks:")
            for index, task in enumerate(completed_tasks):
                print(f"Task {index + 1}:\n{task}")

    def list_incomplete_tasks(self):
        """Lists all incomplete tasks."""
        incomplete_tasks = [task for task in self.tasks if not task.completed]
        if not incomplete_tasks:
            print("No incomplete tasks available.")
        else:
            print("Incomplete Tasks:")
            for index, task in enumerate(incomplete_tasks):
                print(f"Task {index + 1}:\n{task}")


