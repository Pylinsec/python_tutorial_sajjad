import sys , pygame 

pygame.init()
# variables
size = (1000,800)
red = (255,0,0)
text = ''
black =(0,0,0)
# display
win = pygame.display.set_mode(size)
# title
pygame.display.set_caption('keys and mouse')
# text
font = pygame.font.Font(None,60)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     print(event.unicode)    
        if event.type == pygame.KEYDOWN:
            # print(event)
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
                font_s = font.render(text,True,red)
                win.fill(black)
                win.blit(font_s,(50,100)) 
                pygame.display.update()   
            else:    
                text = text + event.unicode
                font_s = font.render(text,True,red)
                win.blit(font_s,(50,100)) 

    
              
    pygame.display.update()        

