# review 
#  data type --> boolean , integer, float,string
#list[] , dictionary{"":""},tuple , set{} -->  ['q',1,4.5,True , list , tuple,dict]

# tuple ()   vigegi --> unchangable ( meqdar har index nemishe avaz kard)
tuple1 = (1,2,3)
# tuple1[1]=4 
# print(tuple1)

# vigegi 2 --> ordered  yani agar jaye meqdar index ha avaz koni tuple avaz mishe 
# print((11,22,33) == (22,11,33))  # false barmigaranad
# vigegi 3 -- > allow duplicate item  --> peziresh ozv tekrari 
# print((11,11,33))

#  hesab tool tuple  len(tuple)   
# s = (1,2,3,4,5,6)
# print(len(s))

#  access item in tuple 
tuple2 = ('sajjad','ansaryan',14 , 17,18)
print(tuple2[:])  # [start:end:step]
print(tuple2[:-1])  # ta yeki mande ba akhar 
print(tuple2[:-2])  # ta 2 ta monde be akhar 
print(tuple2[-1:])  
print(tuple2[-3:-1])  
print(tuple2[-1:-3:-1])  
print(tuple2[4:0:-1])  




