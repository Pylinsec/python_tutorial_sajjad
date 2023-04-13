from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x600')
        self['bg'] = 'lightgreen'
        self.make_widget()
#  access data for spinbox
    def lbl_write(self):
        self.lbl.config(text=self.spin.get(),font=10)

#  make widget 
    def make_widget(self):
        self.lbl = Label(self)
        self.lbl.pack()
        self.spin = Spinbox(self,width=40 ,font=1,command=self.lbl_write)   
        self.spin.pack(pady=30 , ipady=10) 
        # rahehal meghdae dehi spinbox
        self.spin.config(from_=1,to=100, increment=5)
     # rahel 2 estefadeh az list , tuple , set , dictionary
        colors = ['red','blue','green','yellow']
        # colors = 'sajjad ansaryan from iran in jam'
        self.spin.config(values=colors)
        self.spin.set('select')
       
       
      


a = App()
a.mainloop()        