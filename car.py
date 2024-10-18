from vehicle import Vehicle
import random

class Car(Vehicle):
    def __init__(self):
        super().__init__("Lightning Car", "C", 6, 8)

    def description_string(self):
        return "Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)."

    def special_move(self, dist):
        if self._energy >= 15:
            self._energy -= 15
            speed = int(random.randint(self._min_speed, self._max_speed) * 1.5)
            if speed < dist:
                self._position += speed
                return f"{self._name} used Nitro Boost and moved {speed} units!"
            else:
                self._position += (dist - 1)
                return f"{self._name} crashed into an obstacle!"
        return f"{self._name} does not have enough energy for Nitro Boost!"
