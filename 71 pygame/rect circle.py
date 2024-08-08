import pygame , sys , random

# tarif andaze screen
size = (1000,800)
win = pygame.display.set_mode(size)
# caption --> title
pygame.display.set_caption('review')

# color
black = (0,0,0)
white = (255,255,255)
green = (0,55,0)
yellow = (255,255,0)
win.fill(green)
# variable
location = []


# rect
# pygame.draw.rect(surface,color,(location,size),width)


for i in range(100):
    location.append((random.randrange(0,1000),random.randrange(0,800),random.randrange(10,30)))
print(location)    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for loc in location:
        pygame.draw.rect(win,yellow,(loc[0],loc[1],loc[2],loc[2]))
        pygame.time.delay(100)
        pygame.display.update()        
