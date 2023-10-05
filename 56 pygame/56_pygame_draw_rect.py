import pygame , sys

# variales
size = (800,800)
black = (0,0,0)
yellow = (255,255,0)
red = (255,0,0)
blue= (0,0,255)
green =(0,255,0)
white = (255,255,255)

# create surface
win = pygame.display.set_mode(size)
# change name of win
pygame.display.set_caption('rectange') # mostetil

# rasm mostetil 
# format --> mostetil --> pygame.draw.rect(surface,color,(location,size),width) #
pygame.draw.rect(win,yellow,(100,100,80,80),2)
pygame.draw.rect(win,white,(200,200,80,80),2)
pygame.draw.rect(win,green,(300,300,80,80),2)
pygame.draw.rect(win,blue,(400,400,80,80),2)
pygame.draw.rect(win,red,(500,500,80,80),2)
pygame.draw.rect(win,(200,200,3),(600,600,80,80),2)
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # pygame.display.update()        
