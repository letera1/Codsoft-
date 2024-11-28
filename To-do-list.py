import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime, timedelta


class Task:
    def __init__(self, name, due_date=None, estimated_time=None, priority="Medium"):
        self.name = name
        self.due_date = due_date
        self.estimated_time = estimated_time
        self.priority = priority
        self.completed = False
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        self.start_time = datetime.now()

    def stop_timer(self):
        self.end_time = datetime.now()

    def get_elapsed_time(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return timedelta()


class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.configure(bg="#001F3F")  # Set dark blue background color

        self.tasks = []

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, width=50, height=10, bg="#001F3F", fg="white")
        self.task_listbox.pack(pady=10)

        # Buttons for actions
        add_button = tk.Button(self.master, text="Add Task", command=self.add_task, bg="#0074CC", fg="white")
        add_button.pack(side=tk.LEFT, padx=5)

        edit_button = tk.Button(self.master, text="Edit Task", command=self.edit_task, bg="#FF8800", fg="white")
        edit_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task, bg="#FF3333", fg="white")
        delete_button.pack(side=tk.LEFT, padx=5)

        complete_button = tk.Button(self.master, text="Mark as Complete", command=self.complete_task, bg="#00C851",
                                    fg="white")
        complete_button.pack(side=tk.LEFT, padx=5)

        # Buttons for time management
        start_timer_button = tk.Button(self.master, text="Start Timer", command=self.start_timer, bg="#AA66CC",
                                       fg="white")
        start_timer_button.pack(side=tk.LEFT, padx=5)

        stop_timer_button = tk.Button(self.master, text="Stop Timer", command=self.stop_timer, bg="#673AB7", fg="white")
        stop_timer_button.pack(side=tk.LEFT, padx=5)

        # Dropdown for priority levels
        self.priority_var = tk.StringVar(self.master)
        self.priority_var.set("Medium")  # default priority
        priority_menu = tk.OptionMenu(self.master, self.priority_var, "High", "Medium", "Low")
        priority_menu.config(bg="#001F3F", fg="white")
        priority_menu.pack(side=tk.RIGHT, padx=5)

        # Search Entry and Button
        self.search_var = tk.StringVar(self.master)
        search_entry = tk.Entry(self.master, textvariable=self.search_var, width=20, bg="#004080", fg="white")
        search_entry.pack(side=tk.RIGHT, padx=5)
        search_button = tk.Button(self.master, text="Search", command=self.search_tasks, bg="#005cbf", fg="white")
        search_button.pack(side=tk.RIGHT, padx=5)

        # Sorting Option
        sort_options = ["Name", "Due Date", "Priority", "Completion Status"]
        self.sort_var = tk.StringVar(self.master)
        self.sort_var.set("Name")  # default sorting
        sort_menu = tk.OptionMenu(self.master, self.sort_var, *sort_options, command=self.sort_tasks)
        sort_menu.config(bg="#001F3F", fg="white")
        sort_menu.pack(side=tk.RIGHT, padx=5)

        # Update the task listbox
        self.update_task_listbox()

    def add_task(self):
        task_name = simpledialog.askstring("Add Task", "Enter task name:")
        if task_name:
            due_date = simpledialog.askstring("Add Task", "Enter due date (YYYY-MM-DD HH:MM):")
            estimated_time = simpledialog.askfloat("Add Task", "Enter estimated time (in hours):")
            due_date = datetime.strptime(due_date, "%Y-%m-%d %H:%M") if due_date else None

            new_task = Task(name=task_name, due_date=due_date, estimated_time=estimated_time,
                            priority=self.priority_var.get())
            self.tasks.append(new_task)
            self.update_task_listbox()

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            new_name = simpledialog.askstring("Edit Task", "Enter new task name:", initialvalue=task.name)
            if new_name:
                task.name = new_name
                self.update_task_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_listbox()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task.completed = not task.completed
            self.update_task_listbox()

    def start_timer(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task.start_timer()
            messagebox.showinfo("Timer Started", f"Timer started for task: {task.name}")

    def stop_timer(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task.stop_timer()
            elapsed_time = task.get_elapsed_time()
            messagebox.showinfo("Timer Stopped", f"Timer stopped for task: {task.name}\nElapsed Time: {elapsed_time}")

    def search_tasks(self):
        keyword = self.search_var.get().lower()
        filtered_tasks = [task for task in self.tasks if keyword in task.name.lower()]
        self.display_tasks(filtered_tasks)

    def sort_tasks(self, *args):
        sort_key = self.sort_var.get()
        if sort_key == "Name":
            self.tasks.sort(key=lambda x: x.name)
        elif sort_key == "Due Date":
            self.tasks.sort(key=lambda x: x.due_date or datetime.max)
        elif sort_key == "Priority":
            self.tasks.sort(key=lambda x: x.priority)
        elif sort_key == "Completion Status":
            self.tasks.sort(key=lambda x: x.completed)
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[ ]" if not task.completed else "[X]"
            due_date_str = f" - Due: {task.due_date}" if task.due_date else ""
            estimated_time_str = f" - Estimated Time: {task.estimated_time} hours" if task.estimated_time else ""
            priority_str = f" - Priority: {task.priority}"
            self.task_listbox.insert(tk.END, f"{status} {task.name}{due_date_str}{estimated_time_str}{priority_str}")

    def display_tasks(self, tasks):
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            status = "[ ]" if not task.completed else "[X]"
            due_date_str = f" - Due: {task.due_date}" if task.due_date else ""
            estimated_time_str = f" - Estimated Time: {task.estimated_time} hours" if task.estimated_time else ""
            priority_str = f" - Priority: {task.priority}"
            self.task_listbox.insert(tk.END, f"{status} {task.name}{due_date_str}{estimated_time_str}{priority_str}")


def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()