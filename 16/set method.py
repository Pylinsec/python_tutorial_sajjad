# clear - pop - update -del - add - discard-remove

# diffrence , diffrence_update
# intersection , intersection_update
#union
#isdisjoint()
#issubset()
#issuperset()

a = {'sajjad','ansaryan',15,True,}
b = {'sajjad','nohom',15,False}
c= a.intersection(b)
# -->**********************************
# diffrence and diffrence_update   heman tefazol khodeman hast  a-b
# c = a.difference(b)  # diffrence  item haye miare ke dar avali bashe dar dovomi nevashe
# d = b.difference(a) 
# print(d)
# a.difference_update(b)  # item ya ke dar avali hast dar dovvomi nist ra migireh mirize dakhel avvali 
# print(a,b)
# *************************************************
# --> intersection  and intersection_update  heman eshtrak khoeman hast 
# c = a.intersection(b)  # moshterak ha ra miareh 
# b.intersection_update(a)
# print(b)


#****************************************
#-------> union ejtema khodeman  
# a.union(b)
# print(a)

# ************************************************
# in seta True ya false barmigardanand 
# print(a.isdisjoint(b))  # ISDISJOINT  --> agar item moshtrak nebashad True barmigardand
# print(a.issubset(b)) # a.issubset(a) --> agar a zirmajmoeh b hast True bargardan
# print(c.issubset(b))

# print(a.issuperset(c)) # agar b dar shekam a bood true bargardan

# **********************
#  symetric_diffrence() , symetric_diffrence_update()
d = a.symmetric_difference(b)
print(d) # baraks eshtrak amal mikonad hazf moshtrak va avardan tegavot ha dar har do set
a.symmetric_difference_update(b)
print(a)