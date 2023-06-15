#  nokte 1  beraye hazf va ezafe kardan bayad tuple ra be list tabdil kard 
# list1 = list(tuple2)  # tabdil be list 
# list1[3]='iran'
# tuple2 = tuple(list1)  # tabdil be tuple 
# # del tuple2   # hazf kamel tuple 

# print(tuple2)

tuple2 = ('sajjad','ansaryan',14 , 17,18)
tuple3 = ('laboo','qoli','baqali','qoli')

# nokte 2  JOIN   tuple1 join tuple2  tupl1 +=tuple2   tuple3 = tuple1 + tuple2
# print(tuple3 + tuple2)
# tuple2 += tuple3
# print(tuple2)


# NOKTEH 3  COUNT   INDEX 
# print(tuple3.count('qoli'))  #  count shomeresh tedad item 
# print(tuple3[3:].count('qoli'))

# index 
print(tuple3.index("qoli"))  # shomare avalin khane ke daresh item moored nezar hast 


# unpacking tuple 
fruit = ('ananas','chery','blueberry','lemone' , 'banana' ,'sajjad')
(green,red,blue ,*yellow) = fruit  # * be manay 0 ta binehayat 

print(green)
print(red)
print(yellow)

