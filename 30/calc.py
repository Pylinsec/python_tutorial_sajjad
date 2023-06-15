from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x600')
        self.config(bg='black')
        self.str_var = StringVar()
        self.create_widget()


    def create_widget(self):
        self.entry = Entry(self,width=40,font=4,textvariable=self.str_var)
        self.entry.insert(END,'sajjad')
        self.entry.insert(END,' ansaryn')
        btn7 = Button(self,text='7',bg='lightyellow',width=10,height=5,command=lambda:self.write('7'))
        btn8 = Button(self,text='8',bg='lightyellow',width=10,height=5,command=lambda:self.write('8'))
        btn9 = Button(self,text='9',bg='lightyellow',width=10,height=5,command=lambda:self.write('9'))
        btn_mul = Button(self,text='*',bg='lightyellow',width=10,height=5,command=lambda:self.write('*'))
        btn_result = Button(self,text='=',bg='lightyellow',width=10,height=5,command=self.result)


        self.entry.grid(row=0,columnspan=4,ipady=15,padx=10)
        btn7.grid(row=1,column=0,pady=10)
        btn8.grid(row=1,column=1)
        btn9.grid(row=1,column=2)
        btn_mul.grid(row=1,column=3)
        btn_result.grid(row=2,column=1)

    def write(self,adad):
        temp = self.str_var.get()
        self.str_var.set(temp + adad)


    def result(self):
        temp = self.str_var.get()
        self.str_var.set(eval(self.str_var.get()))   

a = App()
a.mainloop()