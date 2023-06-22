data = [{'name':'sajjad','lname':'ansaryan','age':15,'city':'jam'},
        {'name':'taha','lname':'nemati','age':15,'city':'jam'},
        {'name':'bardia','lname':'kamaei','age':14,'city':'jam'},
        {'name':'ali','lname':'bazyari','age':15,'city':'jam'}]

info = {'name':'sajjad','lname':'ansaryan','age':15,'city':'jam'}
# print(info.keys())
# int(info.values())

list1 = list(info.values())
list_key = list(info.keys())

for i in list1:
    if i == 15:
        print(list1.index(15))
        print(list_key[2])


# for i in info:
#     print(i)
#     print(info[i])

# for i , j in info.items():
#     print(i,j)    

