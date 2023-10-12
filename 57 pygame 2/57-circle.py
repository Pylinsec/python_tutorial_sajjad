import pygame , sys

pygame.init()
# variables

size = (600,800) # w = 600 , y = 800
green = (0,255,0)
# make surface
win = pygame.display.set_mode(size)
# define title for win
pygame.display.set_caption('Game1')

# circle --> pygame.draw.circle(surface,color,(location x, y),radius,width)  , radius --> shoae
pygame.draw.circle(win,green,(300,300),60,1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()        
    # pygame.display.flip()       