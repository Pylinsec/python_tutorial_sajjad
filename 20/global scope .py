# type variable --? bool - str - int- float
# global --> variabli ke dakhel hich function nebaseh 
# local --> mahali --> variable dakhel function 

# x = 'global'
# def main():
#     x = 'local'
#     print(x)

# main()
# print(x)    

y = 400
def add():
    
    global z
    z = 800
    a = y
    a = a * 5
    # global y
    # y = y * 3
    return a
print(add())
print(y , z)    