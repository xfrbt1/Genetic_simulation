import random


class Food:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def random_pos(self):
        self.posX = random.randint(0, 1080) // 10 * 10
        self.posY = random.randint(0, 720) // 10 * 10

    def random_pos_1zone(self):
        self.posX = random.randint(0, 590) // 10 * 10
        self.posY = random.randint(0, 360) // 10 * 10

    def random_pos_2zone(self):
        self.posX = random.randint(590, 1080) // 10 * 10
        self.posY = random.randint(0, 360) // 10 * 10

    def random_pos_3zone(self):
        self.posX = random.randint(0, 590) // 10 * 10
        self.posY = random.randint(360, 720) // 10 * 10

    def random_pos_4zone(self):
        self.posX = random.randint(590, 1080) // 10 * 10
        self.posY = random.randint(360, 720) // 10 * 10

    def get_self(self):
        return [self.posX, self.posY]


def get_food_array(food_array, amount):
    food = Food(10, 10)
    for i in range(amount):
        food.random_pos()
        food_array.append(food.get_self())


