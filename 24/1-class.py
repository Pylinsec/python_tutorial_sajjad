class Person:
    count = 0
    def __init__(self, fname, lname, age):
        self.name = fname
        self.lname = lname
        self.age  = age # object variable 
        Person.count += 1# class variable 

    def info(self , color): # object varible 
        print(self.name , self.lname , self.age )
        print(f"hair colors is {color}")

    def print_count(self):
        print(Person.count)

# sajjad = Person('sajjad','ansaryan',14) # ersal argoman be __init__
# sajjad.info("black") # ersal argomamn be tabe khas hengam seda kardan oon tabe ersal mikonim
qoli = Person("qoli","qolizadeh",25)
# qoli = Person("jafar","bolboli",65)
qoli.print_count()
