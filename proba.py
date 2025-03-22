import tkinter as tk
import pygame

def play_music():
    pygame.mixer.music.load("1.mp3") # загрузка музыки
    pygame.mixer.music.play()

def change_position(val):
    pos = int(val) * pygame.mixer.music.get_length() // 1000
    pygame.mixer.music.set_pos(pos)

def update_slider():
    pos = pygame.mixer.music.get_pos()
    length = pygame.mixer.music.get_length()
    val = pos * 1000 // length
    scale.set(val)
    root.after(100, update_slider)

root = tk.Tk()
root.title("Music Player")

pygame.mixer.init()

play_music()

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=change_position)
scale.pack()

update_slider()

root.mainloop()