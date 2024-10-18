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
        '''
        Returns the initial of the vehicle.

        Returns:
        str: The initial of the vehicle.
        '''
        return self._initial

    @property
    def position(self):
        '''
        Returns the current position of the vehicle.

        Returns:
        int: The current position of the vehicle.
        '''
        return self._position

    @property
    def energy(self):
        '''
        Returns the current energy level of the vehicle.

        Returns:
        int: The current energy level of the vehicle.
        '''
        return self._energy

    def fast(self, dist):
        '''
        Moves the vehicle fast if there is sufficient energy.
        Randomly selects a value between min and max speed for the number of spaces to move.
        Deducts 5 energy for the move. If the movement is less than the distance to the next obstacle,
        the vehicle moves that amount. Otherwise, it crashes into the obstacle and stops just before it.

        Parameters:
        dist (int): The distance to the next obstacle.

        Returns:
        str: A string describing the fast move event.
        '''
        if self._energy >= 5:
            spaces_moved = random.randint(self._min_speed, self._max_speed)
            self._energy -= 5
            if spaces_moved < dist:
                self._position += spaces_moved
                return f"{self._name} moved {spaces_moved} spaces."
            else:
                self._position += (dist - 1)
                return f"{self._name} moved {spaces_moved} spaces and crashed into the obstacle."
        return f"{self._name} does not have enough energy to move fast."

    def slow(self, dist):
        '''
        Moves the vehicle slow, going around obstacles without energy cost.
        The vehicle moves at half speed. If there is an obstacle, it goes around it.

        Parameters:
        dist (int): The distance to the next obstacle.

        Returns:
        str: A string describing the slow move event.
        '''
        half_speed = (self._min_speed + self._max_speed) // 2
        if half_speed < dist:
            self._position += half_speed
            return f"{self._name} moved {half_speed} spaces."
        else:
            self._position += (dist - 1)
            return f"{self._name} moved {half_speed} spaces and went around the obstacle."

    def __str__(self):
        '''
        Returns a string representation of the vehicle's name, position, and energy.

        Returns:
        str: A string representation of the vehicle.
        '''
        return f"{self._name} [Position - {self._position}, Energy - {self._energy}]"

    @abstractmethod
    def description_string(self):
        '''
        Abstract method to return a string with the vehicle’s stats and abilities.
        '''
        pass

    @abstractmethod
    def special_move(self, dist):
        '''
        Abstract method to implement the special move for the vehicle.

        Parameters:
        dist (int): The distance to the next obstacle.
        '''
        pass