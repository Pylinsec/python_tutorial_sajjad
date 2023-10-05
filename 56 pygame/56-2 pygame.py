import pygame
# define variable
size = (500,500) #(width,height) ya (tool, arz)
size_list = [500,500]
# sakht display ya surface 
win = pygame.display.set_mode(size_list) # mitonim az list ya tuple estefadeh konim

# revesh negah dashtan win rooye screen 
# raheha2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
