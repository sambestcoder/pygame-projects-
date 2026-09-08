import pygame
import random
import os 

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
light_blue = (0, 255, 255)
yellow = (255, 255, 0)
small_balck = (30, 27, 30)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
# BackGround image 
image = pygame.image.load("game_image.jpg")
image = pygame.transform.scale(image, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Sam_snake")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)  # score ki paint karna hai to style or size
font2 = pygame.font.SysFont(None, 70)  # score ki paint karna hai to style or size

def text_screen2(text, color, x, y):
    screen_text = font2.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(small_balck)
        text_screen2("Welcome to SAM Game", white, 200, 210)
        text_screen2("Press To SpaceBar and Play", white, 150, 270)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game  = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('backGroundSong.mp3')
                    pygame.mixer.music.play()
                    gameLoop()
                    
        
        pygame.display.update()
        clock.tick(60)
    

# Game Loop

# Games variables
def gameLoop():
    pygame.mixer.music.load('backGroundSong.mp3')
    pygame.mixer.music.play()
    
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55

    velocity_x = 0
    velocity_y = 0

    food_position = 400
    food_x = random.randint(20, food_position)
    food_y = random.randint(20, food_position)

    init_velocity = 5
    snake_size = 30
    fps = 60
    score = 0   # game ka score
    
    #snake ko badha ne ke liye
    snk_list = []
    snk_length = 1 

    # check high scorce file exits 
    if(not os.path.exists("highscorce.txt")):
        with open("highscorce.txt", "w") as g:
            g.write("0")

    with open("highscorce.txt", "r") as f:
        hiscore = f.read()


    while not exit_game:
        if game_over:
            with open("highscorce.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(green)
            text_screen('''Game Over SAM...  ''', black, 270, 300)
            text_screen('''    please Enter Button''', black, 200, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop() # game_loop ke jaga par welcome() function ko call
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_d:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_a:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_w:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_s:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_0:
                        score = 0
                        hiscore = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                score +=10
                food_x = random.randint(20, food_position)
                food_y = random.randint(20, food_position)
                snk_length += 20
                
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(light_blue)
            gameWindow.blit(image, (0, 0))
            text_screen("Score: " + str(score)+"  Hiscore : "+str(hiscore), white, 4, 4)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
                

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('snake_out.wav')
                pygame.mixer.music.play()

            if head in snk_list[: -1]:
                game_over = True
                pygame.mixer.music.load('snake_out.wav')
                pygame.mixer.music.play()
                

            #pygame.draw.rect(gameWindow, red, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, blue, snk_list, snake_size)
            pygame.draw.rect(gameWindow, yellow, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
