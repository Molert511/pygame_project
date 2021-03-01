import pygame
import time
import random


def is_score(score):
    value = score_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [10, 10])


def message(msg, color):
    mesg = menu_style.render(msg, True, color)
    screen.blit(mesg, [275, height / 3])

    
def sss(s_size, blocks):
    for x in blocks:
        pygame.draw.rect(screen, orange, [x[0], x[1], s_size, s_size])


pygame.init()
width = 700
height = 500
white = (255, 255, 255)
orange = (255, 165, 0)
green = (255, 0, 0)
gray = (66, 66, 66)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
s_size = 10
s_speed = 15
menu_style = pygame.font.SysFont("candara", 40)
score_style = pygame.font.SysFont("candara", 35)
game_over = False
game_close = False
x1 = width / 2
y1 = height / 2
x_score = 0
y_score = 0
blocks = []
is_length = 1
food_x = round(random.randrange(0, width - s_size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - s_size) / 10.0) * 10.0
while not game_over:
    while game_close == True:
        screen.fill(gray)
        message("You Lost", orange)
        is_score(is_length - 1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_score = -s_size
                y_score = 0
            elif event.key == pygame.K_RIGHT:
                x_score = s_size
                y_score = 0
            elif event.key == pygame.K_UP:
                y_score = -s_size
                x_score = 0
            elif event.key == pygame.K_DOWN:
                y_score = s_size
                x_score = 0
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_close = True
    x1 += x_score
    y1 += y_score
    screen.fill(gray)
    pygame.draw.rect(screen, green, [food_x, food_y, s_size, s_size])
    block = []
    block.append(x1)
    block.append(y1)
    blocks.append(block)
    if len(blocks) > is_length:
        del blocks[0]
    for i in blocks[:-1]:
        if i == block:
            game_close = True
    sss(s_size, blocks)
    is_score(is_length - 1)
    pygame.display.update()
    if x1 == food_x and y1 == food_y:
        food_x = round(random.randrange(0, width - s_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - s_size) / 10.0) * 10.0
        is_length += 1
    clock.tick(s_speed)
pygame.quit()
quit()
