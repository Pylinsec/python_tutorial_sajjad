
def number():
    while True:
        num = int(input("insert one number: "))
        if num % 2 == 0:
            even()
        else:
            odd()    

def odd():
    print("this number is odd")

def even():
    print("this number is even")

# number()  

"""
def number():
    num = int(input("insert one number: "))
    if num % 2 == 0:
        even()
    else:
        odd()    

def odd():
    print("this number is odd")
    number()

def even():
    print("this number is even")
    number()
# number()   
"""


