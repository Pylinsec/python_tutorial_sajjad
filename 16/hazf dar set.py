# hazf az set --. remove , discard, pop , del , clear
temp = {14,'qoli',2,'golabi','boz',92,'levashak',3363}
# _______________________________________________________
# remove() , discard()
# temp.remove('qoli')  
# temp.remove('qoli1') # remove agar item payda nekard error midehad 
# print(temp)
# # temp.discard('levashak')
# temp.discard('levashak1') # discard agar item ra payda nakard error nemidehad
# print(temp)

#__________________________________________________________
# hazt az set ba pop()
# print(temp)
# temp.pop() # yeki mindazeh biroon 
# print(temp)

# ________________________________________________
# temp.clear() --> item haye set ra hazf mikonad yani feqat adamye khane mindaze biroon 
# del temp--> kolan set ra hazf mikonad  yani khod sakhteman kharab  mikonad
print(temp)
temp.clear()
print(temp)
del temp  # !!!!!  -- be nahve format deqat shavead del qabl az set miad 
print(temp)
