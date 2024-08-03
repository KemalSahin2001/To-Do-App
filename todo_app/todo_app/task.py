from datetime import datetime

class Task:
    def __init__(self, title: str, description: str = "", due_date: datetime = None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        """Marks the task as completed."""
        self.completed = True

    def mark_incomplete(self):
        """Marks the task as incomplete."""
        self.completed = False
        print(f"Task '{self.title}' is now marked as incomplete.")

    def update_title(self, new_title: str):
        """Updates the title of the task."""
        self.title = new_title

    def update_description(self, new_description: str):
        """Updates the description of the task."""
        self.description = new_description

    def update_due_date(self, new_due_date: datetime):
        """Updates the due date of the task."""
        self.due_date = new_due_date



    def __str__(self):
        """Returns a string representation of the task."""
        status = "Completed" if self.completed else "Incomplete"
        due_date_str = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No due date"
        return f"Task: {self.title}\nDescription: {self.description}\nDue Date: {due_date_str}\nStatus: {status}\n"

