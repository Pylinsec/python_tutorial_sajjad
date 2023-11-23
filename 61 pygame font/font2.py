import pygame , sys

pygame.init()
# variable
size_x = 800
size_y = 600
yellow = (255,255,0)
white = (255,255,255)
green = (0,255,0)




# define screen
win = pygame.display.set_mode((size_x,size_y))
# title
pygame.display.set_caption('Font')


font = pygame.font.Font(None,1000)
text = '.'
t_s = font.render(text,True,yellow) 
win.blit(t_s,(400,100))

font1 = pygame.font.Font(None,1000)
text = '.'
t_s = font1.render(text,False,yellow) 
win.blit(t_s,(100,100))


# function for main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


main()
