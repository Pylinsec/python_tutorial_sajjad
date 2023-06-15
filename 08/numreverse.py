num = 9
str1 = ""
mul = 1
while num :
    str1 += str(num)
    mul *=num
    num -= 1
print(f"{'*'.join(str1)} = {mul}")    
    