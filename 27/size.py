from tkinter import *

#  format dadan font , name font--> font = ('name font',size)
win = Tk()
win.geometry('600x600')
lbl = Label(win,text='sajjad ansaryan',bg='blue',fg='white',font=('Roman',103))
lbl.pack()
print(lbl['font'])
# print(lbl['text'])
win.mainloop()