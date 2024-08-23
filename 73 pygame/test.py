from tkinter import *

# make root
window = Tk()
# dadan name be panjereh
window.title('Mp3Player')
# change size
window.geometry("600x500")



colors = ('red1','blue2','red3','blue4','red5','blue6','red','blue7','red8','blue9')
# make frame 
frame_up = Frame(window,bg='red',width=560,height=300)
frame_up.grid(column=0,pady=30)
frame_down = Frame(window,bg='blue',width=560,height=100)
frame_down.grid(column=1)

# create image for button
play_img = PhotoImage(file='assets/image/play.png')
listbox = Listbox(frame_up,width=500,height=20)
listbox.grid()
for i in colors:
    listbox.insert(END,i)

listbox.insert(5,'sajjad')
window.mainloop()