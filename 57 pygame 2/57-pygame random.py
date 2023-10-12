import pygame , sys  , random , time

pygame.init()
# variables
size = (1800,1000) # w = 600 , y = 800
blue = (0,0,255)
white =(255,255,255)
r = 50 # shoae
# make surface
win = pygame.display.set_mode(size)
# define title for win
pygame.display.set_caption('Game1')

def sky():
    for i in range(50):       
        time.sleep(.3)        
        x = random.randrange(50,1750)        
        y = random.randrange(50,950)
        r = random.randrange(1,25)  
        circle = pygame.draw.circle(win,white,(x,y),r)
        return circle
        


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    sky()      
    pygame.display.update()        
    # pygame.display.flip()       