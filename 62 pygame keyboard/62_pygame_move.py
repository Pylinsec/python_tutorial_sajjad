import pygame , sys 
pygame.init()
# variables
size_x = 1200
size_y = 800
red = (255,0,0)
black = (0,0,0)
rect_x = 400
rect_y = 300

# screen
win = pygame.display.set_mode((size_x,size_y))

# give title for window
pygame.display.set_caption('Working with Keys')



# main function
def main(rect_x,rect_y):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # hasas be feshordan kelid rooye keyboard 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if rect_x < -60:
                        rect_x = 1130
                    else:    
                        rect_x -= 30
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if rect_x > 1130:
                        rect_x = 0
                    else:    
                        rect_x += 30
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if rect_y < -60:
                        rect_y = 720
                    else:    
                        rect_y -= 30
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if rect_y > 730:
                        rect_y = 0
                    else:    
                        rect_y += 30


        win.fill('black')            
        pygame.draw.rect(win,red,(rect_x,rect_y,70,70))
        pygame.display.update()        


main(rect_x,rect_y)