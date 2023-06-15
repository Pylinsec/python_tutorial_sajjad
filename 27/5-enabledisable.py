from tkinter import *

win = Tk()
win.geometry('400x400')



btn1 = Button(win,text='clickme!',font=5,width=12,height=6,bg='green')
btn1.pack()
btn2 = Button(win,text='clickme!',font=5,width=12,height=6,bg='yellow')
btn2.pack(pady=30)

# define function --> disable button
def enable_disable():
    if btn2['state']=='disabled':
        btn2.config(state='normal',bg='yellow')
        btn2.pack(side='right')
    else:
        btn2.config(state=DISABLED ,bg='black')
        btn2.pack(side='left')

# btn command
btn1.config(command=lambda:enable_disable())    
    

win.mainloop()
