import random
import pygame
import sys

from type_red.type_red import Red_type

from food.food import get_food_array
from type_red.type_red import get_red_array, change_reds_positions, division, red_eat_food, dead_check
from food.food_density import zones_counter, get_new_food

width = 1080
height = 720
fps = 30

pygame.init()
screen = pygame.display.set_mode(size=(width, height))
screen.fill(color=(190, 190, 190))
pygame.display.set_caption("SIMULATION")
clock = pygame.time.Clock()


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_food_array(food_array):
    for food in food_array:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((food[0], food[1], 10, 10)), width=0)


def draw_red_array(red_array):
    for red in red_array:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(red[0], red[1], 10, 10), width=0)



food_list = list()
get_food_array(food_list, 900)

reds_list = list()
get_red_array(reds_list, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color=(190, 190, 190))

    zn_cntr = zones_counter(food_list)

    change_reds_positions(reds_list)

    print(reds_list[0])

    red_eat_food(reds_list, food_list)

    division(reds_list)

    draw_red_array(reds_list)

    draw_food_array(food_list)

    draw_text(screen, f"Food: {len(food_list)}", 17, 1010, 7)
    draw_text(screen, f"Reds: {len(reds_list)}", 17, 1010, 25)

    draw_text(screen, f"Zone1: {zn_cntr[0]}", 17, 1010, 45)
    draw_text(screen, f"Zone2: {zn_cntr[1]}", 17, 1010, 65)
    draw_text(screen, f"Zone3: {zn_cntr[2]}", 17, 1010, 85)
    draw_text(screen, f"Zone4: {zn_cntr[3]}", 17, 1010, 105)

    pygame.display.update()
    clock.tick(fps)
