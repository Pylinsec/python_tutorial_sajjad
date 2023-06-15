from tkinter import *

# class App(Tk):
#     def __init__(self):
#         super().__init__()
        
# a = App()
# a.mainloop()

class A:
    def __init__(self):
        print('sajjad')
        print('ansaryn')
        self.dog = 'jerman'

    def havij(self):
        print('a__havij')
        

class B(A):
    def __init__(self):
        super().__init__()
        print(self.dog)
        self.havij()


    


b = B()



       
