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
img_bg = pygame.image.load('photo/fire_bg.png')
new_img_bg = pygame.transform.scale(img_bg,(1200,800))
# gherar dadan aks dakhel win
win.blit(new_img_bg,(img_x,img_y))

pic2 = pygame.image.load('photo/icon.jpg')
new_pic2 = pygame.transform.scale(pic2,(200,200))
win.blit(new_pic2,(400,500))

# make main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    clock.tick(50)        
    pygame.display.update()        