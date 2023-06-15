#file ha  kar ba file haye matni

#format 1
# file = open("path",option)  path --> masir file ast
# opption  r --> read  w --> write   a --> append   x -->

file = open("1.txt","a")  # w  harbar mikobeh az aval misaze  vali  a agar nebood misaze agar bood edame file minevise
file.write("sajad ansaryan")

file.close()
# optipon x  agar file nebood misaze agar bood error midehad
# neveshtan dar file  write  , writeline
# file1 = open("3.txt","a")
# for i in range(20):
#     file1.write("sajjad\t")
#     
# file1.close()


#format 2
with open("4.txt","a") as f:
    #f.writelines(["sajjad\n","ansaryan\n",'4\t'])
    f.writelines("""To insert characters that are illegal
in a string, use an escape character.

An escape character is a backslash \ followed by th
e character you want to insert.

An example of an illegal character is a
double quote inside a string that is
surrounded by double quotes:":""")
    
with open('3.txt','r') as f:
    pass
    #print(f.read()) # tabe read()  kol file ra mikhane f.read()  string barmigardaned
#     print(f.read(20)) # f.read(number)  tedad harf miareh az aval file
#     print(f.read()[1:50])
    
#     print (f.readline(-1))  # khat avval barmiogardanad
#       print(f.readlines())  # list bar migardand ke har khat yek item dar list mishevad 
# counter = 0  
# with open('3.txt','r') as f:
#     for i in f.readlines():
#         for j in i:
#             if j == " ":
#                 counter += 1
#         counter += 1    
# print(counter)

with open('3.txt','a') as f:
    print(f.tell()) # position character akhar + 1
    print(f.seek(20)) # position jadid
    print(f.tell())
    
    f.write("python")
    print(f.tell())



            
      
    
    