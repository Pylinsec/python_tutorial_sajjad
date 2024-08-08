import pygame , sys

# tarif andaze screen
size = (500,500)
win = pygame.display.set_mode(size)
# caption --> title
pygame.display.set_caption('review')

# color
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
win.fill(green)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()        