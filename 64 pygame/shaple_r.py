import pygame , sys

# variables
size = (1000,800)
blue_sky = (135, 206,235)
title = 'Havij'
yellow = (255,255,0)
lgreen = (144,238,144)
c = (103,53,169)
pi = 57
angle1 = 0
angle2 = 90/57

# display
win = pygame.display.set_mode(size)
win.fill(blue_sky)
# title
# shape rectangle
pygame.display.set_caption(title)
pygame.draw.rect(win,yellow,(0,0,1000,800),10)
pygame.draw.rect(win,lgreen,(10,10,980,780),10)

# circle
# pygame.draw.circle(win,c,(500,500),80,5)
# # ellipse
# pygame.draw.ellipse(win,c,(600,600,50,80),10)
# # polygon
# pygame.draw.polygon(win,c,((10,20),(50,100),(400,450),(500,900)))
# line
# pygame.draw.aaline(win,c,(100,200),(400,450),10)
# pygame.draw.aalines(win,yellow,True,((200,300),(500,550),(700,200)),10)
# arc
pygame.draw.arc(win,(255,0,0),(300,300,300,200),0,90/57,5)
pygame.draw.arc(win,(0,255,0),(300,300,300,200),90/57,180/57,5)
pygame.draw.arc(win,(0,0,255),(300,300,300,200),180/57,270/57,5)
pygame.draw.arc(win,(255,0,255),(300,300,300,200),270/57,360/57,5)
# main loop , solutin 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit90
    pygame.display.update() 

