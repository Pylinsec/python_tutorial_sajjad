# 
# # adameh mabhas list
# list1 = [ 22,33, 45,67,-1]
# newlist = [i for i in list1 if i> 40]
# new3 = [y for y in list1 if y % 2 ==1]
# new4 = [ x for x in  list1 if x  >4]
# 
# new5 = [x * 3 for x in list1]
# new6 = [x**2 for x in list1]
# new7 = []
# for x in list1:
#     new7.append(x**2)
#     
# print(new7    
#     
# 
# 
# print(new6)
# print(newlist)
# new2 =[]
# for i in list1:
#     if i > 40:
#         new2.append(i)
#         
# print(new2)        
#


strlist =["taha","nemati","school","banana"]
new11 = [str.title() for str in strlist]
new12 = [str.upper() for str in strlist]
new13 = [str if str != "banana" else "apple" for str in strlist ]
print(new11)
print(new13)

list1 = [ 22,33, 44,67,-1]
list14 = [x if x % 2 == 0 else "havij" for x in list1]
print(list14)
