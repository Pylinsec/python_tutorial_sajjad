#  tevabe bedoo name 
#  format --> lambda ARGUMANT: EXPRESSION
#  mesal
# def add(num1, num2):
#     print(num1+num2)
# add(3,5)    

# x = lambda num1 ,num2: print(num1 + num2)
# x(3,5)

# x = lambda num1 ,num2: num1 + num2
# print(x(3,5))


# ***********************
# def pow(x):
#     print(x*x)

# y = lambda a,b,c,d: a*b*c*d
# print(y(1,2,3,4))
# *********************************************

list1 = []
for i in range(20):
    list1.append(i)
print(list1)

a = lambda list1:print([i for i in list1 if i %2 ==0])
a
