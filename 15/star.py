from turtle import *
speed(0)
pencolor('red')
fillcolor('yellow')
colors= ('red','yellow','green','pink','red','yellow','green','red','yellow','green','pink','pink','red','yellow','green','pink','red','yellow','green','pink') # avali pencolor hast dovomi fillcolor hast

pensize(3)
for j in range(20):
    fillcolor(colors[j])
    pencolor(colors[j])
    rt(25)
    begin_fill()
    for i in range(4):
        fd(200);rt(90)
    end_fill()
done()    