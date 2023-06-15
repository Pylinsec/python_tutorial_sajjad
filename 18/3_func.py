"""
def chap(x):  # chap(parameter)
    if x < 0:
        print("manfi")
    if x > 0:
        print("mosbat")

for i  in (-100,20,1,5,-500):
    chap(i) # argument --> chap(argument) 
"""


# make calculator 
def calc(a ,b ,opr):  # opr --> heman operation (amalgar mesl -+*/)
    if opr == '+':
        print(f"{a} + {b} = {a + b}")
    if opr == '-':
        print(f"{a} - {b} = {a - b}")
    if opr == '*':
        print(f"{a} * {b} = {a * b}")
    if opr == '/':
        print(f"{a} / {b} = {a / b}")

#  call 
calc(22,5,'+')        
calc(22,5,'-')        
calc(22,5,'*')        
calc(22,5,'/')        
calc(222,55,'*')        


# sakht jadval zarb 
for i in range(10):
    for j in range(10):
        calc(i,j,'*')

