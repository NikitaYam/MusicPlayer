import tkinter as tk

def underline_selected(event):
    selected_index = listbox.curselection()
    if selected_index:
        item = listbox.get(selected_index)
        listbox.itemconfig(selected_index, selectbackground="white", selectforeground="black")

# создание окна
root = tk.Tk()

# создание listbox
listbox = tk.Listbox(root)
listbox.pack()

# добавление элементов в listbox
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")

# привязка функции к событию выбора элемента в listbox
listbox.bind("<Button-1>", underline_selected)

root.mainloop()