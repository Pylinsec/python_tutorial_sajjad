from tkinter import *

win = Tk()
win.geometry('400x400')
win.config(bg='red')
''' bd , fg , bg , font , height , width , padx , pady , text , config
state  --> normal , disabled , active ,
activebackground --> change range paszamine hengeam raftan mouse rooye an
activeforground  --> change rang font hengam raftan mouse rooye an
command --> function migirad 
'''
btn = Button(win,text='clickme!',font=5,width=12,height=6,bg='green',command=lambda:change_color())
btn.pack()
print(win['bg'])


# define fucntion for change rang paszamineh asli 
def change_color():
    if win['bg'] == 'red':
        win.config(bg='blue')
    else:
        win.config(bg='red')

win.mainloop()
