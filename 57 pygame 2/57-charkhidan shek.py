import pygame , sys , time

pygame.init()
# variables
size = (800,630) # w = 600 , y = 800
black =(0,0,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
red=(255,0,0)
color = yellow
rect_x = 0
rect_y = 0
# make surface
win = pygame.display.set_mode(size)
# define title for win
pygame.display.set_caption('Game1')

rect = pygame.draw.rect(win,color,(rect_x,rect_y,80,80))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win.fill(black)  
    time.sleep(0)      
    rect = pygame.draw.rect(win,color,(rect_x,rect_y,80,80))        
    if rect_y == 0 and rect_x <= 720:
        rect_x += 10
        color=yellow
        # win.fill(red)
    if rect_x == 720 and rect_y <= 540:
        rect_y += 10 
        color= red  
        # win.fill(green)
    if rect_x >= 10 and rect_y == 550:
        rect_x -= 10   
        color = blue 
    if rect_x == 0 and rect_y >= 10:
        rect_y -= 10  
        color = green  
    # pygame.display.update()        
    pygame.display.flip()       