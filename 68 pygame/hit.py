import pygame , sys


pygame.init()
# variables 
size = (800,600)
blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)
p_x = 400
p_y = 540
e_x = 400
e_y = 0

win = pygame.display.set_mode(size)


# main loop
flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            # pygame.quit()
            # sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         print('sajjad')  
    press = pygame.key.get_pressed()
    # taggir mekan
    if press[pygame.K_LEFT]:
        p_x -= 10
    if press[pygame.K_RIGHT]:
        p_x += 10

    # moshakhas kardan hodood beraye player
    if p_x < 0:
        p_x = 740
    if p_x > 800:
        p_x = 0             
    # moshakhas kardan hodood beraye enemy
    if e_y > 540:
        e_y = 0
    else:
        e_y += 10    
           
    # hit ba fekr be player 
    if p_x in range(e_x,e_x + 60) and p_y in range(e_y , e_y + 60):
        pygame.time.delay(1000)
    if p_x + 60 in range(e_x,e_x + 60) and p_y in range(e_y , e_y + 60):
        pygame.time.delay(1000)
        
    # # hit ba fekr be enemy
    # if e_x in range(p_x,p_x + 60) and e_y + 59 in range(p_y , p_y + 60):
    #     pygame.time.delay(2000)
    # if e_x + 59 in range(p_x,p_x + 60) and e_y + 59 in range(p_y , p_y + 60):
    #     pygame.time.delay(2000)

    win.fill(black)    
    pygame.draw.rect(win,blue,(p_x,p_y,60,60),4)
    pygame.draw.rect(win,red,(e_x,e_y,60,60),4)
    # bar asas mili sanieh
    pygame.time.delay(40)
pygame.display.update()        