import pygame , sys , random

# tarif andaze screen
size = (1000,800)
win = pygame.display.set_mode(size)
# caption --> title
pygame.display.set_caption('circle')

# color
black = (0,0,0)
white = (255,255,255)
green = (0,55,0)
yellow = (255,255,0)
red = (255,0,0)
blue = (0,0,255)
win.fill(green)
# variable
location = []
color_list = (red,yellow,blue,'#D77ED7','#1FCAD7','#95339E',black,white)


# rect
# pygame.draw.rect(surface,color,(location),radius,width)


for i in range(150):
    location.append((random.randrange(30,960),random.randrange(30,760),random.randrange(5,15)))
print(location)    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for loc in location:
#         index = location.index(loc)
        color = random.randrange(0,8)
#         color = index % 3
        pygame.draw.circle(win,color_list[color],(loc[0],loc[1]),loc[2])
        pygame.time.delay(50)
        pygame.display.update()        

