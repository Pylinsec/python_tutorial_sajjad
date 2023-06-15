# from turtle import *  # * --> harche bood az 0 ta binehayat 
#forward(adad)jelo raftan  backward(adad)aqab raftan  right(zavieh)charkhesh be rast left(zavieh)
import turtle
turtle.pensize(5) # andazeh medad
turtle.pencolor('green') # rang medad
turtle.fillcolor('yellow') # rang dakhel shekl
turtle.begin_fill() # shoro jaye por kardan rang
turtle.speed(1) # speed(0,10) --> 0--> fastest  1--> slowest  3--> slow 10--> fast 6--> normale
for i in range(2):
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.fd(100)
turtle.goto(-100,-100)    
for i in range(2):
    turtle.right(90)
    turtle.forward(200)
    turtle.rt(90)
    turtle.fd(100)
        
# turtle.right(90)
# turtle.fd(200)
# turtle.right(90)
# turtle.fd(100)
turtle.end_fill() # payan rang kardan dakhel shekl 
