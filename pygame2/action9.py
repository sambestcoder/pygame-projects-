
# iss me hum bullet jab fire ho rahi hai to ussi time left right kar ke enter press kiya 
#  to bullet player ke sath ho ja rahi hai iss problem ko slove karne ke liye hum 
#  uss condition me badlav karne ghe jisme humne if condition bullet fire ka use kiya tha 
#   :- ye condition laga ye ghe 
#     :- if bullet_state is "ready"
# iss me hum enter button dabaye ghe to  score print honga 
#   iss me hum math module ka use karen ghe .... 
#   iss me hum distance ka formula use karen ghe jo math me hota hai 
#   iss me colusion hai age distance < 27 pixels se less than hua to return karna honga 'TRUE'



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

# ENEMY image 
enemy_image = pygame.image.load("enemy2.png")
enemy_x = random.randint(0, 800)
enemy_y = random.randint(0, 400)
# enemy moment velocity
enemy_x_velocity = 0.3
enemy_y_velocity = 30

# BULLET image 
bullet_image = pygame.image.load('bulletsmall.png')
bullet_x = 0
bullet_y = 500
# bullet moment velocity
bullet_x_velocity = 0
bullet_y_velocity = 1

bullet_state = "ready"

# image moment velocity 
player_x_velocity = 0
player_y_velocity = 0

def player():
    gameWindow.blit(player_image, [player_x, player_y])

def enemy():
    gameWindow.blit(enemy_image, [enemy_x, enemy_y])

def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    gameWindow.blit(bullet_image, (x+16, y+10))

def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
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
                
    enemy_x += enemy_x_velocity

    player_x += player_x_velocity
    player_y += player_y_velocity 
# boarder of the game by player_x
    if player_x <= 0:
        player_x = 0
    elif player_x >= 890:
        player_x = 890

# boarder of the game by enemy_x
    if enemy_x <= 0:
        enemy_x_velocity = 0.3
        enemy_y += enemy_y_velocity
    elif enemy_x >= 890:
        enemy_x_velocity = -0.3
        enemy_y += enemy_y_velocity

# bullet Movement .... 
    if bullet_state is "fire":
        bullet_fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_velocity

    if bullet_y <= 0:
        bullet_y = 500
        bullet_state = "ready"

    # collision ke bare me
    collision = isCollision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 550
        bullet_state = "ready"
        score += 1
        print(score) 

    player()
    enemy()
    pygame.display.update()