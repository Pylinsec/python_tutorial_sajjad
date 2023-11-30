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
            print(pygame.QUIT)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # hasas be feshordan kelid rooye keyboard 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"you press char {event.unicode}, {event.key}")
                if event.key == pygame.K_b:
                    print(f"you press char {event.unicode}")

        pygame.display.update()        


main()