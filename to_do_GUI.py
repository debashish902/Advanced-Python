from tkinter import *

# Create window
root = Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="#f0f0f0")

# Functions
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        pass

def clear_tasks():
    listbox.delete(0, END)

# Title
title = Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Entry box
entry = Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Add button
add_btn = Button(root, text="Add Task", width=20, command=add_task, bg="#4CAF50", fg="white")
add_btn.pack(pady=5)

# Listbox
listbox = Listbox(root, width=35, height=12, font=("Arial", 12))
listbox.pack(pady=10)

# Delete button
del_btn = Button(root, text="Delete Task", width=20, command=delete_task, bg="#f44336", fg="white")
del_btn.pack(pady=5)

# Clear button
clear_btn = Button(root, text="Clear All", width=20, command=clear_tasks, bg="#555", fg="white")
clear_btn.pack(pady=5)

# Run app
root.mainloop()