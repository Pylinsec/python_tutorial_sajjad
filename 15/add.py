### add in set 

set_name1 = {'golam','qoli',False,'rezvan',222,'rezvan',5.255}
set_name2 = {1,2,3,4}

# revesh 1  set_name1.add('havij')
set_name1.add('havij')
set_name1.add(22222555555555555555555555555)
print(set_name1)
# revesh 2  set_name.update(set,list ,dict.items(),dict.keys(),str , dict.values() ,INT)
# deqqat shevad ke dar in revesh list, set , ...  bashad 
set_name1.update(set_name2)
print(set_name1)
print(set_name1.update(set_name2)== set_name2.update(set_name1)) # for fun 
set_name1.update([11,22,33])
set_name1.update((11,22,33))
set_name1.update()
print(set_name1)
print(1,2)
print((1,2))



