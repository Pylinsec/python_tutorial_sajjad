from tkinter import *
from tkinter import filedialog, messagebox
import os


root = Tk()
root.title('MP3Player')
root.geometry('600x600') # x ---> harf englisi ix
root.config(bg='dimgray')


# function 
def add_one_song():
    song = filedialog.askopenfilename(initialdir='assets/image',title='add one song')
    basename = os.path.basename(song)
    list_song.insert(END,basename[:-4])

def add_more_songs():
    songs = filedialog.askopenfilenames(initialdir='assets/image',title='add one song')
    for song in songs:
        basename = os.path.basename(song)
        list_song.insert(END,basename[:-4])




# frame top
frame_top = Frame(root,width=500,height=350,bg='lightgreen')
frame_top.pack(side=TOP,pady=10)
# fram midle
frame_mid = Frame(root,width=500,height=150,bg='dimgray',relief=GROOVE,border=10)
frame_mid.pack(side=TOP)

# create image for button
play_img = PhotoImage(file='assets/image/play.png')
stop_img = PhotoImage(file='assets/image/stop.png')
pause_img = PhotoImage(file='assets/image/pause.png')
forward_img = PhotoImage(file='assets/image/forward.png')
back_img = PhotoImage(file='assets/image/back.png')

# make button control for mp3player
back_btn = Button(frame_mid,image=back_img)
back_btn.grid(row=0,column=0)
stop_btn = Button(frame_mid,image=stop_img)
stop_btn.grid(row=0,column=1,padx=30)
play_btn = Button(frame_mid,image=play_img)
play_btn.grid(row=0,column=2)
pause_btn = Button(frame_mid,image=pause_img)
pause_btn.grid(row=0,column=3,padx=30)
next_btn = Button(frame_mid,image=forward_img)
next_btn.grid(row=0,column=4)

# make menu
main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu,tearoff=0)
help_menu = Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Help',menu=help_menu)

file_menu.add_command(label='Open song',command= add_one_song)
file_menu.add_command(label='Open songs',command=add_more_songs)



list_song = Listbox(frame_top,bg='aqua',width=90,height=20,relief=GROOVE,border=5,font=5)
list_song.pack()



play_btn.config(command=lambda:print(list_song.selection_get()))
root.mainloop()