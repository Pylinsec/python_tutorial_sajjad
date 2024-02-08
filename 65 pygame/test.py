import sys , pygame 

pygame.init()
# variables
size = (1000,800)
red = (255,0,0)
points = [(100,200)]
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
            
            win.fill((0,0,0))
            points.insert(len(points),event.pos) 
            pygame.draw.lines(win,red,False,(points),2)
            pygame.display.update()
        

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     points.append(event.pos) 
        #     if len(points) >= 2: 
        #         pygame.draw.lines(win,red,False,points,2)
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print(event)    
        # if event.type == pygame.MOUSEMOTION:
        #     print(event)    
    pygame.display.update()        
