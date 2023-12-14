import pygame , sys 

pygame.init()
siz_x = 1800
siz_y = 1000
keys = []
win = pygame.display.set_mode((siz_x,siz_y),flags=pygame.HIDDEN)
pygame.display.set_caption('key logger')


with open("key_list.txt",'w') as file: 
                file.write('salam sajjad')  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            # keys.append(event.unicode)
            with open("key_list.txt",'a') as file: 
                print(event.unicode , end="")
                file.write(event.unicode)
                pygame.display.update()
