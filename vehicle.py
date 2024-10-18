

import random
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, name, initial, min_speed, max_speed):
        self._name = name
        self._initial = initial
        self._min_speed = min_speed
        self._max_speed = max_speed
        self._position = 0 
        self._energy = 100

    @property
    def initial(self):
        return self._initial

    @property
    def position(self):
        return self._position

    @property
    def energy(self):
        return self._energy

    def fast(self, dist): 
        if self._energy >= 5:
            spaces_moved = random.randint(self._min_speed, self._max_speed)
            self._energy -= 5
            if spaces_moved < dist:
                self._position += spaces_moved
                return f"{self._name} quickly moves {spaces_moved} units!"
            else:
                self._position = (dist-1)
                return f"{self._name} crashes in an obstacle!"
        return f"{self._name} does not have enough energy to move fast."

    def slow(self, dist): 
        half_speed = (self._min_speed + self._max_speed) // 2
        if half_speed < dist:
            self._position += half_speed
            return f"{self._name} slowly moves {half_speed} units."
        else:
            self._position += (dist - 1)
            return f"{self._name} safely moves around the obstacle."

    def __str__(self):
        return f"{self._name} [Position - {self._position}, Energy - {self._energy}"

    @abstractmethod
    def description_string(self):
        pass

    @abstractmethod
    def special_move(self, dist):
        pass