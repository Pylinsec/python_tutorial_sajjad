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
        btn_chap.pack(pady=10,side='left',padx=5)
        btn_next = Button(self,text='next',width=10,bg='black',font=5,fg='white',command=self.next)
        btn_next.pack(pady=10 , side='left',padx=5)
        btn_back = Button(self,text='back',width=10,bg='black',font=5,fg='white',command=self.back)
        btn_back.pack(pady=10 , side='left',padx=5)
        btn_len = Button(self,text='listbox length',width=10,bg='black',font=5,fg='white',command=self.print_len)
        btn_len.pack(pady=10 , side='left',padx=5)

        #  label
        self.lbl = Label(self)
        self.lbl.pack(side='bottom')

     

    def insert_data(self):
        countries = ['japan','iran','usa','france','german','qatar','brezil',
                     'netherland','poland','russia','southafrica','cameron',
                     'canada','mexico','turkey']
        for country in countries:
            self.list_box.insert(END,country)
            
        # zoom kardan rooue widget --> faal shodan keyboard rooye list_box
        self.list_box.focus_set()    
        self.list_box.selection_set(0) 
          

    def chap(self):
        # gereftan etelaat az listbox
        self.lbl.config(text=self.list_box.selection_get())
        # print(self.list_box.selection_get())


#  function next
    def next(self):
        #  gereftan index item ke entekhab shode
        self.index = self.list_box.curselection()[0] # cur --> HEMAN CURSOR --> HEMAN NESHANGAR
        print(self.index)
        #  update index 
        self.index += 1
        #  active kardan ba estefadeh az index
        self.list_box.activate(self.index)
        # self.list_box.selection_clear()
        self.list_box.select_clear(0,END)
        # select line jadid
        self.list_box.selection_set(self.index)


# function back 
    def back(self):
        #  gereftan index item ke entekhab shode
        self.index = self.list_box.curselection()[0] # cur --> HEMAN CURSOR --> HEMAN NESHANGAR
        print(self.index)
        #  update index 
        self.index -= 1
        #  active kardan ba estefadeh az index
        self.list_box.activate(self.index)
        # self.list_box.selection_clear()
        self.list_box.select_clear(0,END)
        # select line jadid
        self.list_box.selection_set(self.index)

# bedast avardan tool listbox
    def print_len(self):

        print(self.list_box.index(END))
        print(self.list_box.size())

a = App()
a.mainloop()        