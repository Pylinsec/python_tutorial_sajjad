for i in range(5 ,0,-1):
    for j in range(5,0,-1):
        if i >= j:
            print(" *",end="")
        else:
            print(" ",end="")
    print()
 

for i in range(5 ,0,-1):
    for j in range(0,6):
        if i <= j:
            print(" *",end="")
        else:
            print(" ",end="")
    print()    