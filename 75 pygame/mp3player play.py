from tkinter import *
from tkinter import filedialog, messagebox
import os , pygame


root = Tk()
root.title('MP3Player')
root.geometry('600x600') # x ---> harf englisi ix
root.config(bg='dimgray')
pygame.init()
# berye mesir
path_dirname = StringVar()
is_pause = BooleanVar()
is_pause.set(False)

# function 
def add_one_song():
    global path_dirname
    song = filedialog.askopenfilename(initialdir='assets/songs',title='add one song')
    basename = os.path.basename(song)
    path_dirname.set(os.path.dirname(song))
    list_song.insert(END,basename[:-4])
    # list_song.activate(0)
    list_song.selection_set(0)
    list_song.focus()

def add_more_songs():
    songs = filedialog.askopenfilenames(initialdir='assets/songs',title='add one song')
    for song in songs:
        basename = os.path.basename(song)
        path_dirname.set(os.path.dirname(song))
        list_song.insert(END,basename[:-4])
        list_song.selection_set(0)
        list_song.focus()


def play():
    index = list_song.size()
    if not is_pause.get() and index > 0:
        main_path = f"{path_dirname.get()}/{list_song.selection_get()}.mp3"
        print(main_path)
        pygame.mixer.music.load(main_path)
        pygame.mixer.music.play()
        is_pause.set(True)
        play_btn.config(image=pause_img)
    else:
        pygame.mixer.music.pause()
        play_btn.config(image=play_img)
        is_pause.set(False)



# frame top
frame_top = Frame(root,width=500,height=350,bg='lightgreen')
frame_top.pack(side=TOP,pady=10)
# fram midle
frame_mid = Frame(root,width=500,height=150,bg='dimgray',relief=GROOVE,border=10)
frame_mid.pack(side=BOTTOM)

frame_mid_top = Frame(frame_mid,width=500,height=100,bg='dimgray',relief=GROOVE,border=10)
frame_mid_top.pack(side=TOP)
frame_mid_bot = Frame(frame_mid,width=500,height=50,bg='dimgray',relief=GROOVE,border=10)
frame_mid_bot.pack(side=BOTTOM)

# create image for button
play_img = PhotoImage(file='assets/image/play.png')
stop_img = PhotoImage(file='assets/image/stop.png')
pause_img = PhotoImage(file='assets/image/pause.png')
forward_img = PhotoImage(file='assets/image/forward.png')
back_img = PhotoImage(file='assets/image/back.png')

# make button control for mp3player
back_btn = Button(frame_mid_top,image=back_img)
back_btn.grid(row=0,column=0)
stop_btn = Button(frame_mid_top,image=stop_img)
stop_btn.grid(row=0,column=1,padx=30)
play_btn = Button(frame_mid_top,image=play_img)
play_btn.grid(row=0,column=2)
pause_btn = Button(frame_mid_top,image=pause_img)
pause_btn.grid(row=0,column=3,padx=30)
next_btn = Button(frame_mid_top,image=forward_img)
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


# run btn function
play_btn.config(command=lambda:play())
# pause_btn.config(command=lambda:pause())
root.mainloop()