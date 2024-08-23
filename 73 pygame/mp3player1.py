from tkinter import *

# make root
window = Tk()
# dadan name be panjereh
window.title('Mp3Player')
# change size
window.geometry("600x500")

# make frame 
frame_listbox = Frame(window,bg='red',width=560,height=300)
frame_listbox.pack(pady=20)
frame_button = Frame(window,bg='lightgreen',width=560,height=100)
frame_button.pack()
frame_status = Frame(window,bg='gray',width=560,height=50)
frame_status.pack(pady=10)

# create image for button
play_img = PhotoImage(file='assets/image/play.png')
stop_img = PhotoImage(file='assets/image/stop.png')
pause_img = PhotoImage(file='assets/image/pause.png')
forward_img = PhotoImage(file='assets/image/forward.png')
back_img = PhotoImage(file='assets/image/back.png')

# make button control for mp3player
back_btn = Button(frame_button,image=back_img)
back_btn.grid(row=0,column=0)
back_stop = Button(frame_button,image=stop_img)
back_stop.grid(row=0,column=1,padx=30)
back_play = Button(frame_button,image=play_img)
back_play.grid(row=0,column=2)
back_pause = Button(frame_button,image=pause_img)
back_pause.grid(row=0,column=3,padx=30)
back_forward = Button(frame_button,image=forward_img)
back_forward.grid(row=0,column=4)



window.mainloop()