from tkinter import * 

root = Tk()
root.geometry('500x500')

#  make label 
f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()
f3 = Frame(root)
f3.pack()
red= Label(f1,text='RED:')
red.pack(pady=30, side='left',anchor='nw')
red_label = Label(f1,bg='red',width=40)
red_label.pack(pady =30,anchor='nw')


blue= Label(f2,text='BLUE:')
blue.pack(pady=30,side='left',anchor='nw')
blue_label = Label(f2,bg='blue',width=40)
blue_label.pack(pady =30,anchor='nw')

black= Label(f3,text='BLACK:')
black.pack(pady=30 , side='left',anchor='nw')
black_label = Label(f3,bg='black',width=40)
black_label.pack(pady = 30,anchor='nw')
# 
# yellow= Label(root,text='yellow:')
# yellow.pack(pady=30 , side='left',anchor='nw')
# yellow_label = Label(root,bg='yellow',width=40)
# yellow_label.pack(pady = 30,side='left',anchor='n')
# 
# green= Label(root,text='green:')
# green.pack(pady=30 , side='left',anchor='nw')
# green_label = Label(root,bg='green',width=40)
# green_label.pack(pady = 30,side='left',anchor='n')

root.mainloop()