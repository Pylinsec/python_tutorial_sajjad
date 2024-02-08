import sys , pygame 

pygame.init()
# variables
size = (1000,800)
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
    pygame.display.update()        

