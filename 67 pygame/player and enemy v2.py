# modules
import sys , pygame , random

pygame.init()

# variables
size = (1200,800)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
player_x = random.randint(0,1140)
player_y = 700
step = 20
enemy_list = []
clock = pygame.time.Clock()
fps = 60


# display
win = pygame.display.set_mode(size)

# title
pygame.display.set_caption('make button')

# functions
def make_enemy():
     a = random.randint(0,10)
     if len(enemy_list) <= 50 and a == 0:
        e_x = random.randint(0,1140)
        e_y = 0
        enemy_list.append([e_x,e_y])
        # print(enemy_list)

ee_y = 0
def draw_enemy():
     for enemy in enemy_list:
        pygame.draw.rect(win,red,(enemy[0],enemy[1],60,60)) 
    # global ee_y
    # pygame.draw.rect(win,red,(100,ee_y,60,60)) 
    # ee_y += 10
    # pygame.display.update()

def move_enemy():
    for e in enemy_list:
        if e[1] in range(800):
            e[1] += 10
        else:
            index = enemy_list.index(e)    
            enemy_list.pop(index)
            # for index , e in enumerate(enemy_list):
            #     enemy_list.pop(index)


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += step
            if event.key == pygame.K_LEFT:
                    player_x -= step
    
    # check mandan shekl dakhel window                
    if player_x < 0:
        player_x = 1140            
    if player_x > 1150:
        player_x = 0            
    win.fill(black)            
    pygame.draw.rect(win,blue,(player_x,player_y,60,60))   
    # call functions
    make_enemy()    
    draw_enemy() 
    move_enemy()
    clock.tick(20)
    pygame.display.update() 
        

           
