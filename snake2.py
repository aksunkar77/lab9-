# in this file i will upgrade my snake.py from lab8
#i added foods with random values 
#and food will be removed on the screen after 5 seconds and replace eaten food
import pygame
import random
import sys

pygame.init()

BLOCK_SIZE = 20
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (BLOCK_SIZE, 0)

wall_blocks = [(300, 200), (320, 200), (340, 200)]

score = 0
level = 1
speed = 10

#  Food list with position, value, color, and spawn time
food = []
food_timer_limit = 300  # How long food stays on screen (~5 seconds)

# Random food value/color and spawn time
def generate_food(snake_body, wall_blocks):
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_pos = (x, y)

        if food_pos in snake_body or food_pos in wall_blocks:
            continue

        value = random.choice([1, 2, 3])
        color = RED if value == 1 else ORANGE if value == 2 else YELLOW

        return (food_pos, value, color, pygame.time.get_ticks())

def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def game_loop():
    global snake, snake_dir, score, level, speed, food

    running = True
    food.append(generate_food(snake, wall_blocks))  #  First food spawn

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != (0, BLOCK_SIZE):
                    snake_dir = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK_SIZE):
                    snake_dir = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and snake_dir != (BLOCK_SIZE, 0):
                    snake_dir = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-BLOCK_SIZE, 0):
                    snake_dir = (BLOCK_SIZE, 0)

        head_x, head_y = snake[0]
        new_head = (head_x + snake_dir[0], head_y + snake_dir[1])

        if new_head in wall_blocks or new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            running = False

        snake.insert(0, new_head)

        ate_food = False
        for i in range(len(food) - 1, -1, -1):
            pos, value, color, spawn_time = food[i]
            if new_head == pos:
                score += value
                ate_food = True
                del food[i]

                food.append(generate_food(snake, wall_blocks))  #  Replace eaten food

                if score % 4 == 0:
                    level += 1
                    speed += 2
                break

        if not ate_food:
            snake.pop()

        #  Remove expired food after time limit
        current_time = pygame.time.get_ticks()
        for i in range(len(food) - 1, -1, -1):
            _, _, _, spawn_time = food[i]
            if current_time - spawn_time > food_timer_limit:
                del food[i]
                food.append(generate_food(snake, wall_blocks))  #  Replace expired food

        for block in snake:
            pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))

        for pos, value, color, _ in food:
            pygame.draw.rect(screen, color, (*pos, BLOCK_SIZE, BLOCK_SIZE))

        for wall in wall_blocks:
            pygame.draw.rect(screen, BLUE, (*wall, BLOCK_SIZE, BLOCK_SIZE))

        draw_text(f"Score: {score}", WHITE, 10, 10)
        draw_text(f"Level: {level}", WHITE, 10, 40)

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()
    sys.exit()

game_loop()
#code worked succesfully 
