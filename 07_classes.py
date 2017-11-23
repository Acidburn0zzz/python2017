# A object orientated game
import math
import random

class GameObject:
    x = 0
    y = 0

    def distance_to_game_object(self, obj):
        return math.sqrt(
            pow(self.x - obj.x, 2) + \
            pow(self.y - obj.y, 2)
            )

class Player(GameObject):
    pass

class Treasure(GameObject):
    def randomize_location(self):
        self.x = random.randint(-10, 10)
        self.y = random.randint(-10, 10)


player = Player()
treasure = Treasure()
treasure.randomize_location()

while True:
    print("You are at ({}, {}). The treasure is {} metres away!".format(
        player.x,
        player.y,
        treasure.distance_to_game_object(player)
        ))

    direction = input("Which way would you like to go? ")

    if direction == 'up':
        player.y += 1
    elif direction == 'down':
        player.y -= 1
    elif direction == 'left':
        player.x -= 1
    elif direction == 'right':
        player.x += 1
    else:
        print("That's not a real direction!")
        continue
