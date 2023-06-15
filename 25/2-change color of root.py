from tkinter import *
import time 
win = Tk()
win.title("ordak")
colors = ['red','blue','pink','black','yellow','green','brown','purple','aqua','orange']
while 1:
    for color in colors:
        time.sleep(.5)
        win.title(color)
        win.config(bg=color)
        win.update() # jehat update panjerah 
        time.sleep(2)
        win.destroy()
win.mainloop()