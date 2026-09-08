
# game screen me image show karni badhe ghi .... 
# plsyer_x and player_y is the direction of the image.. ki blackground me image kaha par honi chahiye..


import pygame
pygame.init()

screen_widh = 900
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


def player():
    gameWindow.blit(player_image, [player_x, player_y])

#  gameLoop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gameWindow.fill(dark_green)
    player()
    pygame.display.update()
