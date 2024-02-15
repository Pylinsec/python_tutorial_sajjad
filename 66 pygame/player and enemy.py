# modules
import sys , pygame , random

pygame.init()

# variables
size = (1200,800)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
player_x = random.randint(0,1140)
player_y = 700
step = 20

# display
win = pygame.display.set_mode(size)

# title
pygame.display.set_caption('make button')

# functions


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += step
            if event.key == pygame.K_LEFT:
                    player_x -= step
    
    # check mandan shekl dakhel window                
    if player_x < 0:
        player_x = 1140            
    if player_x > 1150:
        player_x = 0            
    win.fill(black)            
    pygame.draw.rect(win,blue,(player_x,player_y,60,60))        
    pygame.display.update() 
        

           
