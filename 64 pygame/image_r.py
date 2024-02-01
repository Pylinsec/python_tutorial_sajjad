import pygame , sys

# variables
size = (1200,800)
green = (0,255,0)
title = 'Football'



# display
win = pygame.display.set_mode(size)
# win.fill(green)
# title
pygame.display.set_caption(title)
# icon
ball = pygame.image.load('object.png')
pygame.display.set_icon(ball)

# image
bg = pygame.image.load('field.jpg')
BG = pygame.transform.scale(bg,(1200,800))
win.blit(BG,(0,0))

win.blit(ball,(700,300))
# main loop , solutin 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    pygame.display.flip()        