list1 = [500,1,2,3,4,5,5,2,3,55,67,26442,-1,6,7,34,23,21,55,4,2,680]
min = list1[0]
max = list1[0]
for i in range(len(list1)):
              
    if max < list1[i]:
        max = list1[i]
    
print(max)    
    