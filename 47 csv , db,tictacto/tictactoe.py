from tkinter import *

root = Tk()
root.geometry('320x320')
root.config(bg='black')
root.title('tictactoe')
bool_var = BooleanVar()
bool_var.set(True)


def result_x():
    pass
def result_o():
    pass
# tabe berya click
def change_text(btn):
    if bool_var.get():
        btn.config(text='x',bg='red')
        bool_var.set(False)
    else:
        btn.config(text='o',bg='blue')
        bool_var.set(True)





# btn 1,2,3
btn1 = Button(root,text='',width=10,height=5,bd=1,relief=GROOVE,bg='lightgreen')
btn1.grid(row=0,column=0,padx=10,pady=10)
btn2 = Button(root,text='',width=10,height=5,bd=1,relief=GROOVE,bg='lightgreen')
btn2.grid(row=0,column=1,padx=10,pady=10)
btn3 = Button(root,text='',width=10,height=5,bd=1,relief=GROOVE,bg='lightgreen')
btn3.grid(row=0,column=2,padx=10,pady=10)

# btn 4,5,6
btn4 = Button(root,text='',width=10,height=5,bd=1,relief=GROOVE,bg='lightgreen')
btn4.grid(row=1,column=0,padx=10,pady=10)
btn5 = Button(root,text='',width=10,height=5,bd=1,relief=GROOVE,bg='lightgreen')
btn5.grid(row=1,column=1,padx=10,pady=10)
btn6 = Button(root,text='',width=10,height=5,bd=1,relief=GROOVE,bg='lightgreen')
btn6.grid(row=1,column=2,padx=10,pady=10)

# btn 7,8,9
btn7 = Button(root,text='',width=10,height=5,bd=1,relief=GROOVE,bg='lightgreen')
btn7.grid(row=2,column=0,padx=10,pady=10)
btn8 = Button(root,text='',width=10,height=5,bd=1,relief=GROOVE,bg='lightgreen')
btn8.grid(row=2,column=1,padx=10,pady=10)
btn9 = Button(root,text='',width=10,height=5,bd=1,relief=GROOVE,bg='lightgreen')
btn9.grid(row=2,column=2,padx=10,pady=10)

# change config for btn
btn1.config(command=lambda:change_text(btn1))
btn2.config(command=lambda:change_text(btn2))
btn3.config(command=lambda:change_text(btn3))

btn4.config(command=lambda:change_text(btn4))
btn5.config(command=lambda:change_text(btn5))
btn6.config(command=lambda:change_text(btn6))

btn7.config(command=lambda:change_text(btn7))
btn8.config(command=lambda:change_text(btn8))
btn9.config(command=lambda:change_text(btn9))

for i in root.winfo_children():
    print(i.grid_forget())
root.mainloop()
