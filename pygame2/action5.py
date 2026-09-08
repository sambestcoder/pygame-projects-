
#(1) CREAT BOARDER... 
# hum game me left ya right side me boarder laga sakte hai ... 
# player_x ke displacement me condition lagayi ...  

#(2) Create enemy in the game 
# issme hum enemy dal ne wale hai ...

import pygame
pygame.init() # inlization of pyagame


screen_widh = 950
screen_hight = 600

# Creting Logo And Color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dark_green = (0, 200, 0)

#  Creating for window
gameWindow = pygame.display.set_mode((screen_widh, screen_hight))
pygame.display.set_caption("Py Sam")

logo = pygame.image.load("logo_pygame.png")
pygame.display.set_icon(logo)


# player image in blackground 

player_x = 400
player_y = 500
player_image = pygame.image.load("aircraft.png")

# ENEMY image 
enemy_image = pygame.image.load("enemy2.png")
enemy_x = 420
enemy_y = 90
enemy_velocity = 0

# image moment velocity 
player_x_velocity = 0
player_y_velocity = 0




def player():
    gameWindow.blit(player_image, [player_x, player_y])

def enemy():
    gameWindow.blit(enemy_image, [enemy_x, enemy_y])

#  gameLoop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_velocity = 0.3
                player_y_velocity = 0
            if event.key == pygame.K_LEFT:
                player_x_velocity = -0.3
                player_y_velocity = 0
            if event.key == pygame.K_UP:
                player_y_velocity = -0.3
                player_x_velocity = 0
            if event.key == pygame.K_DOWN:
                player_y_velocity = 0.3
                player_x_velocity = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_x_velocity = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_velocity = 0
                

    player_x += player_x_velocity
    player_y += player_y_velocity 

# boarder of the game by player_x

    if player_x <= 0:
        player_x = 0
    if player_x >= 890:
        player_x = 890

    gameWindow.fill(dark_green)
    player()
    enemy()
    pygame.display.update()
