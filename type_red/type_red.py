import random


class Red_type:
    def __init__(self, posX=0, posY=0, division_energy=0, energy=30):
        self.posX = posX
        self.posY = posY
        self.division_energy = division_energy
        self.energy = energy

    def random_pos(self):
        self.posX = random.randint(0, 1080) // 10 * 10
        self.posY = random.randint(0, 720) // 10 * 10

    def get_self(self):
        return [self.posX, self.posY, self.division_energy, self.energy]


def get_red_array(list, amount):
    red = Red_type()
    for i in range(amount):
        red.random_pos()
        list.append(red.get_self())


def change_reds_positions(list):
    for i in range(len(list)):
        if list[i][0] <= 0:
            list[i][0] += 10
        elif list[i][0] >= 1080:
            list[i][0] -= 10
        if list[i][1] <= 0:
            list[i][1] += 10
        elif list[i][1] >= 720:
            list[i][1] -= 10

        b = random.randint(0, 1)
        c = random.randint(0, 1)
        if b == 0:
            if c == 0:
                list[i][0] += 10
            else:
                list[i][0] -= 10
        else:
            if c == 0:
                list[i][1] += 10
            else:
                list[i][1] -= 10


def red_eat_food(red_array, food_array):
    for i in range(len(red_array)):
        for j in food_array:
            if red_array[i][0] == j[0] and red_array[i][1] == j[1]:
                food_array.remove(j)
                inc_energy(red_array[i])
        else:
            dec_energy(red_array[i])


def dead_check(red_array):
    for i in range(len(red_array)):
        if red_array[i][3] == 0:
            red_array.remove(red_array[i])


def inc_energy(red):
    red[2] += 1
    red[3] += 20


def dec_energy(red):
    red[3] = red[3] - 1


def division(red_array):
    for red in red_array:
        if red[2] > 3:
            red[2] = 0
            red_array.append([red[0], red[1], 0, 50])
