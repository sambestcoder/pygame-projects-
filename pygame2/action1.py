import pygame
pygame.init()

screen_widh = 900
screen_hight = 600

#  Creating for window
gameWindow = pygame.display.set_mode((screen_widh, screen_hight))
pygame.display.set_caption("Py Sam")

#  gameLoop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



