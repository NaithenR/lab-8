
from vehicle import Vehicle
import random
class Truck(Vehicle):
    def __init__(self):
        super().__init__("Behemoth Truck", "T", 4, 8)

    def description_string(self):
        return f"Truck Name: {self._name}, Initial: {self._initial}, Speed Range: {self._min_speed}-{self._max_speed}, Energy: {self._energy}"

    
    def special_move(self, dist):
        if self._energy >= 15:
            speed = random.randint(self._min_speed, self._max_speed) * 2
            if speed >= dist:
                self._position += dist
                self._energy -= 15
                return f"{self._name} rams forward bashing through the Obstacle to go {int(speed)} units."
            else:
                self._position += speed
                self._energy -= 15
                return f"{self._name} rams forward bashing through the Obstacle to go {int(speed)} units."
        else:
            return f"{self._name} doesn't have enough energy for a special move."