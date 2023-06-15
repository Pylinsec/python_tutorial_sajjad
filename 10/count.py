# method list : count - extend -pop-del-clear - remove-copy-reverse-insert-append-sort
# count 
list2 = ["sajjad", 3, ":ansaryan", 5, 4,"iran", 7, 5, 4, 7]
# print(list2.count(4))  # count(x)  tedad x ha ra barmigardanad


for i in list2:
    print(list2.index("iran"))
    print(f"{list2.index(i)} --> {i}")
#    print(list2.index(i))
print(list2[list2.index("iran")])


for i in range(0,len(list2)):
    print(list2[i])