from tkinter import *

root = Tk()
root.title('MP3Player')
root.geometry('600x600') # x ---> harf englisi ix
root.config(bg='dimgray')

# ------------------------------------------------------------------------------------
# frames
# frame top
frame_top = Frame(root,width=500,height=350,bg='lightgreen')
frame_top.pack(side=TOP,pady=10)
# fram midle
frame_mid = Frame(root,width=500,height=150,bg='dimgray',relief=GROOVE,border=10)
frame_mid.pack(side=TOP)
# frame bottom
frame_bottom = Frame(root,width=500,height=50,bg='blue')
frame_bottom.pack(side=BOTTOM)

# ----------------------------------------------------------------------------------------------------------

# photos ----------------------------------------------------------------------------
# create image for button
play_img = PhotoImage(file='assets/image/play.png')
stop_img = PhotoImage(file='assets/image/stop.png')
pause_img = PhotoImage(file='assets/image/pause.png')
forward_img = PhotoImage(file='assets/image/forward.png')
back_img = PhotoImage(file='assets/image/back.png')

# make button control for mp3player
back_btn = Button(frame_mid,image=back_img)
back_btn.grid(row=0,column=0)
back_stop = Button(frame_mid,image=stop_img)
back_stop.grid(row=0,column=1,padx=30)
back_play = Button(frame_mid,image=play_img)
back_play.grid(row=0,column=2)
back_pause = Button(frame_mid,image=pause_img)
back_pause.grid(row=0,column=3,padx=30)
back_forward = Button(frame_mid,image=forward_img)
back_forward.grid(row=0,column=4)
# --------------------------------------------------------------------------------------

"""
# -relief
RAISED='raised'
SUNKEN='sunken'
FLAT='flat'
RIDGE='ridge'
GROOVE='groove'
SOLID = 'solid'
"""

list_song = Listbox(frame_top,bg='aqua',width=90,height=20,relief=GROOVE,border=5)
list_song.pack()

root.mainloop()