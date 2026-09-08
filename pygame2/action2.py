
import pygame
pygame.init()

screen_widh = 900
screen_hight = 600

#  Creating for window
gameWindow = pygame.display.set_mode((screen_widh, screen_hight))
pygame.display.set_caption("Py Sam")

# Creting Logo And Color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dark_green = (0, 150, 0)

logo = pygame.image.load("logo_pygame.png")
pygame.display.set_icon(logo)
#  gameLoop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gameWindow.fill(dark_green)
    pygame.display.update()
