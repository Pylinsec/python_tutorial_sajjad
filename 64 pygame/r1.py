import pygame , sys

# variables
size = (800,600)
green = (0,255,0)
title = 'Havij'



# display
win = pygame.display.set_mode(size)
# win.fill(green)
# title
pygame.display.set_caption(title)


# main loop , solutin 1
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit90
#     pygame.display.update() 

# solution 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    pygame.display.flip()        