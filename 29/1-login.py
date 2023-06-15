from tkinter import *

class App:
    def __init__(self,master):
        self.master = master
        self.master.geometry('500x400')
#         self.master.iconbitmap('33.ico') # --> revesh aval change icon
        # revesh dovoom
        img = PhotoImage(file='22.png') 
        self.master.iconphoto(False , img) # false --> yani feghat dar hamin safheh anjam sheh True --> rooye hame ye panjere ha emal mikonad
        
        # create login page
        
        # create label for username
        self.user_name_label = Label(self.master,text = "username")
        self.user_name_label.grid(row=0 , column=0)
        
        #create entry for username 
        self.user = Entry(self.master , font = 5)
        self.user.grid(row=0 , column=1,ipady=20, ipadx=40, pady=20)
        
        # create label for password 
        self.password_label = Label(self.master,text = "password")
        self.password_label.grid(row=1 , column=0)
        
        # create entry password 
        self.password = Entry(self.master ,  font=5 , show='*')
        self.password.grid(row=1 , column=1 ,ipady=20, ipadx=40,pady=20)
        
        # create button for login
        self.click_btn = Button(self.master , text = 'login',width=10,height=5 , bg='green',command=lambda:self.login())
        self.click_btn.grid(row=2 ,columnspan=2)
        
    def login(self):
        self.user_name_label.grid_forget()
        self.user.grid_forget()
        self.password_label.grid_forget()
        self.password.grid_forget()
        self.click_btn.grid_forget()
        self.label = Label(self.master,text = 'sajjad you are login successfully',font=5, fg = 'green' , bg='lightblue')
        self.label.grid(row=4)
        
        



win = Tk()
a = App(win)  
win.mainloop()      
