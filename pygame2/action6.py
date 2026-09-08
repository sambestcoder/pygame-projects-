
# hum enemy ke image ko movement kare ghe 
# or random module ka use karenghe ki enemy hume unlimited mile .. 
# random module ka use issliye karen ghe ki emeny kahi par bhi gameWindow me show kare...
# jab enemy thoda border par lage to thoda niche aaja ye ...
# USS KE liye hume enemy_x_velocity ko badhana honga .... 
# iss condition se enemy niche aara hai :- enemy_y += enemy_y_velocity

import pygame
import random

pygame.init() 

screen_widh = 950
screen_hight = 600
fps = 60 

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
enemy_y_velocity = 40

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
            if event.key == pygame.K_d:
                player_x_velocity = 0.3
                player_y_velocity = 0
            if event.key == pygame.K_a:
                player_x_velocity = -0.3
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


    gameWindow.fill(dark_green)
    player()
    enemy()
    pygame.display.update()
