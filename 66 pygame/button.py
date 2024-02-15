# modules
import sys , pygame 

pygame.init()

# variables
size = (1200,800)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
white =(255,255,255)
rect_x = 600
rect_y = 300
text_x = 610
text_y = 320
text = 'Click Me'
# display
win = pygame.display.set_mode(size)

# title
pygame.display.set_caption('make button')
pygame.draw.rect(win,blue,(rect_x,rect_y,300,120))  

# functions
def change():
    text = 'Done ....'
    t_s = font.render(text,True,(189,124,89))
    win.fill(white)
    pygame.draw.rect(win,yellow,(rect_x,rect_y,300,120))  
    win.blit(t_s,(text_x,text_y))

# text
font = pygame.font.Font(None,100)   
t_s = font.render(text,True,red)
win.blit(t_s,(text_x,text_y))


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(600,900) and event.pos[1] in range(300,420):
                change()
    pygame.display.update() 
        

           
