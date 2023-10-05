import pygame ,sys
# define variable
size = (500,500) #(width,height) ya (tool, arz)
size_list = [500,500]
# sakht display ya surface 
win = pygame.display.set_mode(size_list) # mitonim az list ya tuple estefadeh konim
pygame.display.set_caption('FirstGame')
# revesh negah dashtan win rooye screen 
# rahehal avval
while True:
    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()        

