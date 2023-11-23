import pygame , sys

pygame.init()
# variable
size_x = 800
size_y = 600
yellow = (255,255,0)
white = (255,255,255)
green = (0,255,0)

# =================================================
# fonts  -> avardan temam font haye nasb shode dar windows 
# fonts = pygame.font.get()
# print(fonts,len(fonts))

# ==================================================================



# define screen
win = pygame.display.set_mode((size_x,size_y))
# title
pygame.display.set_caption('Font')

# font = pygame.font.Font(font name,size,)
font = pygame.font.Font('ds_digital.TTF',50)
text = 'Sajjad Ansaryan'
# format neveshatan dar pygame
# t_s = font.render(text,True/False,color,bgcolor) # True --> labe saf , False --> lebe saf nist
t_s = font.render(text,True,yellow,green) 
win.blit(t_s,(300,400))


# function for main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


main()
