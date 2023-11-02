import pygame , sys , random


# define variables 
size_w = 1000
size_h = 800
sky_blue = (135, 206, 235)
white= (255,255,255)
circle_w = 200
circle_h = 0
clock = pygame.time.Clock() # tarif time jehat kontrol harakt 
time_speed = 30
# make screen
screen = pygame.display.set_mode((size_w,size_h))
pygame.display.set_caption('Snow Fall')
screen.fill(sky_blue)


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(time_speed)
    screen.fill(sky_blue)
    pygame.draw.circle(screen,white,(circle_w,circle_h),8) 
    if circle_h > size_h:
        circle_h = 0
    else:    
        circle_h += 10

    pygame.display.update()        
