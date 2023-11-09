import pygame ,sys 

# variables
size_x = 800
size_y = 700
pink = (177,142,205)
green = (0,255,0)



# surface
screen = pygame.display.set_mode((size_x,size_y))
screen.fill(pink)
# select title
pygame.display.set_caption('lines')
# pygame.draw.line(screen,color,(point1),(point2),width)
# pygame.draw.line(screen,green,(100,100),(400,300),3)
pygame.draw.lines(screen,green,False,[(100,120),],3)
# pygame.draw.lines(screen,green,True,((100,120),(200,120),(200,220),(400,334)))
# pygame.draw.aaline(screen,green,(100,140),(400,340)) # w naghshi nedarad 
# pygame.draw.aalines(screen,green,True,((100,140),(200,140),(200,240),(400,354)),300)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()        