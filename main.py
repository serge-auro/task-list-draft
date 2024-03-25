import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_list_box.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def del_task():
    selected_index = task_list_box.curselection()
    if selected_index:
        task_list_box.delete(selected_index)

def complete_task():
    selected_index = task_list_box.curselection()
    if selected_index:
        task_list_box.itemconfig(selected_index, bg="yellow green")
        #text = task_list_box.get(selected_index)
        #task_list_box.delete(selected_index)
        #task_list_box.insert(selected_index, f"✅{text}✅")
        task_list_box.selection_clear(0, tk.END)


root = tk.Tk()
root.title('Task List Draft')
root.config(bg='CadetBlue4')

text1 = tk.Label(root, text="Enter your task here:", bg='CadetBlue4')
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg='CadetBlue', fg='grey6')
task_entry.pack(pady=10, padx=10)

add_task_button = tk.Button(root, text="Add a task", command=add_task)
add_task_button.pack(pady=5)

del_task_button = tk.Button(root, text="Delete a task", command=del_task)
del_task_button.pack(pady=5)

mark_task_button = tk.Button(root, text="Complete a task", command=complete_task)
mark_task_button.pack(pady=5)

text2 = tk.Label(root, text="list of tasks:", bg='CadetBlue4')
text2.pack(pady=5)

task_list_box = tk.Listbox(root, height=10, width=50, bg='CadetBlue4')
task_list_box.pack(pady=10, padx=10)

root.mainloop()
