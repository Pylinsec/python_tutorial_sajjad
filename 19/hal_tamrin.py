# rah hal1
# def majmoo_adad(*adad):
#     print(type(adad))
#     total = 0
#     for num in adad:
#         total +=num
#     print(total)


# majmoo_adad(1,2,3,4,5,11,6,7)  
# #rah 2  
# def majmoo_adad(adad):
#     total = 0
#     for num in adad:
#         total +=num
#     print(total)

# majmoo_adad({1,2,3,4,5,11,6,7})    


#tamrin 
text = "thIs iS A PythonN CoURSe by MR Binandeh For Sajjad"

def count(text):
    lower = 0
    upper = 0
    for i in text:
        if i.islower():
            lower +=1
        else:
            if i != " ":
                upper += 1

    print(f"voojood darad lower= {lower} , upper = {upper}")        
count(text)                

# *****************revesh2
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower1 = upp.lower()
print(lower1)
def new_find(text):
    low_count=0
    upp_count = 0
    for i in text:
        if i in upp:
            upp_count +=1
        else:
            pass

        if i in lower1:
            low_count += 1    
    print(low_count, upp_count)        

new_find(text)