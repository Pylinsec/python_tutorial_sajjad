
car1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car1['bomb']=car1.pop('brand')

print(car1)



keys = tuple(car1.keys())
print(keys)
values = tuple(car1.values())
print(values)
x =zip(keys,values)
print(x)