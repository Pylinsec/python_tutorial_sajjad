from tkinter import *
from tkinter import ttk
import time

win = Tk()
int_var = IntVar()
#  horizontal ---> ofoghi   vertical --> ammodi 
#  maximum --> hadaksar meghdar dakhek progressbar
# length --> andazeh progressbar dar dakhek win
pb = ttk.Progressbar(win,orient=HORIZONTAL,length=400,maximum=200)
pb.pack(ipady=20)
for i in range(1,200):
    int_var.set(i)
    pb.config(variable=int_var)
    
    win.update()
    time.sleep(.2)
    pb.stop()



win.mainloop()