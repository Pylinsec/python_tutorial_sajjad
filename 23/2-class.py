class Human:
    
    def __init__(self,lname): # dunder method--> double underscore  init--> initial (shoroo)
        self.name = 'sajjad'
        # self.lname = lname 
        self.PrintName()
        self.PrintName2(lname)
     
    def PrintName(self):
        print(self.name)

    def PrintName2(self,lname):
        print(f"{self.name} ---> {lname}")

        
sajjad = Human
# rahkar avval jehat 
sajjad('ansaryan')
# sajjad.PrintName2()

#revesh dovom call function 
