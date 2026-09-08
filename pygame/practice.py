import pygame

# Game color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
light_blue = (0, 255, 255)
yellow = (255, 255, 0)


# creating gamewindow
game_widh = 900
game_height = 500
gameWindow = pygame.display.set_mode((game_widh, game_height))
pygame.display.set_caption("samrat")
pygame.display.update()

# spaefic varibles

exit_game = False
over_game = False
snake_x = 45
snake_y = 55
snake_size = 10

clock = pygame.time.Clock()
fps = 30
# Game Loop

while not exit_game:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit_game = True

    gameWindow.fill(red)
    pygame.draw.rect(gameWindow, yellow, [snake_x, snake_y, snake_size, snake_size])
    clock.tick(fps)
    pygame.display.update()

pygame.quit()
quit()