from tkinter import *

win = Tk()
win.geometry('800x600')
win.title('grid')
win.config(bg='aqua')
#  make label 
#  row0
btn1 = Button(text='00 ',font=3,bg="yellow", border=2,width=20)
btn1.grid(row=0,column=0,pady=3,padx=3)
btn2 = Button(text='01',bg="yellow",font=3, border=2,width=20)
btn2.grid(row=0,column=1,pady=3,padx=3)
btn3 = Button(text='02',font=3,bg="yellow", border=2,width=20)
btn3.grid(row=0,column=2,pady=3,padx=3)
btn3 = Button(text='03',font=3,bg="yellow", border=2,width=20)
btn3.grid(row=0,column=3,pady=3,padx=3)
# row1
btn4 = Button(text='10',font=3,bg="yellow", border=2,width=20)
btn4.grid(row=1,column=0,pady=3)
btn5 = Button(text='11,12 ',font=3,bg="yellow", border=2,width=40)
btn5.grid(row=1,column=1,columnspan=2,pady=3) # tedad sooton ekhtesasi 
btn6 = Button(text='13 ',font=3,bg="yellow", border=2,width=20)
btn6.grid(row=1,rowspan=3,column=3,pady=3,ipady=20)

# row2
btn4 = Button(text='20',font=3,bg="yellow", border=2,width=20)
btn4.grid(row=2,column=0,pady=3)
btn5 = Button(text='21',font=3,bg="yellow", border=2,width=20)
btn5.grid(row=2,column=1,pady=3)
btn6 = Button(text='22',font=3,bg="yellow", border=2,width=20)
btn6.grid(row=2,column=2,pady=3)
# btn6 = Button(text='23',font=3,bg="yellow", border=2,width=20)
# btn6.grid(row=2,column=3,pady=3)

# for i in range(5):
#     for j in range(5):
#         lbl1 = Label(text='username: ',font=3,bg="yellow", border=2)
#         lbl1.grid(row=i,column=j,padx=30,pady=30)
# lbl1.pack(pady=30,side=LEFT)
# lbl2 = Label(text='username: ',font=3,bg='green')
# lbl2.grid(row=10,column=10)
# lbl2.pack(pady=30,side='right',anchor=CENTER)





win.mainloop()