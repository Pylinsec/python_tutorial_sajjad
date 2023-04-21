from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x300')
        self.config(bg='lightyellow')
        self.make_widget()
        self.insert_data()


    def make_widget(self):
        # avval scrol bayad besazim
        #  make scrol
        self.scrol = Scrollbar(self)
        self.scrol.pack(side='right',fill='y')
        # make listbox
        self.list_box = Listbox(self,width=50,height=10,font=10 )   
        self.list_box.pack(padx=20) 
        # config
        self.list_box.config(yscrollcommand=self.scrol.set)
        self.scrol.config(command=self.list_box.yview)
        #  make btn for print
        btn_chap = Button(self,text='print',width=10,bg='black',font=5,fg='white',command=self.chap)
        btn_chap.pack(pady=10)
        btn_del = Button(self,text='delete item',width=10,bg='black',font=5,fg='white',command=self.delete)
        btn_del.pack(pady=10 , after = btn_chap)

        


    def insert_data(self):
        countries = ['japan','iran','usa','france','german','qatar','brezil',
                     'netherland','poland','russia','southafrica','cameron',
                     'canada','mexico','turkey']
    # self.list_box.insert(index,matn) index --> shomare line ,
    # example for inserting in listbox
        # for i in range(10):
        #     self.list_box.insert(END,f'line {i} --> sajjad')
        # END --> eshare be tah listbox 
        # 0 --> ebtedaye list

        for country in countries:
            self.list_box.insert(END,country)

    def chap(self):
        # gereftan etelaat az listbox
        print(self.list_box.selection_get())

    def delete(self):
        # hazf etelaat az listbox
        # self.list_box.delete(start,end) --> start --> index shoro  , end --> index payan
        # self.list_box.delete(0,END)  az index 0 ta AKHAR HAZF MIKONAD
        self.list_box.delete(5,8) # az khane 5 ta khane 8 hazf mikonad 

a = App()
a.mainloop()        