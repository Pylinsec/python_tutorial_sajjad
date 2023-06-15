# chest page 
from turtle import *
penup() # makhfi kardan cursor 
goto(-400,400)
pendown() # bargardandan cursor
pensize(3)
speed(0)

colors = ['red','blue']
for k in range(1,9):
    for j in range(1,9):
        begin_fill()
        sum = k + j
        fillcolor(colors[sum % 2])
        # for i in range(4):
        #     fd(100)
        #     rt(90)
        
        # circle(50) # dakhel perantez shoaa migere

        for i in range(3):
            fd(100)
            lt(120)
        penup()
        fd(100) 
        pendown()
        end_fill()
    penup()    
    goto(-400,400-100*k) 
    pendown()   


done()