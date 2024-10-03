import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime, timedelta
from tkcalendar import DateEntry
import tkinter.font as tkFont
import json

# Global list to store tasks
todos = []
selected_index = None

# Path to the tasks file
TASKS_FILE = 'todos.txt'

def load_tasks():
    """
    Load tasks from a file and convert due_date strings to datetime.date objects.
    """
    global todos
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
            # Convert due_date strings to datetime.date objects
            for task in tasks:
                if task['due_date']:
                    task['due_date'] = datetime.strptime(task['due_date'], '%Y-%m-%d').date()
            todos = tasks
    except (FileNotFoundError, json.JSONDecodeError):
        todos = []  # Initialize with an empty list

def save_tasks():
    """
    Save tasks to a file with due_date as strings.
    """
    tasks_to_save = []
    for task in todos:
        if isinstance(task['due_date'], datetime):
            task['due_date'] = task['due_date'].strftime('%Y-%m-%d')
        tasks_to_save.append(task)
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks_to_save, file)

def open_task_window(title, task=None):
    """
    Open a window for adding or editing a task.
    """
    is_edit = task is not None
    task_window = tk.Toplevel(root)
    task_window.title(title)

    tk.Label(task_window, text="What is your To-Do?").pack()
    task_entry = tk.Entry(task_window, width=40)
    if is_edit:
        task_entry.insert(0, task['task'])
    task_entry.pack()

    tk.Label(task_window, text="Due Date:").pack()
    due_date_entry = DateEntry(task_window, width=12, background='darkblue', foreground='white', borderwidth=2)
    if is_edit and task['due_date']:
        due_date_entry.set_date(datetime.strptime(task['due_date'], '%Y-%m-%d').date())
    due_date_entry.pack()

    tk.Label(task_window, text="Set Priority:").pack()
    priority_var = tk.StringVar(value=task['priority'].capitalize() if is_edit else 'Medium')
    priority_menu = tk.OptionMenu(task_window, priority_var, 'High', 'Medium', 'Low')
    priority_menu.pack()

    def save_task():
        """
        Save the task and close the window.
        """
        task_text = task_entry.get().strip()
        due_date = due_date_entry.get_date() if due_date_entry.get() else None
        priority = priority_var.get().lower() if priority_var.get().lower() in ['high', 'medium', 'low'] else 'medium'

        if task_text:
            due_date_str = due_date.strftime('%Y-%m-%d') if due_date else None
            task_data = {'task': task_text, 'due_date': due_date_str, 'priority': priority}
            if is_edit:
                todos[selected_index] = task_data
            else:
                todos.append(task_data)
            refresh_listbox()
            save_tasks()
            task_window.destroy()
        else:
            messagebox.showerror("Error", "Task cannot be empty.")

    tk.Button(task_window, text="Save", command=save_task).pack()

def add_task():
    """
    Open a window to add a new task.
    """
    open_task_window("Add New Task")

def edit_task():
    """
    Open a window to edit the selected task.
    """
    global selected_index
    if selected_index is None:
        messagebox.showwarning("Warning", "No task selected to edit.")
        return

    task = todos[selected_index]
    open_task_window("Edit Task", task)

def delete_task():
    """
    Delete the selected task.
    """
    global selected_index
    if selected_index is None:
        messagebox.showwarning("Warning", "No task selected to delete.")
        return

    del todos[selected_index]
    selected_index = None
    refresh_listbox()
    save_tasks()

def on_select(event):
    """
    Handle selection change in the Listbox.
    """
    global selected_index
    selection = listbox.curselection()
    if selection:
        selected_index = selection[0]
    else:
        selected_index = None
    print(f"Selected index: {selected_index}")  # Debugging line

def refresh_listbox(specific_todos=None):
    """
    Refresh the Listbox display with tasks from a specific list.
    """
    listbox.delete(0, tk.END)
    for idx, todo in enumerate(specific_todos or todos, 1):
        task_str = f"{idx}: {todo['task']}"
        if todo['due_date']:
            task_str += f" (Due: {todo['due_date']})"
        task_str += f" [Priority: {todo['priority'].capitalize()}]"
        listbox.insert(tk.END, task_str)

def search_tasks():
    """
    Search for tasks containing a specific term.
    """
    query = simpledialog.askstring("Search", "Enter search term:")
    if query:
        filtered_todos = [todo for todo in todos if query.lower() in todo['task'].lower()]
        refresh_listbox(filtered_todos)

def sort_by_priority():
    """
    Sort tasks by priority.
    """
    priority_order = {'high': 1, 'medium': 2, 'low': 3}
    todos.sort(key=lambda x: priority_order[x['priority']])
    refresh_listbox()

def check_reminders():
    """
    Check for upcoming due dates and display reminders.
    """
    today = datetime.today().date()
    for todo in todos:
        due_date = datetime.strptime(todo['due_date'], '%Y-%m-%d').date() if isinstance(todo['due_date'], str) else todo['due_date']
        if due_date and due_date <= today + timedelta(days=1):
            messagebox.showinfo("Reminder", f"Task '{todo['task']}' is due soon!")
    root.after(60000, check_reminders)  # Check every minute

# Setup the main application window
root = tk.Tk()
root.title("To-Do List")
font = tkFont.Font(family="Arial", size=12)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Bind selection event
listbox.bind('<<ListboxSelect>>', on_select)

# Buttons for user actions
btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(fill=tk.X)

btn_edit = tk.Button(root, text="Edit Task", command=edit_task)
btn_edit.pack(fill=tk.X)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete.pack(fill=tk.X)

btn_sort = tk.Button(root, text="Sort by Priority", command=sort_by_priority)
btn_sort.pack(fill=tk.X)

btn_search = tk.Button(root, text="Search Tasks", command=search_tasks)
btn_search.pack(fill=tk.X)

# Load tasks from file and start checking for reminders
load_tasks()
refresh_listbox()
check_reminders()

# Start the application
root.mainloop()
