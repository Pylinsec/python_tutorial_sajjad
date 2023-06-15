from tkinter import *

win = Tk()
win.geometry('800x600')
win.title('entry')
win.config(bg='aqua')


# functions
def chap():
    
    if entry.get() == '':
        print('sajjad')
        lbl_chap.config(text='dakkhel entry hichi nist',fg='red')
    else:

        str1 = entry.get() # gereftan harch dakhel entry bood
        lbl_chap.config(text=str1,fg='green')
        entry.delete(0,END)



#  sakhtan entry
# *******
'''
state --> normal , disabled , readonly
show("*") --> hengam neveshtan bejaye character ha * mizare
entry.insert(index,'string') --> dar jayegah indes string bezar
entry.delete(start index , end index)
entry.get()

'''
# *******
username = Label(win,text="username-->: ",font=5,bg='aqua')
username.grid(row=0,column=0,padx=20)
entry = Entry(win,width=40,font=5,bg='lightblue')
entry.grid(row=0,column=1,pady=40,ipady=10)

# sakhtan label beraye chap
lbl_chap = Label(win,bg='white',width=60)
lbl_chap.grid(row=2,column=1 , pady=20)

# sakhtan btn beraye chp har chi dakhel entry bood 
btn = Button(win , text="chap koon",bg='lightgreen')
btn.grid(row=1,column=1)

# conngfig
btn.config(command=lambda:chap())

# yadavari
# num = int(input("insert number: ")
# print(num ** 2)

win.mainloop()