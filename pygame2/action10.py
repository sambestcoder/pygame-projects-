
# issme hum multiple enemy game dale ghe .... random module se ....
#    multiple enemy ko banane ke liye append function ka use karna honga ...
#    enemy_image or enemy_moment ko sare append kar diya ki nayi value pass ho sake
#     border of game by enemy ko bhi hum ne [i] laga diya hai kyu ki jo multiple enemy ke varibles 
#     banaye the ho use na ho sake...



import pygame
import random
import math

pygame.init() 

screen_widh = 950
screen_hight = 600
fps = 60 
score = 0

#Creting Logo And Color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dark_green = (0, 200, 0)

#Creating for window
gameWindow = pygame.display.set_mode((screen_widh, screen_hight))
pygame.display.set_caption("Py Sam")

logo = pygame.image.load("logo_pygame.png")
pygame.display.set_icon(logo)

# ADDING BACKGROUND IMAGE
background = pygame.image.load('background.jpg') 
background = pygame.transform.scale(background, (screen_widh, screen_hight)).convert_alpha()

# player image in blackground 
player_x = 400
player_y = 500
player_image = pygame.image.load("aircraft.png")

# multiple enemy 
enemy_image = []
enemy_x = []
enemy_y = []
enemy_x_velocity = []
enemy_y_velocity = []
no_of_enemy = 6

for i in range(6):
    # ENEMY image 
    enemy_image.append(pygame.image.load("enemy2.png"))
    enemy_x.append(random.randint(0, 800))
    enemy_y.append(random.randint(0, 400))
    # enemy moment velocity
    enemy_x_velocity.append(0.3)
    enemy_y_velocity.append(30)

# BULLET image 
bullet_image = pygame.image.load('bulletsmall.png')
bullet_x = 0
bullet_y = 500
# bullet moment velocity
bullet_x_velocity = 0
bullet_y_velocity = 1.2

bullet_state = "ready"

# image moment velocity 
player_x_velocity = 0
player_y_velocity = 0

def player():
    gameWindow.blit(player_image, [player_x, player_y])

def enemy(x, y, i):
    gameWindow.blit(enemy_image[i], (x, y))

def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    gameWindow.blit(bullet_image, (x+16, y+10))

def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    # by using distance formula 
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        False


#  gameLoop
running = True
while running:

    # background image adding 
    gameWindow.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player_x_velocity = 0.5
                player_y_velocity = 0

            if event.key == pygame.K_RETURN:
                if bullet_state is "ready":
                    bullet_x = player_x
                    bullet_fire(bullet_x, bullet_y) 

            if event.key == pygame.K_a:
                player_x_velocity = -0.5
                player_y_velocity = 0
            if event.key == pygame.K_w:
                player_y_velocity = -0.3
                player_x_velocity = 0
            if event.key == pygame.K_s:
                player_y_velocity = 0.3
                player_x_velocity = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                player_x_velocity = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_y_velocity = 0
                
    

    player_x += player_x_velocity
    player_y += player_y_velocity 
# boarder of the game by player_x
    if player_x <= 0:
        player_x = 0
    elif player_x >= 890:
        player_x = 890

# boarder of the game by enemy_x
    for i in range(no_of_enemy):  
        enemy_x[i] += enemy_x_velocity[i]    
        if enemy_x[i] <= 0:
            enemy_x_velocity[i] = 0.3
            enemy_y[i] += enemy_y_velocity[i]
        elif enemy_x[i] >= 890:
            enemy_x_velocity[i] = -0.3
            enemy_y[i] += enemy_y_velocity[i]
        # collision ke bare me
        collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 550
            bullet_state = "ready"
            score += 1
            print(score) 
        
            enemy_x[i] = random.randint(0, 800)
            enemy_y[i] = random.randint(50, 150)
        enemy(enemy_x[i], enemy_y[i], i)

# bullet Movement .... 
    if bullet_state is "fire":
        bullet_fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_velocity

    if bullet_y <= 0:
        bullet_y = 500
        bullet_state = "ready"

    

    player()
    
    pygame.display.update()