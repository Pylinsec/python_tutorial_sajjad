import sys , pygame 

pygame.init()
# variables
size = (1000,800)
red = (255,0,0)
points = []
# display
win = pygame.display.set_mode(size)
# title
pygame.display.set_caption('keys and mouse')

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            points.append(event.pos) 
            if len(points) >= 2: 
                pygame.draw.lines(win,red,False,points,2)
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print(event)    
        # if event.type == pygame.MOUSEMOTION:
        #     print(event)    
    pygame.display.update()        

