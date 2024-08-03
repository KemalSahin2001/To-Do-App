from datetime import datetime
from todo_app.task_manager import TaskManager
from todo_app.storage import Storage

class CLI:
    def __init__(self):
        self.task_manager = TaskManager()
        self.storage = Storage()

        # Load existing tasks
        self.storage.load_tasks(self.task_manager)

    def display_menu(self):
        """Displays the main menu."""
        print("\n--- To-Do List Application ---")
        print("1. List all tasks")
        print("2. Add a new task")
        print("3. Update a task")
        print("4. Remove a task")
        print("5. Mark task as completed")
        print("6. Mark task as incomplete")
        print("7. List completed tasks")
        print("8. List incomplete tasks")
        print("9. Save and Exit")
        print("------------------------------")

    def get_user_input(self):
        """Gets the user's menu choice."""
        return input("Enter your choice (1-9): ")

    def list_tasks(self):
        """Lists all tasks."""
        self.task_manager.list_tasks()

    def add_task(self):
        """Adds a new task."""
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date_str = input("Enter due date (YYYY-MM-DD) or leave blank: ")

        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        self.task_manager.add_task(title, description, due_date)

    def update_task(self):
        """Updates an existing task."""
        index = self.get_task_index()
        if index is not None:
            title = input("Enter new task title or leave blank to keep unchanged: ")
            description = input("Enter new task description or leave blank to keep unchanged: ")
            due_date_str = input("Enter new due date (YYYY-MM-DD) or leave blank to keep unchanged: ")

            due_date = None
            if due_date_str:
                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

            self.task_manager.update_task(index, title, description, due_date)

    def remove_task(self):
        """Removes an existing task."""
        index = self.get_task_index()
        if index is not None:
            self.task_manager.remove_task(index)

    def mark_task_complete(self):
        """Marks a task as completed."""
        index = self.get_task_index()
        if index is not None:
            self.task_manager.mark_task_complete(index)

    def mark_task_incomplete(self):
        """Marks a task as incomplete."""
        index = self.get_task_index()
        if index is not None:
            self.task_manager.mark_task_incomplete(index)

    def list_completed_tasks(self):
        """Lists all completed tasks."""
        self.task_manager.list_completed_tasks()

    def list_incomplete_tasks(self):
        """Lists all incomplete tasks."""
        self.task_manager.list_incomplete_tasks()

    def save_and_exit(self):
        """Saves tasks to file and exits the application."""
        self.storage.save_tasks(self.task_manager)
        print("Exiting the application. Goodbye!")
        exit()

    def get_task_index(self):
        """Prompts the user for a task index and validates it."""
        try:
            index = int(input("Enter task number: ")) - 1
            if 0 <= index < len(self.task_manager.tasks):
                return index
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
        return None

    def run(self):
        """Runs the CLI loop."""
        while True:
            self.display_menu()
            choice = self.get_user_input()

            if choice == '1':
                self.list_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.remove_task()
            elif choice == '5':
                self.mark_task_comple
