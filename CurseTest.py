import tkinter as tk

def on_scale_move(value):
    print(value)

root = tk.Tk()
root.title("Music Player")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=on_scale_move)
scale.pack()

root.mainloop()
