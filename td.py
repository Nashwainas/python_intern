import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 14))
entry.pack(side=tk.LEFT)

add_button = tk.Button(frame, text="Add Task", font=("Helvetica", 12), command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=delete_task)
delete_button.pack(pady=10)

listbox = tk.Listbox(root, font=("Helvetica", 12), selectmode=tk.SINGLE, width=40, height=10)
listbox.pack()

root.mainloop()
