ls = ['bbbbb','Red', 'Green', 'White', 'Blaceeek', 'Pink', 'Yellow']

#review
str = 'grelwwlen'
# for i in str:
#      print(i)
# print(str.replace('e' ,'*'))

str1 =""
for j in str:
    if j == 'e' or j=='l':
#         str1 = str1+'*'
          str1 = f"{str1}*"
    else:
        str1 = str1+j
print(str1)        
    


newlist = []       
for i in ls:
    if 'e' in i or 'l' in i:
        word = i.replace('e','*')
        word = word.replace('l','*')
        newlist.append(word)
    else:
        newlist.append(i)
        
print(newlist)        
        