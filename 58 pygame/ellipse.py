import pygame , sys , random


# define variables 
size_w = 1000
size_h = 800
sky_blue = (135, 206, 235)
white= (255,255,255)

# make screen
screen = pygame.display.set_mode((size_w,size_h))
pygame.display.set_caption('Snow Fall')
# screen.fill(sky_blue)
# pygame.draw.ellipse(surface,color,(location-x,location-y,qotr1,qotr2),width)
pygame.draw.ellipse(screen,sky_blue,(300,400,200,100),2)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()        
