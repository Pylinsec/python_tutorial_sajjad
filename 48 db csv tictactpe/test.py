from tkinter import *


win = Tk()
win.geometry('500x500')
win.config(bg='lightgreen')

menu_bar = Menu(win)
win.config(menu=menu_bar)

menu_file = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=menu_file)
menu_file.add_command(label='print',command=lambda:print('sajjad ansaryan'))



help_menu = Menu(menu_bar) # 1 --> sakht menu 
menu_bar.add_cascade(label='Help',menu=help_menu)
menu_file.add_command(label='qoli',command=lambda:print('qoli'))
help_menu.add_command(label='help',command=lambda:print('havij'))

win.mainloop()