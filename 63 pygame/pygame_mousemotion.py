import pygame , sys 
from tkinter import colorchooser
pygame.init()
siz_x = 800
siz_y = 700

win = pygame.display.set_mode((siz_x,siz_y))
pygame.display.set_caption('key logger')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # mousebuttondown
        elif event.type == pygame.MOUSEMOTION:
            # draw circle with left click
            # if event.buttons == (1,0,0):
            x = event.pos[0]
            y = event.pos[1]
            color = (255,255,0)
            win.fill((0,0,0))
            pygame.draw.circle(win,color,(x,y),50)
            pygame.display.update()
            if event.buttons == (0,0,1):
                color = (255,0,255)
                x = event.pos[0]
                y = event.pos[1]
                pygame.draw.circle(win,color,(x,y),50)
            if event.buttons == (0,1,0):
                color = colorchooser.askcolor()[0]
                x = event.pos[0]
                y = event.pos[1]
                pygame.draw.circle(win,color,(x,y),50)

    pygame.display.update()
