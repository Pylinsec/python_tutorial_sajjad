import pygame , sys , time

# variales
size = (800,800)
black = (0,0,0)
yellow = (255,255,0)
red = (255,0,0)
blue= (0,0,255)
green =(0,255,0)
white = (255,255,255)
w = 0
h = 0

# create surface
win = pygame.display.set_mode(size)
# change name of win
pygame.display.set_caption('rectange') # mostetil
# taqir rang display
win.fill(red)

# format --> mostetil --> pygame.draw.rect(surface,color,(location,size),width) #



# main loop
pygame.draw.rect(win,yellow,(w,h,80,80),0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill(red)     
    w += 20
    h += 20
    pygame.draw.rect(win,yellow,(w,h,80,80),0)  
    pygame.display.update()  # ya pygame.display.flip()
    time.sleep(0.4) 
          
