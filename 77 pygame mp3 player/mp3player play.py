from tkinter import *
from tkinter import filedialog, messagebox
import os , pygame , time


root = Tk()
root.title('MP3Player')
root.geometry('600x600') # x ---> harf englisi ix
root.config(bg='dimgray')
pygame.init()
# berye mesir
path_dirname = StringVar()
is_pause = BooleanVar()
is_pause.set(False)

# function for calculate time
def timer():
    song_len_time = pygame.mixer.music.get_pos() // 1000   
    time_gm = time.gmtime(song_len_time)
    time_struc = time.strftime('%H:%M:%S',time_gm)
    lbl_status.config(text=time_struc)
    lbl_status.after(1000,timer)
    root.update()
    

# function 
def add_one_song():
    list_song.delete(0,END)
    global path_dirname
    song = filedialog.askopenfilename(initialdir='assets/songs',title='add one song')
    basename = os.path.basename(song)
    path_dirname.set(os.path.dirname(song))
    list_song.insert(END,basename[:-4])
    # list_song.activate(0)
    list_song.selection_set(0)
    list_song.focus()
    back_btn.config(state='disabled')
    next_btn.config(state='disabled')

def add_more_songs():
    list_song.delete(0,END)
    back_btn.config(state='disabled')
    songs = filedialog.askopenfilenames(initialdir='assets/songs',title='add one song')
    for song in songs:
        basename = os.path.basename(song)
        path_dirname.set(os.path.dirname(song))
        list_song.insert(END,basename[:-4])
        list_song.selection_set(0)
        list_song.focus()
        back_btn.config(state='disabled')


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
    timer()    


# make function for next btn 
def next():
    back_btn.config(state='normal')
    current = list_song.curselection()[0] # tuyple barmigardand 
    if current + 1 == list_song.size() -1:
        # print(current,list_song.size())
        next_btn.config(state='disabled')
    else:
        pass  

    if current in range (0,list_song.size()-1):
        current += 1
        song = list_song.get(current)
        # print(f"current-->{current},song--> {song}")
        list_song.selection_clear(0,END)
        list_song.selection_set(current)
        list_song.activate(current)
        main_path = f"{path_dirname.get()}/{list_song.selection_get()}.mp3"
        pygame.mixer.music.load(main_path)
        pygame.mixer.music.play()
        

    else:
        pass  


def back():
    next_btn.config(state='normal')
    current = list_song.curselection()[0] # tuyple barmigardand 
    if current -1 == 0:
        # print(current,list_song.size())
        back_btn.config(state='disabled')
    else:
        pass  

    if current in range (1,list_song.size()):
        current -= 1
        song = list_song.get(current)
        # print(f"current-->{current},song--> {song}")
        list_song.selection_clear(0,END)
        list_song.selection_set(current)
        list_song.activate(current)
        main_path = f"{path_dirname.get()}/{list_song.selection_get()}.mp3"
        pygame.mixer.music.load(main_path)
        pygame.mixer.music.play()
        

    else:
        pass    
    

def delete_one_song():
    # first way
    song_index = list_song.curselection()[0]
    # song_name = list_song.selection_get()
    # print(song_name)
    # list_song.delete(song_index)

    # second way 
    list_song.delete(ANCHOR)


def delete_all_song():
    pygame.mixer.music.stop()
    list_song.delete(0,END)   



# frame top
frame_top = Frame(root,width=500,height=350,bg='lightgreen')
frame_top.pack(side=TOP,pady=10)
# fram midle
frame_mid = Frame(root,width=500,height=150,bg='dimgray',relief=GROOVE,border=10)
frame_mid.pack(side=BOTTOM)

frame_mid_top = Frame(frame_mid,width=500,height=100,bg='dimgray',relief=GROOVE,border=10)
frame_mid_top.pack(side=TOP)

frame_mid_bot = Frame(frame_mid,width=500,height=50,bg='aqua')
frame_mid_bot.pack(side=BOTTOM,anchor='e')

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
edit_menu = Menu(main_menu,tearoff=0)
help_menu = Menu(main_menu,tearoff=0)

main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='Help',menu=help_menu)

# file menu commands
file_menu.add_command(label='Open song',command= add_one_song)
file_menu.add_command(label='Open songs',command=add_more_songs)

# edit menu commands
edit_menu.add_command(label='Delete one song',command=lambda:delete_one_song())
edit_menu.add_command(label='Delete all songs',command=lambda:delete_all_song())


list_song = Listbox(frame_top,bg='aqua',width=90,height=20,relief=GROOVE,border=5,font=5)
list_song.pack()

# make label for status
lbl_status = Label(frame_mid_bot,text='00:00:00',font=5,fg='red')
lbl_status.pack(side='right')

# run btn function
play_btn.config(command=lambda:play())
next_btn.config(command=lambda:next())
back_btn.config(command=lambda:back())

root.mainloop()