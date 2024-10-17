from vehicle import Vehicle
import random

class Motorcycle(Vehicle):
    
    def __init__(self):
        super().__init__("Swift Bike", "M", 6, 8)
    
    def slow(self, dist):
        speed = 0.75 * self._max_speed
        if dist is not None:
            travel_distance = min(speed, dist)
            return f"{self._name} traveled at 75% speed for {travel_distance} units, avoiding an obstacle."
        else:
            return f"{self._name} traveled at 75% speed with no obstacles."
    
    def description_string(self):
        return f"Motorcycle Name: {self._name}, Initial: {self._initial}, Speed Range: {self._min_speed}-{self._max_speed}, Energy: {self._energy}"
    
    def special_move(self, dist):
        if self._energy >= 15:
            self._energy -= 15
            if random.random() < 0.75:  # 75% chance
                speed = 2 * self._max_speed
                if dist is not None and speed >= dist:
                    return f"{self._name} crashed into an obstacle after moving {dist - 1} units."
                else:
                    return f"{self._name} successfully moved at 2x speed for {speed} units."
            else:
                return f"{self._name} crashed and only moved one space forward."
        else:
            return f"{self._name} did not have enough energy to perform the special move."

    