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
    else:
        selected_index = in_progress_list_box.curselection()
        if selected_index:
            in_progress_list_box.delete(selected_index)
        else:
            selected_index = completed_list_box.curselection()
            if selected_index:
                completed_list_box.delete(selected_index)

def move_to_in_progress():
    selected_index = task_list_box.curselection()
    if selected_index:
        task = task_list_box.get(selected_index)
        task_list_box.delete(selected_index)
        in_progress_list_box.insert(tk.END, task)

def move_to_completed():
    selected_index = in_progress_list_box.curselection()
    if selected_index:
        task = in_progress_list_box.get(selected_index)
        in_progress_list_box.delete(selected_index)
        completed_list_box.insert(tk.END, task)

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

move_to_in_progress_button = tk.Button(root, text="Move to In Progress", command=move_to_in_progress)
move_to_in_progress_button.pack(pady=5)

move_to_completed_button = tk.Button(root, text="Move to Completed", command=move_to_completed)
move_to_completed_button.pack(pady=5)

text2 = tk.Label(root, text="Backlog:", bg='CadetBlue4')
text2.pack(pady=5)

task_list_box = tk.Listbox(root, height=5, width=50, bg='CadetBlue4')
task_list_box.pack(pady=10, padx=10)

text2 = tk.Label(root, text="IN PROGRESS:", bg='CadetBlue4')
text2.pack(pady=5)

in_progress_list_box = tk.Listbox(root, height=5, width=50, bg='light yellow')
in_progress_list_box.pack(pady=10, padx=10)

text2 = tk.Label(root, text="DONE:", bg='CadetBlue4')
text2.pack(pady=5)

completed_list_box = tk.Listbox(root, height=5, width=50, bg='pale green')
completed_list_box.pack(pady=10, padx=10)

#test comment

root.mainloop()
