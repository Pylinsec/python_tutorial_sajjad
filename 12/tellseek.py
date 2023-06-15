# with open('file.txt','a+w') as f:
#     print(f.tell())  # tell --> position pointer neveshtan ra neshan midehad
#     print(f.read())
#     print(f.tell())
#     f.seek(10)  # seek --> jabeja kardan position pointer 
#     print(f.tell())
#     print(f.read())

with open ('file.txt' ,'a') as file:
    print('before',file.tell())
    file.write("*sajjad**ansaryan*")
    print('after',file.tell())
    file.seek(8)
    file.write("@jam@")