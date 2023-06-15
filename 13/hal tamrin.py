dict1 = {'ten': 20, 'ten': 250, 'Thirty': 30}
print(dict1)
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {'sixty': 30, 'seventy': 40, 'eigty': 80}
dict3['sixty'] = 1000
print(dict3['sixty'])

# for i , j in dict3.items():
#     if j == 40:
#         print(i)
#     else:
#         print('nist')


# a = list(dict3.keys())
# b= list(dict3.values())
# print(a,b)
# for i in b:
#     if i ==40:
#         result = b.index(40)
#         print(a[result])
#

td={}
for h in "abcdefghijklmopqrstuvwxyz":
    td[h]=h.upper()
#     dit={h:h.upper()}
#     td.update(dit)
print(td)



        