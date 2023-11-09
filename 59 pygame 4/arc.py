import pygame ,sys 

# variables
size_x = 800
size_y = 700
pink = (177,142,205)
green = (0,255,0)
pi = 57


# surface
screen = pygame.display.set_mode((size_x,size_y))
screen.fill(pink)
# select title
pygame.display.set_caption('lines')
# pygame.draw.arc(screen,green,(x,y,r1,r2),start radian,end radin,w)
# pygame.draw.arc(screen,green,(200,200,300,300),0,90/pi,3)
# pygame.draw.arc(screen,green,(200,200,300,300),180/pi,270/pi,3)
pygame.draw.arc(screen,green,(200,200,500,500),90/57,270/pi,3)
pygame.draw.arc(screen,green,(200,200,500,400),90/57,270/pi,3)
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()        