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
        # elif event.type == pygame.MOUSEBUTTONDOWN:# pos --> position click , button -> 1--> lclick ,2--> scrool click , 3-> rclick,4_-> up scrool ,5--> down scrool 
        #     print(event)
            # mouse buttondown
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     print(event)
        # mouse motion
        elif event.type == pygame.MOUSEMOTION:
            # pos --> position x,y click
            # rel --> relative dar kodam jehat harekat karde 
            # buttons --> tuple (leftclick,scrol,rightclick) --. kodam negah dashtim 
            print(event)
            
