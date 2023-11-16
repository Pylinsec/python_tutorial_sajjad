import pygame ,sys

# variables
size_w = 1200
size_h = 800
img_x = 0
img_y = 0
# clock
clock = pygame.time.Clock()



# make screen
win = pygame.display.set_mode((size_w,size_h))
# title for screen
pygame.display.set_caption('Place background')
# load photo for icon
ico = pygame.image.load('photo/tree.jpg')
pygame.display.set_icon(ico)
# load image for background
img_bg = pygame.image.load('photo/blackhorse.jpg')
new_img_bg = pygame.transform.scale(img_bg,(2400,800))
# gherar dadan aks dakhel win
win.blit(new_img_bg,(img_x,img_y))

# make main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if img_x != -1000:        
        img_x -= 10 
        win.fill((0,0,0))
        win.blit(new_img_bg,(img_x,img_y)) 
    else:
        img_x = 0  
        win.blit(new_img_bg,(img_x,img_y))         
    clock.tick(50)        
    pygame.display.update()        