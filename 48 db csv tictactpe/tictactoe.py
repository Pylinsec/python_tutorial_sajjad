from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('320x320')
root.config(bg='black')
root.title('tictactoe')
bool_var = BooleanVar()
bool_var.set(True)
global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9
def disabled_btn():
    btn1.config(state='disabled')
    btn2.config(state='disabled')
    btn3.config(state='disabled')
    btn4.config(state='disabled')
    btn5.config(state='disabled')
    btn6.config(state='disabled')
    btn7.config(state='disabled')
    btn8.config(state='disabled')
    btn9.config(state='disabled')

def win_x():
    # check 123 for x
    if btn1['text'] == 'x' and btn2['text'] == 'x' and btn3['text'] == 'x':
        btn1.config(bg='red')
        btn2.config(bg='red')
        btn3.config(bg='red')
        messagebox.showinfo(title='tictactoe',message='user x win!!!!')
        disabled_btn()
    # check 456 for x
    elif btn4['text'] == 'x' and btn5['text'] == 'x' and btn6['text'] == 'x':
        btn4.config(bg='red')
        btn5.config(bg='red')
        btn6.config(bg='red')
        messagebox.showinfo(title='tictactoe',message='user x win!!!!')
        disabled_btn()
    # check 789 for x
    elif btn7['text'] == 'x' and btn8['text'] == 'x' and btn9['text'] == 'x':
        btn7.config(bg='red')
        btn8.config(bg='red')
        btn9.config(bg='red')
        messagebox.showinfo(title='tictactoe',message='user x win!!!!')
        disabled_btn()
    # check 147 for x
    elif btn1['text'] == 'x' and btn4['text'] == 'x' and btn7['text'] == 'x':
        btn1.config(bg='red')
        btn4.config(bg='red')
        btn7.config(bg='red')
        messagebox.showinfo(title='tictactoe',message='user x win!!!!')
        disabled_btn()
    # check 258 for x
    elif btn2['text'] == 'x' and btn5['text'] == 'x' and btn8['text'] == 'x':
        btn2.config(bg='red')
        btn5.config(bg='red')
        btn8.config(bg='red')
        messagebox.showinfo(title='tictactoe',message='user x win!!!!')
        disabled_btn()
    # check 369 for x
    elif btn3['text'] == 'x' and btn6['text'] == 'x' and btn9['text'] == 'x':
        btn3.config(bg='red')
        btn6.config(bg='red')
        btn9.config(bg='red')
        messagebox.showinfo(title='tictactoe',message='user x win!!!!')
        disabled_btn()
    # check 159 for x
    elif btn1['text'] == 'x' and btn5['text'] == 'x' and btn9['text'] == 'x':
        btn1.config(bg='red')
        btn5.config(bg='red')
        btn9.config(bg='red')
        messagebox.showinfo(title='tictactoe',message='user x win!!!!')
        disabled_btn()
    # check 357 for x
    elif btn3['text'] == 'x' and btn5['text'] == 'x' and btn7['text'] == 'x':
        btn3.config(bg='red')
        btn5.config(bg='red')
        btn7.config(bg='red')
        messagebox.showinfo(title='tictactoe',message='user x win!!!!')
        disabled_btn()



def win_o():
    # check 123 for x
    if btn1['text'] == 'o' and btn2['text'] == 'o' and btn3['text'] == 'o':
        btn1.config(bg='blue')
        btn2.config(bg='blue')
        btn3.config(bg='blue')
        messagebox.showinfo(title='tictactoe',message='user o win!!!!')
        disabled_btn()
    # check 456 for x
    elif btn4['text'] == 'o' and btn5['text'] == 'o' and btn6['text'] == 'o':
        btn4.config(bg='blue')
        btn5.config(bg='blue')
        btn6.config(bg='blue')
        messagebox.showinfo(title='tictactoe',message='user o win!!!!')
        disabled_btn()
    # check 789 for x
    elif btn7['text'] == 'o' and btn8['text'] == 'o' and btn9['text'] == 'o':
        btn7.config(bg='blue')
        btn8.config(bg='blue')
        btn9.config(bg='blue')
        messagebox.showinfo(title='tictactoe',message='user o win!!!!')
        disabled_btn()
    # check 147 for x
    elif btn1['text'] == 'o' and btn4['text'] == 'o' and btn7['text'] == 'o':
        btn1.config(bg='blue')
        btn4.config(bg='blue')
        btn7.config(bg='blue')
        messagebox.showinfo(title='tictactoe',message='user o win!!!!')
        disabled_btn()
    # check 258 for x
    elif btn2['text'] == 'o' and btn5['text'] == 'o' and btn8['text'] == 'o':
        btn2.config(bg='blue')
        btn5.config(bg='blue')
        btn8.config(bg='blue')
        messagebox.showinfo(title='tictactoe',message='user o win!!!!')
        disabled_btn()
    # check 369 for x
    elif btn3['text'] == 'o' and btn6['text'] == 'o' and btn9['text'] == 'o':
        btn3.config(bg='blue')
        btn6.config(bg='blue')
        btn9.config(bg='blue')
        messagebox.showinfo(title='tictactoe',message='user o win!!!!')
        disabled_btn()
    # check 159 for x
    elif btn1['text'] == 'o' and btn5['text'] == 'o' and btn9['text'] == 'o':
        btn1.config(bg='blue')
        btn5.config(bg='blue')
        btn9.config(bg='blue')
        messagebox.showinfo(title='tictactoe',message='user o win!!!!')
        disabled_btn()
    # check 357 for x
    elif btn3['text'] == 'o' and btn5['text'] == 'o' and btn7['text'] == 'o':
        btn3.config(bg='blue')
        btn5.config(bg='blue')
        btn7.config(bg='blue')
        messagebox.showinfo(title='tictactoe',message='user O win!!!!')
        disabled_btn()





# tabe berya click
def change_text(btn):
    if bool_var.get():
        btn.config(text='x')
        bool_var.set(False)
        win_x()
        

    else:
        btn.config(text='o')
        bool_var.set(True)
        win_o()



def make_btn():
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9
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

# meke menu
menu_bar = Menu(root)
root.config(menu=menu_bar)
# make file menu
menu_file = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=menu_file)
menu_file.add_command(label='Reset',command=lambda:make_btn())
# help menu
help_menu = Menu(menu_bar)
menu_bar.add_cascade(label='Help',menu =help_menu)

# sajjad menu for learning
sajjad_menu = Menu(help_menu)
help_menu.add_cascade(label='sajjad',menu=sajjad_menu)

make_btn()
root.mainloop()
