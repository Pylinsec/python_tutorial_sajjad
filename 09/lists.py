# define and  condition
# list1 = [1 , 2 ,3] # list sakhteman dade ei ast ke ozvhash ba kama joda shodan
# ozve tekrari darad - changeable - ordered nazm
# list1 = [1,2]
# list2 =[2,1]
# print(list1 == list2)

# print(list1)
# print(type(list1))
# print(len(list1))
# 
# list2 = ["python",3.45,44,True,[3,4,6]]
# print(list2)

# data type:  string , float , int , bool , list , tuple , dictionary , set 
#_______________________________________________
# make list
#str = "python"
# str = "12345654"
# print(type(str),str)
# list1 = list(str) # list yek sazande hast ke iterable migire va list misazad
# print(type(list1),list1)
#___________________________________________________________
#access data
# list2 = ["python",3.45,44,True,[3,4,6,[44,78]]]
# print(list2[1])
# print(list2[1:3])
# print(list2[-3])
# print(list2[1:4:2]) # list[start ,end , step]
# print(list2[-3:])
# print(list2[-2])
# # print(list2[::-3])
# print("python"[-2])
# #list3 = list2[5]
# print(list2[-1][-1][-2])
# # print(list3[1])
#______________________________________________
# change list
# revesh 1  tagiir mosteqim ozv
# list2 = ["python",3.45,44,True,[3,4,6,[44,78]]]
# list2[3] = 5464984
# print(list2)
# 
# #revesh 2 change range item
# list2[2:10] = ["sajjad","ansaryan",14,"sajjad","ansaryan",14]
# print(list2)
# # revesh 3 :  insert(index , value)  --> list1.insert(3,'sajjad')
# list2.insert(1,"havij")
# print(list2)
#________________________________________________
# add item to list
# revesh 1
# list2 = ["python",3.45,44,True,[3,4,6,[44,78]]]
# list2.append("roobah gol")  # in mohom hast
# print(list2)
# revesh 2  extend list  --> list1.extend(list2) list2 ra be tah list1 azafeh mikonad
# list_a = [5,64]
# list_b = [True , "sajjad"]
# list_a.extend(list_b)
# list_a.append("sajjad")
# print(list_a)
# print(list_a.extend(list_b))  # revesh eshtebah 

#_____________________________________
# how to remove item from list
# revesh 1 remove  list1.remove("sajjad")
list1 = [22,33,55,66,44]
# list1.remove(66) # aval search bad remove 
# print(list1)

# revesh 2  pop  list1.pop(index shomare khane)  khane 3 ra hazf mikonad agar list1.pop() az akhar yeki hazf mikonad
# list1.pop(2)
# print(list1)
# print(list1.pop())  # eshtebah margbar
#revesh 3  del list1[index]  feghat khane 1 hazf kon , del list1 kollan hazf
# del list1[1]
# print(list1)
# del list1
# print(list1)

#revesh 4 clear  hazf dadeha
# list1.clear()
# print(list1)
#_____________________________________________________________________________
# how to loop on list
list1 = [22,33,55,66,44]
for i in list1:
    print(list1.index(i))
    
# with open("r.txt","a") as f:
#     while True:
#         f.write("pytbon:")

# list comperehension 
# sort
# copy 
#join
#methods 

