import random

from food.food import Food


def zones_counter(food_array):
    zone1 = 0
    zone2 = 0
    zone3 = 0
    zone4 = 0
    for food in food_array:
        if food[0] < 590 and food[1] < 360:
            zone1 += 1
        elif 590 < food[0] < 1080 and food[1] < 360:
            zone2 += 1
        elif food[0] < 590 and 360 < food[1] < 720:
            zone3 += 1
        elif 590 < food[0] < 1080 and 360 < food[1] < 720:
            zone4 += 1
    return [zone1, zone2, zone3, zone4]


def zone_counter1(food_array):
    counter = 0
    for food in food_array:
        if food[0] < 590 and food[1] < 360:
            counter += 1
    return counter


def zone_counter2(food_array):
    counter = 0
    for food in food_array:
        if 590 < food[0] < 1080 and food[1] < 360:
            counter += 1
    return counter


def zone_counter3(food_array):
    counter = 0
    for food in food_array:
        if food[0] < 590 and 360 < food[1] < 720:
            counter += 1
    return counter


def zone_counter4(food_array):
    counter = 0
    for food in food_array:
        if 590 < food[0] < 1080 and 360 < food[1] < 720:
            counter += 1
    return counter


def generate_food1(amount, food_array):
    food = Food(10, 10)
    for i in range(amount):
        food.random_pos_1zone()
        food_array.append(food.get_self())


def generate_food2(amount, food_array):
    food = Food(10, 10)
    for i in range(amount):
        food.random_pos_2zone()
        food_array.append(food.get_self())


def generate_food3(amount, food_array):
    food = Food(10, 10)
    for i in range(amount):
        food.random_pos_3zone()
        food_array.append(food.get_self())


def generate_food4(amount, food_array):
    food = Food(10, 10)
    for i in range(amount):
        food.random_pos_4zone()
        food_array.append(food.get_self())


def generate_food(num, amount, food_array):
    if num == 0:
        generate_food1(amount, food_array)
    elif num == 1:
        generate_food2(amount, food_array)
    elif num == 2:
        generate_food3(amount, food_array)
    elif num == 3:
        generate_food4(amount, food_array)


def get_new_food(zone_list, food_array):
    for i in range(len(zone_list)):
        if 2124 / zone_list[i] > 20:
            amount = random.randint(500, 600) - zone_list[i]
            generate_food(i, amount, food_array)
