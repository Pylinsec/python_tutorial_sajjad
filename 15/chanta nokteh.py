##len
set_name = {'golam','qoli','jamshid','rezvan','rezvan','rezvan','rezvan'}
print(len(set_name))

## data type  list , str , boolean , int , set , float ,

## type  -- > set
print(type(set_name))

## constructor  set  mikard be shart iterator bashed  iterator yani betonim roosh for bezenim
# set(list) set(string)  set(dict.values()) set(dict.keys())
# set(dict.items())  lotfan chek konid  {(,),(,)}
dict1 = {'name':'sajjad','lastname':'ansaryan','age':14}
print(set(dict1.items()))
newset =set(dict1.items())

print(dict(newset))