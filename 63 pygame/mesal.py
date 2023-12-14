import pygame , sys
from tkinter import colorchooser


pygame.init()
siz_x = 1000
siz_y = 800

win = pygame.display.set_mode((siz_x,siz_y),flags=pygame.SHOWN)
pygame.display.set_caption('Draw')

# functions for draw rectagle
def draw_rect():
    x = int(input('insert x for rect:'))
    y = int(input('insert x for rect:'))
    w  = int(input('insert width for rect:'))
    h = int(input('insert height for rect:'))
    color = colorchooser.askcolor(title='color')[0]
    pygame.draw.rect(win,color,(x,y,w,h))
# functions for draw circle
def draw_circle():
    x = int(input('insert x for rect:'))
    y = int(input('insert x for rect:'))
    rad  = int(input('insert width for radius:'))

    color = colorchooser.askcolor(title='color')[0]
    pygame.draw.circle(win,color,(x,y),rad)
# functions for draw line


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            if event.unicode == 'r':
                draw_rect()
                pygame.display.update()
            if event.unicode == 'l':
                pass
            if event.unicode == 'c':
                draw_circle()
    pygame.display.flip()