# list copy

# rah avval
list1 =[2,5,3,777,4,5,4,11,-1]
listcopy = list(list1)
print(listcopy)

#rah dovoom
newlist = list1.copy()
print(newlist)


# dardesar dar copy   warning !!!!!!!!!!!!!!!!!!!!!!!

list2 = list1  # dar in halat yek link bineshan dorost misheve 
list1.append("dardesar")
list2.pop(2)
print(type(list2))
print(list2)

print(list1)


