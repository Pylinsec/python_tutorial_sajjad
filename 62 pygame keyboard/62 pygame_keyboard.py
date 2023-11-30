import pygame , sys 
pygame.init()
# variables
size_x = 1200
size_y = 800


# screen
win = pygame.display.set_mode((size_x,size_y))
# give title for window
pygame.display.set_caption('Working with Keys')



# main function
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # hasas be feshordan kelid rooye keyboard 
            elif event.type == pygame.KEYDOWN:
                print(event)
                # unicode = heman khode karakter hast
                print(event.unicode)
                print(event.key)
                # print(type(event))
                # <Event(768-KeyDown {'unicode': 'a', 'key': 97, 'mod': 4096, 'scancode': 4, 'window': None})>

        pygame.display.update()        


main()