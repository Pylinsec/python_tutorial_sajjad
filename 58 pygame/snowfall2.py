import pygame , sys , random


# define variables 
size_w = 1800
size_h = 1000
sky_blue = (135, 206, 235)
white= (255,255,255)
circle_w = random.randrange(1,size_h)
circle_h = 0

clock = pygame.time.Clock() # tarif time jehat kontrol harakt 
time_speed = 30
snow_list = []
# make screen
screen = pygame.display.set_mode((size_w,size_h))
pygame.display.set_caption('Snow Fall')
screen.fill(sky_blue)

# define function for making list
def make_snow_list():
    for i in range(70):
        x = random.randrange(size_w)
        y = 0
        z = random.randrange(3,8)
        snow_list.append([x,y,z])
       

make_snow_list()
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(time_speed)
    screen.fill(sky_blue)
    for snow in snow_list:
        if snow[1] > size_h:
            snow[1] = 0
            snow[0] = random.randrange(1,size_h)
        else:    
            snow[1] += 1
    pygame.draw.circle(screen,white,(snow[0],snow[1]),snow[2]) 

    pygame.display.update()        
