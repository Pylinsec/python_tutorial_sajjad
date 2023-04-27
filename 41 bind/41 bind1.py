from tkinter import *
win = Tk()
win.geometry('600x500')

# format --> widget.bind('<keyboard ya mouse >',hander(function))
# widget --> label , button , ...
# win.bind("<KeyPress>",lambda event:print(event))


def chap(event):
    print("output: ")
    print(f"name key: {event.keysym}")
    print(f"ascii code: {event.keycode}")
    print(f"key: {event.char}")
    print(f"mouse: x = {event.x} ,y = {event.y}")

win.bind("<KeyPress>",lambda event:chap(event))

# win.bind("<KeyRelease>",lambda event:print(event))
# win.bind("<Key>",lambda event:print(event))
# win.bind("<h>",lambda event:print(event))
# event --> hargone harkat az taraf mouse ya keyboard 
# < keysym=g keycode=71 char='g' x=-400 y=261>

def change_bg():
    pass

# win.bind('<KeyRelease>',change_btg)


win.mainloop()