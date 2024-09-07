from tkinter import *
from tkinter import filedialog , messagebox
import os


root = Tk()
root.title('MP3Player')
root.geometry('600x600') # x ---> harf englisi ix
root.config(bg='dimgray')

# frame top
frame_top = Frame(root,width=500,height=350,bg='lightgreen')
frame_top.pack(side=TOP,pady=10)




list_song = Listbox(frame_top,bg='aqua',width=90,height=20,relief=GROOVE,border=5,font =5,fg='black')
list_song.pack()
# list_song.insert(END,'sajjad1')
# list_song.insert(END,'sajjad2')
# list_song.insert(END,'sajjad4')
# list_song.insert(END,'sajjad5')
# list_song.insert(2,'ansaryan')



# song = filedialog.askopenfilename(initialdir='assets/image',title='song')  #select tak 
songs = filedialog.askopenfilenames(initialdir='assets/image',title='song') # tedad 
# print(songs)
for song in songs:
    dirname = os.path.dirname(song)
    basename = os.path.basename(song)
    list_song.insert(END,basename[:-4])
root.mainloop()