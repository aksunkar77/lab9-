#in this file i will upgrade my code from lab8 main.py
# what i added 
# 1. coin points 1,2,3 based on value
#2. coin speed increases
import pygame
import random
import sys

pygame.init()

# Screen 
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 215, 0)

# images
player_img = pygame.image.load("player_car.png")
player_img = pygame.transform.scale(player_img, (120, 140))

coin_img = pygame.image.load("coin.png")

#  setup
player_rect = player_img.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - 120)
player_speed = 5

# Coin data
coin_rects = [] 
coin_values = []  
coin_timer = 0  
coin_spawn_delay = 60  
coin_speed = 4  
coin_count = 0  

font = pygame.font.SysFont(None, 36)

# spead increases
enemy_speed = 5
speed_increase_threshold = 5  

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed


    coin_timer += 1
    if coin_timer >= coin_spawn_delay:
        # Random coin position and value
        coin_x = random.randint(50, WIDTH - 50)
# coin random values 1 2 3 
        coin_value = random.choice([1, 2, 3])
        coin_size = 20 + coin_value * 5  
        scaled_coin = pygame.transform.scale(coin_img, (coin_size, coin_size))
        coin_rect = scaled_coin.get_rect(center=(coin_x, -30))

        coin_rects.append((coin_rect, scaled_coin))  
        coin_values.append(coin_value)  
        coin_timer = 0

    for i in range(len(coin_rects) - 1, -1, -1):
        rect, image = coin_rects[i]
        rect.y += coin_speed

        
        screen.blit(image, rect)

        if player_rect.colliderect(rect):
            coin_count += coin_values[i]  
            del coin_rects[i]
            del coin_values[i]

            if coin_count % speed_increase_threshold == 0:
                coin_speed += 1

        elif rect.top > HEIGHT:
            del coin_rects[i]
            del coin_values[i]

    screen.blit(player_img, player_rect)

    coin_text = font.render(f"Coins: {coin_count}", True, YELLOW)
    screen.blit(coin_text, (WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
# code worked succesfully
