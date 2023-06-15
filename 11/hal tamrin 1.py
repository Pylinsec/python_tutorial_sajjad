ls = [1,'a',330,300,2,'1',23,'b','a',1,250,300]

#rah 1
result =[]

for i in ls:
    if i not in result:
        result.append(i)
print(result)

# rah dovom

result1 =[]
[result1.append(x) for x in ls  if x not in  result1]
print(result1)
# rah3
result3 = set(ls)  # majmooeh ke ozve tekrai nemipezire 
result4 = list(result3)
print(result4)
        