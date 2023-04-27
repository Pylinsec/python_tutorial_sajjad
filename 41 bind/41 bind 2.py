from tkinter import *
win = Tk()
win.geometry('600x500')

#   taghiir rang paszamineh ba feshar dadan kelid y -- > yellow 
#  b --> blue  , r --> red , g --> green 

# solution 1
def change_color(e):
    print(e)
    if e.char == 'g':
        win.config(bg='green')
    if e.char == 'r':
        win.config(bg='red')
    if e.char == 'y':
        win.config(bg='yellow')
    if e.char == 'b':
        win.config(bg='blue')


# win.bind('<a>',lambda event:change_color(event))    

# solution 2
win.bind('<g>',lambda event:win.config(bg='green'))    
win.bind('<b>',lambda event:win.config(bg='blue'))    
win.bind('<y>',lambda event:win.config(bg='yellow'))    
win.bind('<r>',lambda event:win.config(bg='red'))    

win.mainloop()