# mashgh 1
# t = 200
# while t :
#     print(t)
#     t -= 1
#     
# k = 0
# while k<= 6:
#     print("* * * * * *")
#     k +=1
#  
# print('python','iran','france',sep=" X ")  #sep = " "  jodakonande 
# print('course' , end="\t")   # end = "\n" vaqti kar temam shod ba khat bad chikar konad 
# print('course11123')

# j , i = 0 , 0
# while i <= 5:
#     while j <= 5:
#         print("*" , end="")
#         j += 1
#     print()
#     i += 1

# while True:
#     num = int(input("vared kon adad: "))
#     if num >= 0:
#         print(f"{num} is positive")
#        
#     else:
#         print(f"{num} is negetive")


num = 128
str1 = ""
# sum = 0
# mul = 1
while num:
    
    baqimandeh = num % 10
    str1 =  str1 + str(baqimandeh)
    print(str1)
    
    
#     sum = sum + baqimandeh
#     mul = mul * baqimandeh
    num =num // 10
    
print(str1)
# print(sum)
# print (mul)

i = 0
while True:
   print(i)
   i = i + 1