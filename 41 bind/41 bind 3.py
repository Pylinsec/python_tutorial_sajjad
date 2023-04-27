from tkinter import *
win = Tk()
win.geometry('600x500')

win.bind('<Button>',lambda event: print(event.num))
# win.bind('<ButtonRelease>',lambda event: print(event.num))

#  left click --> bg = black
# solution 1
def change_color(e):
    if e.num == 1:
        win.config(bg='black')

win.bind('<Button>',lambda event: win.config(bg='black'))
#  solution 2
# win.bind('<Button-1>',lambda event: win.config(bg='black'))
win.mainloop()