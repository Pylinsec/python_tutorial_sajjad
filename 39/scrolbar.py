from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('100x400')
        self['bg'] = 'lightgreen'
        self.make_widget()


#  make widget 
# # dar jehat mehvar y ha 
#     def make_widget(self):
#         self.scrol = Scrollbar(self,) 
#         self.scrol.pack(side='left', fill=Y)   
#         self.text = Text(self,font=15,bg='yellow')
#         self.text.pack()
#         for i in range(100):
#             self.text.insert(f"{i}.0",'sajjad\n')
#         self.text.config(yscrollcommand=self.scrol.set) # etesal widget text be scrol  dar jaehat y ha 
#         self.scrol.config(command=self.text.yview) # etesl scrol be wieget text  dar jehat y ha 
       
    def make_widget(self):
        self.scrol = Scrollbar(self,) 
        self.scrol.pack(side='top',fill=BOTH)   
        self.text = Text(self,font=15,bg='yellow',wrap='word')
        self.text.pack()
        for i in range(100):
            self.text.insert(f"{i}.0",'sajjad --> ')
        self.text.config(xscrollcommand=self.scrol.set) 
        self.scrol.config(command=self.text.xview) 
       
      


a = App()
a.mainloop()        