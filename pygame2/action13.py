#                                      Game Over
# :- iss hum gameover kar ne wale hai jhab enemy hare humse takraye ga to game over ho jaye ga,...
#    iss or hum gameover ki image bhi laga ye ghe ...
# Game over ke iss hum game over hone par text bhi laga sakte hai or background bhi
#  player_y_velocity -= 0.1 
#  :- jab bhi gameover ho jaye hamara player upper y axis se jaye ga..




import pygame
import random
import math

pygame.mixer.init() # .. music ke liye import kiya jata hai
pygame.init() 

screen_widh = 950
screen_hight = 600

#Creting Logo And Color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dark_green = (0, 200, 0)

# fps 
clock = pygame.time.Clock()
fps = 60

#Creating for window
gameWindow = pygame.display.set_mode((screen_widh, screen_hight))
pygame.display.set_caption("Py Sam")

logo = pygame.image.load("logo_pygame.png")
pygame.display.set_icon(logo)

# ADDING BACKGROUND IMAGE
background = pygame.image.load('background3.jpg') 
background = pygame.transform.scale(background, (screen_widh, screen_hight)).convert_alpha()

# ADDIING GACKFGROUND MUSICS 
pygame.mixer.music.load("backgroundMusic.mp3")
pygame.mixer.music.play()
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
    enemy_x_velocity.append(2.5)
    enemy_y_velocity.append(30)

# BULLET image 
bullet_image = pygame.image.load('bulletsmall.png')
bullet_x = 0
bullet_y = 500
# bullet moment velocity
bullet_x_velocity = 0
bullet_y_velocity = 10
bullet_state = "ready"

# image moment velocity 
player_x_velocity = 0
player_y_velocity = 0

# score in GameWindow
score = 0
font = pygame.font.SysFont(None, 60)

# if check the high score file exits

with open("highscore.txt", "w") as g:
    g.write("5")

with open("highscore.txt", "r") as f:
    hiscore = f.read()

# Game Over backround
over_background = pygame.image.load('gameover.jpg') 
font2 = pygame.font.SysFont(None, 90) # gameover

#         Or 

# GameOver text Function
over_font = pygame.font.Font("freesansbold.ttf", 80)

def game_over_text():
    gameover = font.render("Game Over.... ", True, white)
    gameWindow.blit(gameover, (200, 250))

def game_over_text2(text, color, x, y):
    text_screen = font2.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])

def show_score(text, color, x, y):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])
    
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
                player_x_velocity = 5
                player_y_velocity = 0

            if event.key == pygame.K_RETURN:
                if bullet_state is "ready":
                    bullet_x = player_x
                    bullet_fire(bullet_x, bullet_y) 

            if event.key == pygame.K_a:
                player_x_velocity = -5
                player_y_velocity = 0
            if event.key == pygame.K_w:
                player_y_velocity = -5
                player_x_velocity = 0
            if event.key == pygame.K_s:
                player_y_velocity = 5
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
        # Game Over
        if enemy_y[i] > 450:
            for j in range(no_of_enemy):
                enemy_y[j] = 2000
            gameWindow.blit(over_background, (0, 0))  # text or backgrond
            game_over_text2(" "+ str(score), white, 600,475)
            player_y_velocity -= 0.1

            break
            
         

        enemy_x[i] += enemy_x_velocity[i]    
        if enemy_x[i] <= 0:
            enemy_x_velocity[i] = 2.5
            enemy_y[i] += enemy_y_velocity[i]
        elif enemy_x[i] >= 890:
            enemy_x_velocity[i] = -2.5
            enemy_y[i] += enemy_y_velocity[i]
        # collision ke bare me
        collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_sound = pygame.mixer.Sound("bullet_fire.wav")
            bullet_sound.play()
            bullet_y = 550
            bullet_state = "ready"
            score += 1
        
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
    
    if score > int(hiscore):
        hiscore = score

    show_score(" "+ str(score), white, 120, 20) # score ke liye hai
    show_score(" "+ str(hiscore), white, 540, 18) # hiscore ke liye hai
    player()
    clock.tick(fps)
    
    pygame.display.update()

pygame.quit()
quit()