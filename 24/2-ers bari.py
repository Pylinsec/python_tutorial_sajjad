class Father:
    def __init__(self,father_name, father_age, mostash):
        self.father_name = father_name
        self.father_age = father_age
        self.mostash = mostash
     
    def print_father_info(self):
        print(f"father info is {self.father_name}")
        if self.mostash:
            print(f"{self.father_name} sibil darad")
        else:
            print(f"sajjad sibil nedarad ")    


class Child(Father): # format ers bari 
    def __init__(self,child_name, child_lname, child_age,is_student,fname ,fage ,mostash): 
        self.child_name  = child_name
        self.child_lname = child_lname
        self.child_age = child_age
        self.is_student = is_student
        super().__init__(fname,fage ,mostash) # 

    def print_child_info(self):
        print(f" name bache hast {self.child_name} , {self.child_lname}")
        print(self.father_name)
        self.print_father_info()


qoli = Child('ahmad' ,30 , False,'qoli',' jamshidi',14,True)
qoli.print_child_info()


