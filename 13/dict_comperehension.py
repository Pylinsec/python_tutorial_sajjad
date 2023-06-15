#mesal 2
new_dict = {}
for i in range(10):
    new_dict[i]=i*i
    
print(new_dict)
new2 = {i:i*i for i in range(10)}
print(new2)


# example 2
dict_age={'bob':20 ,'henry':50 ,'emily':33 ,'john':25 ,'jack':70 }
new_age= {}
for i , j in dict_age.items():
    if j > 40:
        new_age[i] = "old"
    else:
        new_age[i] = 'young'
print(new_age)        
new_age2 = {k:('old' if v>40 else 'young') for (k,v) in dict_age.items()}
print(new_age2)