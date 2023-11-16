import pygame ,sys

# variables
size_w = 800
size_h = 800



# make screen
win = pygame.display.set_mode((size_w,size_h))
# title for screen
pygame.display.set_caption('Place icon')
# load photo for icon
# pygame.image.load(path)
# ico = pygame.image.load('icon.jpg')
ico = pygame.image.load('tree.jpg')
# ico = pygame.image.load('icon.png')
# ico = pygame.image.load('icon.bmp')
pygame.display.set_icon(ico)

# make main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()        