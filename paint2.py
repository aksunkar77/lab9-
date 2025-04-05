#in this file i will upgrade my code from lab8 paint.py
# i added Square triangle ,equilateral Triangle ,Rhombus
import pygame
import sys
import math  

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLACK
screen.fill(WHITE)

DRAW_RECT = 'rect'
DRAW_CIRCLE = 'circle'
DRAW_FREE = 'free'
ERASER = 'eraser'
DRAW_SQUARE = 'square'                  
DRAW_RIGHT_TRI = 'right_triangle'       
DRAW_EQ_TRI = 'equilateral_triangle'   
DRAW_RHOMBUS = 'rhombus'               
current_tool = DRAW_FREE

start_pos = None
radius = 20

font = pygame.font.SysFont(None, 24)

def draw_ui():
    pygame.draw.rect(screen, RED, (10, 10, 40, 40))
    pygame.draw.rect(screen, GREEN, (60, 10, 40, 40))
    pygame.draw.rect(screen, BLUE, (110, 10, 40, 40))
    pygame.draw.rect(screen, BLACK, (160, 10, 40, 40))
    pygame.draw.rect(screen, WHITE, (210, 10, 40, 40))

    pygame.draw.rect(screen, (200, 200, 200), (260, 10, 80, 40))
    pygame.draw.rect(screen, (200, 200, 200), (350, 10, 80, 40))
    pygame.draw.rect(screen, (200, 200, 200), (440, 10, 80, 40))
    pygame.draw.rect(screen, (200, 200, 200), (530, 10, 80, 40))

    pygame.draw.rect(screen, (200, 200, 200), (620, 10, 80, 40))  
    pygame.draw.rect(screen, (200, 200, 200), (710, 10, 80, 40))   
    pygame.draw.rect(screen, (220, 220, 220), (10, 60, 130, 40))  
    pygame.draw.rect(screen, (220, 220, 220), (150, 60, 100, 40))  

    screen.blit(font.render("Rect", True, BLACK), (270, 20))
    screen.blit(font.render("Circle", True, BLACK), (360, 20))
    screen.blit(font.render("Free", True, BLACK), (450, 20))
    screen.blit(font.render("Eraser", True, BLACK), (540, 20))
    screen.blit(font.render("Square", True, BLACK), (630, 20))       
    screen.blit(font.render("R. Tri", True, BLACK), (720, 20))       
    screen.blit(font.render("Eq. Triangle", True, BLACK), (20, 70)) 
    screen.blit(font.render("Rhombus", True, BLACK), (160, 70))      

def get_color(pos):
    x, y = pos
    if 10 <= x <= 50 and 10 <= y <= 50:
        return RED
    elif 60 <= x <= 100 and 10 <= y <= 50:
        return GREEN
    elif 110 <= x <= 150 and 10 <= y <= 50:
        return BLUE
    elif 160 <= x <= 200 and 10 <= y <= 50:
        return BLACK
    elif 210 <= x <= 250 and 10 <= y <= 50:
        return WHITE
    return None

def get_tool(pos):
    x, y = pos
    if 260 <= x <= 340 and 10 <= y <= 50:
        return DRAW_RECT
    elif 350 <= x <= 430 and 10 <= y <= 50:
        return DRAW_CIRCLE
    elif 440 <= x <= 520 and 10 <= y <= 50:
        return DRAW_FREE
    elif 530 <= x <= 610 and 10 <= y <= 50:
        return ERASER
    elif 620 <= x <= 700 and 10 <= y <= 50:
        return DRAW_SQUARE              # New
    elif 710 <= x <= 790 and 10 <= y <= 50:
        return DRAW_RIGHT_TRI           # New
    elif 10 <= x <= 140 and 60 <= y <= 100:
        return DRAW_EQ_TRI              # New
    elif 150 <= x <= 250 and 60 <= y <= 100:
        return DRAW_RHOMBUS             # New
    return None

running = True
mouse_down = False
draw_ui()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            start_pos = pygame.mouse.get_pos()
            pos = start_pos
            color = get_color(pos)
            tool = get_tool(pos)
            if color:
                current_color = color
            if tool:
                current_tool = tool

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            end_pos = pygame.mouse.get_pos()
            x1, y1 = start_pos
            x2, y2 = end_pos

            if current_tool == DRAW_RECT:
                pygame.draw.rect(screen, current_color, pygame.Rect(start_pos, (x2 - x1, y2 - y1)), 2)
            elif current_tool == DRAW_CIRCLE:
                center = ((x1 + x2) // 2, (y1 + y2) // 2)
                radius = max(abs(x2 - x1) // 2, abs(y2 - y1) // 2)
                pygame.draw.circle(screen, current_color, center, radius, 2)
            elif current_tool == DRAW_SQUARE:  # New
                side = min(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, current_color, (x1, y1, side, side), 2)
            elif current_tool == DRAW_RIGHT_TRI:  # New
                points = [start_pos, (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, current_color, points, 2)
            elif current_tool == DRAW_EQ_TRI:  # New
                side = abs(x2 - x1)
                height = int(math.sqrt(3) / 2 * side)
                points = [start_pos, (x1 + side, y1), (x1 + side // 2, y1 - height)]
                pygame.draw.polygon(screen, current_color, points, 2)
            elif current_tool == DRAW_RHOMBUS:  # New
                mid_x = (x1 + x2) // 2
                mid_y = (y1 + y2) // 2
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
                pygame.draw.polygon(screen, current_color, points, 2)

        elif event.type == pygame.MOUSEMOTION and mouse_down:
            if current_tool == DRAW_FREE:
                pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), 3)
            elif current_tool == ERASER:
                pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 10)

    draw_ui()
    pygame.display.flip()

pygame.quit()
sys.exit()
#code worked succesfully
