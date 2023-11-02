import pygame , sys , random , time

pygame.init()

size = (700,600)
white =(255,255,255)
black =(0,0,0)
x = 15
x1=115
x2=500
x3=250
x4=170
x5=115
x6=500
x7=250
x8=170
r = 15
y=0
y1=5
y2=2
y3=10
y4=15
y5=18
y6=20
y7=23
y8=25
color=white
per= 'tur'


win = pygame.display.set_mode(size)
pygame.display.set_caption('snow falling')



while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if y == 710 or per == 'tur':
        per= False
        x1 = random.randrange(15,585)
        x2 = random.randrange(15,585)
        x3 = random.randrange(15,585)
        x4 = random.randrange(15,585)
        x5 = random.randrange(15,585)
        x6 = random.randrange(15,585)
        x7 = random.randrange(15,585)
        x8 = random.randrange(15,585)
        x = random.randrange(15,585)
        y=0
        y1 = random.randrange(0,100)
        y2 = random.randrange(0,100)
        y3 = random.randrange(0,100)
        y4 = random.randrange(0,100)
        y5 = random.randrange(0,100)
        y6 = random.randrange(0,100)
        y7 = random.randrange(0,100)
        y8 = random.randrange(0,100)


    win.fill(black)
    time.sleep(0.1)
    reduce = 12
    circle1 = pygame.draw.circle(win,color,(x,y),reduce)
    circle2 = pygame.draw.circle(win,color,(x1,y1),reduce)
    circle3 = pygame.draw.circle(win,color,(x2,y2),reduce)
    circle4 = pygame.draw.circle(win,color,(x3,y3),reduce)
    circle5 = pygame.draw.circle(win,color,(x4,y4),reduce)
    circle6 = pygame.draw.circle(win,color,(x5,y5),reduce)
    circle7 = pygame.draw.circle(win,color,(x6,y6),reduce)
    circle8 = pygame.draw.circle(win,color,(x7,y7),reduce)
    circle9 = pygame.draw.circle(win,color,(x8,y8),reduce)
    y += 10
    y1 += 10
    y2+= 10
    y3+= 10
    y4+= 10
    y5+= 10
    y6+= 10
    y7+= 10
    y8+= 10
 
    pygame.display.update() 