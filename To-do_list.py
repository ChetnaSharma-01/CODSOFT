import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("📝To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f8ff")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text=" My To-Do List", font=("Elephant", 18,), bg="#f0f8ff")
        title.pack(pady=10)

        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14), width=25)
        self.task_entry.pack(pady=10)

        add_btn = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#90ee90", font=("Helvetica", 12))
        add_btn.pack(pady=5)

        self.listbox = tk.Listbox(self.root, font=("Helvetica", 12), width=30, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        done_btn = tk.Button(self.root, text="Mark as Done ✅", command=self.mark_done, bg="#add8e6", font=("Helvetica", 12))
        done_btn.pack(pady=5)

        delete_btn = tk.Button(self.root, text="Delete Task 🗑️", command=self.delete_task, bg="#ff7f7f", font=("Helvetica", 12))
        delete_btn.pack(pady=5)

        clear_btn = tk.Button(self.root, text="Clear All", command=self.clear_tasks, bg="#ffa500", font=("Helvetica", 12))
        clear_btn.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to delete.")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            if not task.endswith(" ✅"):
                self.tasks[index] = task + " ✅"
                self.update_listbox()
        else:
            messagebox.showinfo("Info", "Please select a task to mark as done.")

    def clear_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
