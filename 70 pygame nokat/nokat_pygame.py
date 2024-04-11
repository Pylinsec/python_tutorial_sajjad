import pygame 

# Initialize pygame
pygame.init()

# Set display surface 
window_w = 800
window_h = 600
window_size = (window_w,window_h)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake Game")
window.fill('#FFFFFF')

# Set Fps and Clock
fps = 20
clock = pygame.time.Clock()

# Colors
green = (0,255,0)
dark_green = (0,40,0)
red = (255,0,0)

# Set values
# Set Font
font = pygame.font.Font('Gabriola.ttf',50)
# font = pygame.font.SysFont()

# Set text
title_text = font.render('~~Snake~~',True,green,dark_green)
# window.blit(title_text,(40,499))
title_rect = title_text.get_rect() # top ,bottom,left, right , ...
title_rect.center = (window_w // 2 , window_h // 2)
# print(title_text)

#Set Rectangle 
rect = pygame.draw.rect(window,green,(200,300,100,150))
# print(rect.topleft)

circle = pygame.draw.circle(window,red,(500,200),50)

ellipse  = pygame.draw.ellipse(window,red,(300,400,100,200),3)
print(ellipse)
# Set image
# Set music
#









# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.blit(title_text,title_rect)
    pygame.display.update()        

# Exit from Pygame
pygame.quit()
