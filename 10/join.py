# join  rah1  list3 = list 1 + list 2
list1 = [1,3,4]
list2 = [5,4,7]
print(list1 + list2)
print(list2 + list1)

# rah2 append

for i in list2:
    list1.append(i)
print(list1)
#list2.append(list1) # deqat kon 
print(list2)

# rah 3  list1.extend(list2)  extend miad list2 ra be tah list1 michaspand 
list1.extend(list2)
print(list1)
list2.extend(list1)

