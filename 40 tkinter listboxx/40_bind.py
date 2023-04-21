#  bind in tkiner   --> format --> widget.bind('<>',handeler(heman funtion))

from tkinter import *

win = Tk()
# Key , KeyPress --> har kelidi ke feshorde shevad feghat keybord
# KeyRelease  --> har kelidi ke reha shevad asar mikonad feghat keyboard
#har name dokmei
# Motion --> harkat mouse 
# Button --> heman kelid haye rooye mouse --> lclick --> 1 , micleclick --> 2 , rclick --> 3 
# ButtonRelease --> vaghti kelid mouse reha shod asar nema 

def chap(e):
    print(e)
    # keysym=e keycode=69 char='e' x=198 y=754
    print(e.keysym) #--> name character be ma mide 
    print(e.keycode) # heman code ascii
    print(e.char) # khode character neshan mide


win.bind('<KeyPress>',lambda event:chap(event))

win.mainloop()