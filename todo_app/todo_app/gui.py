import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
from todo_app.task_manager import TaskManager
from todo_app.storage import Storage

class GUI:
    def __init__(self, root):
        self.task_manager = TaskManager()
        self.storage = Storage()

        # Load existing tasks
        self.storage.load_tasks(self.task_manager)

        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("600x400")

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.save_and_exit)

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Task List
        self.task_listbox = tk.Listbox(self.root, height=15, width=50)
        self.task_listbox.pack(pady=10)

        # Add Task Button
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Edit Task Button
        self.edit_task_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_task_button.pack(pady=5)

        # Remove Task Button
        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

        # Complete Task Button
        self.complete_task_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Uncheck Task Button
        self.uncheck_task_button = tk.Button(self.root, text="Uncheck Task", command=self.incomplete_task)
        self.uncheck_task_button.pack(pady=5)

        # Refresh Button
        self.refresh_button = tk.Button(self.root, text="Refresh List", command=self.refresh_task_list)
        self.refresh_button.pack(pady=5)

        # Save and Exit Button
        self.save_exit_button = tk.Button(self.root, text="Save and Exit", command=self.save_and_exit)
        self.save_exit_button.pack(pady=10)

        # Initial List Load
        self.refresh_task_list()

    def refresh_task_list(self):
        """Refreshes the task list display."""
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.tasks:
            status = "✓" if task.completed else "✗"
            self.task_listbox.insert(tk.END, f"{task.title} | Due: {task.due_date if task.due_date else 'No due date'} | {status}")

    def add_task(self):
        """Opens a dialog to add a new task."""
        self.open_task_dialog("Add Task")

    def edit_task(self):
        """Opens a dialog to edit the selected task."""
        selected_index = self.get_selected_task_index()
        if selected_index is not None:
            self.open_task_dialog("Edit Task", selected_index)

    def remove_task(self):
        """Removes the selected task."""
        selected_index = self.get_selected_task_index()
        if selected_index is not None:
            self.task_manager.remove_task(selected_index)
            self.refresh_task_list()

    def complete_task(self):
        """Marks the selected task as completed."""
        selected_index = self.get_selected_task_index()
        if selected_index is not None:
            self.task_manager.mark_task_complete(selected_index)
            self.refresh_task_list()

    def incomplete_task(self):
        """Marks the selected task as incomplete."""
        selected_index = self.get_selected_task_index()
        if selected_index is not None:
            self.task_manager.mark_task_incomplete(selected_index)
            self.refresh_task_list()

    def open_task_dialog(self, action, task_index=None):
        """Opens a dialog for adding or editing a task."""
        dialog = tk.Toplevel(self.root)
        dialog.title(action)
        dialog.geometry("300x300")  # Adjust the size to fit the DateEntry widget

        # Task Title
        title_label = tk.Label(dialog, text="Task Title")
        title_label.pack(pady=5)
        title_entry = tk.Entry(dialog, width=30)
        title_entry.pack(pady=5)

        # Task Description
        desc_label = tk.Label(dialog, text="Task Description")
        desc_label.pack(pady=5)
        desc_entry = tk.Entry(dialog, width=30)
        desc_entry.pack(pady=5)

        # Task Due Date
        due_date_label = tk.Label(dialog, text="Due Date")
        due_date_label.pack(pady=5)

        # Using DateEntry widget for due date
        due_date_entry = DateEntry(dialog, width=30, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        due_date_entry.pack(pady=5)

        # Fill existing task data for editing
        if task_index is not None:
            task = self.task_manager.get_task(task_index)
            title_entry.insert(tk.END, task.title)
            desc_entry.insert(tk.END, task.description)
            if task.due_date:
                due_date_entry.set_date(task.due_date)

        # Action Button
        action_button = tk.Button(
            dialog,
            text=action,
            command=lambda: self.save_task(dialog, title_entry.get(), desc_entry.get(), due_date_entry.get_date().strftime("%Y-%m-%d"), task_index)
        )
        action_button.pack(pady=10)

    def save_task(self, dialog, title, description, due_date_str, task_index=None):
        """Saves a task, either adding a new one or updating an existing one."""
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
                return

        if task_index is None:
            # Add new task
            self.task_manager.add_task(title, description, due_date)
        else:
            # Update existing task
            self.task_manager.update_task(task_index, title, description, due_date)

        dialog.destroy()
        self.refresh_task_list()

    def get_selected_task_index(self):
        """Gets the index of the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            return selected_index
        except IndexError:
            messagebox.showerror("Selection Error", "Please select a task.")
            return None

    def save_and_exit(self):
        """Saves tasks to file and exits the application."""
        self.storage.save_tasks(self.task_manager)
        print("Saving tasks and exiting.")
        self.root.destroy()

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
