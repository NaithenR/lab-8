from vehicle import Vehicle
import random

class Truck(Vehicle):
    '''
    A class to represent a Truck, inheriting from the Vehicle class.
    '''
    def __init__(self):
        '''
        Initializes the Truck class with the given parameters.
        Calls the superclass’s init with values for name (“Behemoth Truck”),
        initial (‘T’), min_speed (4), and max_speed (8).
        '''
        super().__init__("Behemoth Truck", "T", 4, 8)

    def description_string(self):
        '''
        Returns a string with the truck’s stats and abilities.

        Returns:
        str: A string describing the truck's stats and abilities.
        '''
        return "Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles)."

    def special_move(self, dist):
        '''
        Implements the special move for the Truck.
        If there is sufficient energy (>= 15), deduct 15 energy and move the truck 2x speed,
        even if there is an obstacle (‘ram’ bashes through the obstacle).

        Parameters:
        dist (int): The distance to the next obstacle.

        Returns:
        str: A string describing the special move event.
        '''
        if self._energy >= 15:
            self._energy -= 15
            speed = random.randint(self._min_speed, self._max_speed) * 2
            if dist is not None and dist <= speed:
                self._position += dist  # Moves the full distance if an obstacle is present
                return f"{self._name} rammed through an obstacle and moved {dist} units!"
            else:
                self._position += speed
                return f"{self._name} rammed forward and moved {speed} units!"
        return f"{self._name} does not have enough energy for Ram!"