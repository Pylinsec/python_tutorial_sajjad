import pygame , sys 

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = event.pos[0]
                y = event.pos[1]
                pygame.draw.circle(win,(255,255,0),(x,y),50)
        # draw rectagle 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                x = event.pos[0]
                y = event.pos[1]
                pygame.draw.rect(win,(255,255,0),(x,y,100,120))
    pygame.display.update()

