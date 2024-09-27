from tkinter import *
from tkinter import filedialog , messagebox
import os
import pygame

pygame.init()
# path = 'M:\pythonClass\sajad\75 pygame\assets\songs.music 2024-1.mp3'
path2 = 'assets\songs\music 2024-1.mp3'
pygame.mixer.music.load(path2)
pygame.mixer.music.play()








root = Tk()
root.title('MP3Player')
root.geometry('600x600') # x ---> harf englisi ix
root.config(bg='dimgray')

# frame top
frame_top = Frame(root,width=500,height=350,bg='lightgreen')
frame_top.pack(side=TOP,pady=10)

list_song = Listbox(frame_top,bg='aqua',width=90,height=20,relief=GROOVE,border=5,font =5,fg='black')
list_song.pack()

songs = filedialog.askopenfilenames(initialdir='assets/image',title='song') # tedad 
# print(songs)
for song in songs:
    dirname = os.path.dirname(song)
    basename = os.path.basename(song)
    list_song.insert(END,basename[:-4])
root.mainloop()