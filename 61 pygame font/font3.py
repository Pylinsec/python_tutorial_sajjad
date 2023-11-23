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

text = 'sajjad'
font = pygame.font.Font(None,100)
# # revesh avval
# t_s = font.render(text,True,yellow,green) # t__> text , s --> surface
# win.blit(t_s,(300,300))

# revesh dovvom
t_s = font.render(text,True,yellow,green) # t__> text , s --> surface
t_r = t_s.get_rect(win,white,(400,400,100,100)) # --> TEXT RECTANGLE
t_r.center = (500,500)
win.blit(t_s,t_r)



# function for main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


main()
