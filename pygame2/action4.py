
# IMAGE ko moment karane wale hai matlab 
# left Right or up down 
# if event.type == pygame.KEYUP:
#           if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
#               player_x_velocity = 0
# :- isska matlab hai ki agar mene right key tabaya or player right me ja raha hai tab mene or dusra
#    dusara key tabaya to player stop ho jaye ga.. 
#    iss me faayda ye bhi hai ki right or left button taba ke rakhne se moment hota rahen ga.. 
#  keyup ye event ka type hai 
#     iss me mene up and down ka bhi condition laga diya hai .... same moment honga...
#     player staright line me up or down and right or lift hona ke liye hum jaha par velocity_x hai
#      :-  vaha par velovity_y ko zero kardo ghe.. 

                
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

# image moment velocity 
player_x_velocity = 0
player_y_velocity = 0

player_image = pygame.image.load("aircraft.png")


def player():
    gameWindow.blit(player_image, [player_x, player_y])

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

    gameWindow.fill(dark_green)
    player()
    pygame.display.update()
