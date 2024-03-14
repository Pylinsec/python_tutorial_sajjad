# modules
import sys , pygame , random

pygame.init()

# variables
size = (1200,800)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
player_x = random.randint(0,1140)
player_y = 700
step = 20
enemy_list = []
clock = pygame.time.Clock()
fps = 60
score = 0
score_font = pygame.font.Font(None,60)



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

def level(score , fps):
    if score < 20:
        fps = 25
    elif score < 30:
        fps = 30
    elif score < 40:
        fps = 40
    elif score < 100:
        fps = 50
    return fps    

ee_y = 0
def draw_enemy():
     for enemy in enemy_list:
        pygame.draw.rect(win,red,(enemy[0],enemy[1],60,60)) 

def move_enemy():
    global score
    for e in enemy_list:
        if e[1] in range(800):
            e[1] += 10
        else:
            score += 1
            index = enemy_list.index(e)    
            enemy_list.pop(index)

# function for hit check            
def collison():
    global flag
    for enemy in enemy_list:
        e_x = enemy[0]
        e_y = enemy[1]
        p_x = player_x
        p_y = player_y
        if p_x in range(e_x,e_x + 60) and p_y in range(e_y , e_y + 60) or \
        p_x + 60 in range(e_x,e_x + 60) and p_y + 60 in range(e_y,e_y + 60):
            flag = False
           

            
# function start
def start():
    for i in range(3,0,-1):
        win.fill(black)
        count_font = pygame.font.Font(None,500)
        count_l = count_font.render(str(i),True,blue)
        win.blit(count_l,(480,250))
        pygame.display.update()
        pygame.time.delay(1000)

    win.fill(black)
    go_font = pygame.font.Font(None,500)
    go_text = go_font.render('GO',True,blue)
    win.blit(go_text,(400,200))
    pygame.display.update()
    pygame.time.delay(1000)

        

# main loop
flag = True
while flag:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    press_key = pygame.key.get_pressed()
    if press_key[pygame.K_s]:
        start()
    if press_key[pygame.K_RIGHT]:
        player_x += step
    if press_key[pygame.K_LEFT]:
        player_x -= step
    # if press_key[pygame.K_DOWN]:
    #     player_y += step
    # if press_key[pygame.K_UP]:
    #     player_y -= step

    
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
    collison()
    score_text = score_font.render(f"score:{score}", True,green) 
    win.blit(score_text,(30,30))
    fps = level(score,fps)
    clock.tick(fps)
    pygame.display.update() 
        

           
