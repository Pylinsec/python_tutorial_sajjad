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
pygame.display.set_caption('polygon')

# draw polygon format
# pygame.draw.polygon(screen,color,((point1),(point2),(point),...),w)
# pygame.draw.polygon(screen,green,((500,434),(309,234),(20,24),(508,200)),0)
# pygame.draw.polygon(screen,green,((400,100),(200,200),(200,400),(400,500),(600,400),(600,200)),0)
pygame.draw.polygon(screen,green,((200,400),(400,500),(600,400),(600,200),(400,100),(200,200)),1)
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()        