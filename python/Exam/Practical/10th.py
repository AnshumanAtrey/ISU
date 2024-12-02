#Create a comprehensive Python application integrating multiple concepts.
import tkinter as tk
from tkinter import messagebox
import os

# Task class to represent a task
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.title}: {self.description}"

# Decorator to handle file operations
def file_operations(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    return wrapper

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    @file_operations
    def load_tasks(self):
        """Load tasks from a file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    title, description = line.strip().split(':', 1)
                    self.tasks.append(Task(title, description))

    @file_operations
    def save_tasks(self):
        """Save tasks to a file."""
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title}:{task.description}\n")

    def add_task(self, title, description):
        """Add a new task."""
        new_task = Task(title, description)
        self.tasks.append(new_task)
        self.save_tasks()

    def delete_task(self, title):
        """Delete a task by title."""
        self.tasks = [task for task in self.tasks if task.title != title]
        self.save_tasks()

    def get_tasks(self):
        """Get all tasks as a string."""
        return "\n".join(str(task) for task in self.tasks)

# GUI Application
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management Application")
        self.task_manager = TaskManager("tasks.txt")

        # Create GUI components
        self.title_label = tk.Label(root, text="Task Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.description_label = tk.Label(root, text="Task Description:")
        self.description_label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_button.pack()

        self.tasks_text = tk.Text(root, height=10, width=50)
        self.tasks_text.pack()

    def add_task(self):
        """Add a task to the task manager."""
        title = self.title_entry.get()
        description = self.description_entry.get()
        if title and description:
            self.task_manager.add_task(title, description)
            messagebox.showinfo("Success", "Task added successfully!")
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both title and description.")

    def delete_task(self):
        """Delete a task from the task manager."""
        title = self.title_entry.get()
        if title:
            self.task_manager.delete_task(title)
            messagebox.showinfo("Success", "Task deleted successfully!")
            self.title_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter the title of the task to delete.")

    def view_tasks(self):
        """Display all tasks in the text area."""
        tasks = self.task_manager.get_tasks()
        self.tasks_text.delete(1.0, tk.END)  # Clear the text area
        self.tasks_text.insert(tk.END, tasks)  # Insert tasks into the text area

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()