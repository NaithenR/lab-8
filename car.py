from vehicle import Vehicle
import random

class Car(Vehicle): 
    
    def __init__(self):
        super().__init__("Lighning Car", "C", 6, 8)
    
    def description_string(self):
        return f"Car Name: {self._name}, Initial: {self._initial}, Speed Range: {self._min_speed}-{self._max_speed}, Energy: {self._energy}"
    
    def special_move(self, dist):
        if self._energy >= 15:
            speed = random.randint(self._min_speed, self._max_speed) * 1.5
            if speed >= dist:
                self._position += dist
                self._energy -= 15
                return f"{self._name} used special move and traveled {dist} units to reach the obstacle."
            else:
                self._position += speed
                self._energy -= 15
                return f"{self._name} uses nitro boost and moves {int(speed)} units,"
        else:
            return f"{self._name} doesn't have enough energy for a special move."