from tkinter import *

win = Tk()
win.title('sajjad')
win.geometry('500x500')

# variable calass
str_var = StringVar()  # --> az no string 
int_var = IntVar()  # az no adadi 
bool_var = BooleanVar()  # az no 0 ya 1 

# in se ta variable hastan az no heman ke qablan dashtim vali dar qaleb tkinter 

# meqdardadan ba set()
str_var.set('sajjad ansaryan') # ba set() --> meqdar dadan 
print(str_var.get())
int_var.set(2.5)
print(int_var.get())  # daryaft meqdar

entry1 = Entry(win , textvariable=str_var)
entry1.pack()

entry2 = Entry(win , textvariable=str_var)
entry2.pack()
# entry2.insert(0,'sajjad') 

# create btn
# btn = Button(win, text = 'click me ' , command=lambda:print(str_var()))
btn = Button(win, text = 'click me ' , command=lambda:print(entry2.get()))
btn.pack()




win.mainloop()