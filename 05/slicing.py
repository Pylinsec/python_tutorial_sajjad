#string slicing  str[start:end:x]  start az 0 shoro ta  , x agar -1 bashad reshtejh ra makoos mikonad
str = "Which Browser is Best for Online Security"
length = len(str) # mohasebeh andazeh tool string 
print(length)
print ("az 10 ta akhar-->",str[10::1])
print ("az haef 10 ta harf 30-->",str[10:30:-1]) # 
print ("az avval ta harf 25-->",str[:25])
print ("az 10 ta akhar-->",str[-10:])
print ("az 10 ta akhar-->",str[31:])# manfi feqat jehat r a neshan midehad
print ("az 10 ta akhar-->",str[-10:-20:-1])

# concatenate  yeni chasbandan do rreshteh  strx = str1 + str 2 + str3 ...
str1 = "Which Browser is "
str2 = "Best for Online Security"
strx = str1 + str2 + " bolbol"
print (strx)
strx = str1 - str1
