import tkinter as tk

def select_next_item():
    current_index = listbox.curselection()[0]
    next_index = (current_index + 1) % listbox.size()
    listbox.selection_clear(0, tk.END)
    listbox.select_set(next_index)

root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()

for i in range(10):
    listbox.insert(tk.END, f"Item {i}")

select_button = tk.Button(root, text="Select Next Item", command=select_next_item)
select_button.pack()

root.mainloop()