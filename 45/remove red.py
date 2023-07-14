
colors = ['red','blue','green','yellow','red','red','blue','black','white','green','red','yellow','Red']

# count = colors.count('red')
# print(count)
# # colors.remove('red')
# # print(colors)

# for i in range(4):
#     colors.remove('red')

# print(colors)    

# ________________________
# red , Red 
count = colors.count('red')

print('red'.title())
print('red'.replace('e','E'))
print(len('red'))

for i in range(4):
    index = colors.index('red')
    colors.remove('red')
    colors.insert(index,'pink')
    print(index)

print(colors)    