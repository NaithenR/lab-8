from vehicle import Vehicle
import random

class Truck(Vehicle):
    def __init__(self):
        super().__init__("Behemoth Truck", "T", 4, 8)

    def description_string(self):
        return "Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles)."

    def special_move(self, dist):
        if self._energy >= 15:
            self._energy -= 15
            speed = random.randint(self._min_speed, self._max_speed) * 2

            if dist <= speed:
                self._position += dist  
                return f"{self._name} rammed through an obstacle and moved {dist} units!"
            else:
                self._position += speed 
                return f"{self._name} rammed forward and moved {speed} units!"
        return f"{self._name} does not have enough energy for Ram!"
