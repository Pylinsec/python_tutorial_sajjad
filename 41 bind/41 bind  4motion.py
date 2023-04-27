from tkinter import *
win = Tk()
win.geometry('600x500')

# win.bind('<Motion>',lambda event: print(event))
#  heman harkat mose hast ke x , y barmigardand 
btn = Button(win,text='sajjad',width=20,bg='lightgreen',bd=5)
btn.place(x=100,y=100)

def change_position(e):
    print(e)
    btn.place(x=e.x , y= e.y)
    win.update_idletasks()

btn.bind('<Motion>',lambda event:change_position(event))
# btn.bind('<Button-1>',lambda event:change_position(event))
win.mainloop()