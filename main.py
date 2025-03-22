import random
import tkinter as tk
from tkinter import filedialog, ttk
import os
from pygame import mixer
import random as rd
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import decimal as ds
"""

font_color = "lime"
bg_color = "black"
btn_text_color = "yellow"
btn_color= "gray"
ent_color = "white"

#print(help(tk.Scale.focus_get))


class Player(tk.Tk):

    def __init__(self):

        mixer.init()

        self.flag=True

        self.num = 0

        self.now=0
        self.raz=0

        self.mus = []
        self.le = 0

        self.diar = '' # Дириктива/Путь к файлу(папке)

        self.c = False # Использую в stop_music, для более плавной остановки

        self.tr = ''# Записываю имя трека для play

        self.a = None
        self.text = []

        #self.fig, self.ax = plt.subplots()

        self.count=0

        super().__init__()

        self.mus_spis = tk.StringVar(value=self.mus)


        self.title("MUSICA")
        self.config(bg=bg_color)

        self.geometry('1200x920')
        self.resizable(True, True)

        self.lbl = tk.Label(self, text='by Terrapod', fg=font_color, bg=bg_color)
        self.lbl.config(underline=2)
        self.lbl.place(relx=0.02, rely=0.99, anchor=tk.W)

        self.lbl_mus = tk.Label(self, text='Треки',fg=font_color, bg=bg_color, font='RussianPunk')
        self.lbl_mus.place(relx=0.2, rely=0.05, anchor=tk.CENTER)

        self.lbl_mus = tk.Label(self, text='Текст', fg=font_color, bg=bg_color, font='RussianPunk')
        self.lbl_mus.place(relx=0.75, rely=0.05, anchor=tk.CENTER)

        self.mspis = tk.Listbox(self, listvariable = tk.StringVar(value=[]), width=68, height=37, bd=16, bg=bg_color, fg=font_color)
        self.mspis.place(relx=0.02, rely=0.42, anchor=tk.W)
        self.mspis.bind('<Double-Button>', self.play)

        self.t = ttk.Scrollbar(self, orient='vertical', command= self.mspis.yview)
        self.t.pack(side=tk.LEFT, fill=tk.Y)
        self.mspis['yscrollcommand'] = self.t.set

        self.dob = tk.Button(self, text='Выбор папки', width=20, height=1, bg=bg_color, fg=font_color)
        self.dob.bind('<Button-1>', self.dobmusic)
        self.dob.place(relx=0.02, rely=0.85, anchor=tk.W)

        self.ubr = tk.Button(self, text='Случайный порядок', width=20, height=1, bg=bg_color, fg=font_color)
        self.ubr.bind('<Button-1>', self.randmus)
        self.ubr.place(relx=0.02, rely=0.9, anchor=tk.W)

        self.stop = tk.Button(self, text='|>|', width=4, height=1, bg=bg_color, fg=font_color, font='bold')
        self.stop.bind('<Button-1>', self.stop_music)
        self.stop.place(relx = 0.7, rely=0.85, anchor = tk.W)

        self.bind('<space>', self.stop_music)
        self.bind('<Return>', self.play)

        self.next = tk.Button(self, text='>>', width=4, height=1, bg=bg_color, fg=font_color, font='bold')
        self.next.bind('<Button-1>', self.next_track)
        self.next.place(relx=0.75, rely=0.85, anchor=tk.W)

        self.per = tk.Button(self, text='<<', width=4, height=1, bg=bg_color, fg=font_color, font='bold')
        self.per.bind('<Button-1>', self.prev_track)
        self.per.place(relx=0.65, rely=0.85, anchor=tk.W)

        self.track = tk.StringVar()
        self.voz_text = tk.Entry(self, textvariable=self.track, fg=font_color, bg=bg_color, width=24, highlightcolor='lime')
        self.voz_text.place(relx=0.388, rely=0.9, anchor=tk.E)

        self.voz = tk.Button(self, text='Возпроизвести трек', width=20, height=1, bg=bg_color, fg=font_color)
        self.voz.bind('<Button-1>', self.play)
        self.voz.place(relx=0.388, rely=0.85, anchor=tk.E)

        self.scale = tk.Scale(self, from_=0, to=100, orient="horizontal", length=500, width=10, bg=bg_color, fg=font_color, border=2, troughcolor=bg_color, command=self.on_mus)
        self.scale.config(showvalue=0, highlightbackground='DarkGrey', activebackground=font_color)
        self.scale.place(relx=0.5125, rely=0.9, anchor = tk.W)

        self.line = tk.Text(self, bg=bg_color, fg=font_color, width=68, height=37, bd=16, wrap='word', )
        self.line.place(relx=0.5, rely=0.42, anchor=tk.W)

        self.sc = ttk.Scrollbar(orient='vertical', command = self.line.yview)
        self.sc.pack(side=tk.RIGHT, fill=tk.Y)
        self.line['yscrollcommand'] = self.sc.set

        self.chec_end()

        self.mainloop()


    def play(self, event):
        self.a = mixer.Sound(self.diar + '\\' + self.mspis.selection_get() + '.mp3')
        mixer.music.load(self.diar +'\\'+ self.mspis.selection_get() +'.mp3')
        mixer.music.play()
        self.line.delete('1.0', tk.END)
        if self.mspis.selection_get()+'.txt' in self.text:
            f = open(self.diar + '\\' + self.mspis.selection_get() + '.txt', encoding="utf-8")
            d = [i for i in f]
            s = '***'+self.mspis.selection_get()+'***'+'\n'*2
            for i in d:
                s+= i + '\n'
            self.line.insert('1.0', s)
        else:
            self.line.insert('1.0', 'Вывести текст песни можно переместив .txt файл в папку с музыкой')
        self.le = self.a.get_length()
        self.c = False
        self.stop.config(bg=bg_color, fg=font_color)
        self.scale.set(0)
        self.flag=True
        self.num = self.mspis.curselection()[0]

    def stop_music(self, event):
        if self.c:
            self.flag = True
            mixer.music.unpause()
            self.c = False
            self.stop.config(bg=bg_color, fg=font_color)
        else:
            self.flag = False
            mixer.music.pause()
            self.c = True
            self.stop.config(bg=btn_color, fg='black')

    def on_mus(self, event):
        #print(type(type(self.a)))
        self.now=self.scale.get()/100*self.le
        mixer.music.set_pos(self.now)
        #print(bool(self.scale.winfo_ismapped()))
        #self.scale.winfo_pointerxy()
        #self.mspis.focus_set()

    def next_track(self, event):
        #Эта чернь была сделана только при помощи святого gpt
        #Слава GPT, GPT слава!!!
        #Код, выданый gpt, в файле testo.py
        self.flag=False
        next_index = (self.num + 1)%self.mspis.size()
        self.mspis.selection_clear(0,tk.END)
        self.mspis.selection_set(next_index)
        self.scale.set(0)
        self.play(None)

    def prev_track(self, event):
        self.flag=False
        next_index = (self.num - 1) % self.mspis.size()
        self.mspis.selection_clear(0, tk.END)
        self.mspis.selection_set(next_index)
        self.scale.set(0)
        self.play(None)

    def dobmusic(self, event):
        p = filedialog.askdirectory()
        self.mus = []
        if p:
            self.mspis.delete(0, tk.END)
            self.text.clear()
            self.line.delete('1.0', tk.END)
            self.diar = os.path.abspath(p)
            os.chdir(p)
            songs = os.listdir(p)
            for i in songs:
                if i.endswith('.mp3'):
                    self.mus += [i]
                    self.mspis.insert(tk.END, i[:-4])
                if i.endswith('.txt'):
                    self.text.insert(-1, i)
            for i in self.text:
                self.line.insert(tk.END, i[:-4])
            self.voz_text.delete(0, tk.END)
            self.voz_text.insert(0, self.diar)


    def randmus(self, event):
        d = [i for i in self.mspis.get(0, tk.END)]
        self.mspis.delete(0, tk.END)
        self.mus = []
        rd.shuffle(d)
        for i in d:
            self.mus+= [i]
            self.mspis.insert(tk.END, i)
        self.mspis.selection_set(0)


    def chec_end(self):
        if mixer.music.get_busy() == False and self.a and self.flag:
            self.num = self.mspis.curselection()[0]
            self.mspis.select_clear(self.num)
            self.mspis.selection_set(self.num+ 1)
            self.play(None)
        self.after(10, self.chec_end)




if __name__ == '__main__':
    p = Player()