def chap(x , y):
    print(x+y)

chap(4,6)

y = lambda a ,b : print(a + b)
y = lambda a ,b : chap(a,b)

y(2 , 4)