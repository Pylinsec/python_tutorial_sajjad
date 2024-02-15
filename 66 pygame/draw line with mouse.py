import sys , pygame 

pygame.init()
# variables
size = (1000,800)
red = (255,0,0)
black = (0,0,0)
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(event.pos)
            if event.button == 3:
                if len(points) > 1:
                    points.pop()
                    win.fill(black)
                    pygame.display.update()
                        
        if event.type == pygame.MOUSEMOTION:
            if len(points) >=2:
                points[-1] = event.pos
        if len(points) >=2:
            win.fill(black)            
            pygame.draw.lines(win,red,False,(points),2)
            pygame.display.update() 
        

           
