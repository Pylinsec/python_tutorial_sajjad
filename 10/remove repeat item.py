list1 = [55,4,55,5]
# for i in range(1,len(list1)):
#     print(list1[i])
list2 = []
b = len(list1)
for i in range(0,b-1):
    k = 1
    print(i)
    a = list1[i]
    for j in range(k ,b-1):
        if a == list1[j]:
            del list1[j]
            b = b -1
        else:
            list2.append(list1[j])
            
    k +=  1      
print(list2)            
#         
        
