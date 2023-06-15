# i = 0
# while i <= 5:
#     j = 0
#     while j <= 5:
#         if i == j or i + j ==5:
#             print("A" , end=" ")
#         
#         else:
#             print("B", end = " ")
#            
#         j +=1
#     print() 
#     i += 1

for i in range(6):
    for j in range(6):
        if i ==j or i + j ==5:
            print("A",end=" ")
        else:
            print("B",end=" ")
    print()        