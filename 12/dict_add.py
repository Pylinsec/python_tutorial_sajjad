car1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# change  1- add   2-remove or delete

# add  revesh 1  taqir yeki 
# car1['brand'] = 'pride'
# print(car1)
# # add  revesh 2 chand item ra change konim  ba car1.update({key:value})
# car1.update({'brand':'saipa','option':'airbag'}) #  
# print(car1)
 # change key 
keys = tuple(car1.keys())
values = list(car1.values())
torob = keys.index('year')  # shomare khone year barmigardanad
keys[torob]='havij'
print(keys)

x = zip(keys,values)
print(x)
new_car = dict(zip(keys,values)) # zip tabe hast ke 2 list migirad va ozvhaye hamshomare dokht mikonad 
print(new_car)





