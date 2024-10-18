from vehicle import Vehicle
import random

class Car(Vehicle):
    '''
    A class to represent a Car, inheriting from the Vehicle class.
    '''
    def __init__(self):
        '''
        Initializes the Car class with the given parameters.
        Calls the superclass’s init with values for name (“Lightning Car”),
        initial (‘C’), min_speed (6), and max_speed (8).
        '''
        super().__init__("Lightning Car", "C", 6, 8)

    def description_string(self):
        '''
        Returns a string with the car’s stats and abilities.

        Returns:
        str: A string describing the car's stats and abilities.
        '''
        return "Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)."

    def special_move(self, dist):
        '''
        Implements the special move for the Car.
        If there is sufficient energy (>= 15), deduct 15 energy and move the car 1.5x speed,
        even if there is an obstacle (‘Nitro Boost’).

        Parameters:
        dist (int): The distance to the next obstacle.

        Returns:
        str: A string describing the special move event.
        '''
        if self._energy >= 15:
            self._energy -= 15
            speed = int(random.randint(self._min_speed, self._max_speed) * 1.5)
            if dist is not None and speed >= dist:
                self._position += max(0, dist - 1)  # Prevent negative movement on crash
                return f"{self._name} crashed into an obstacle after moving {dist - 1} units."
            else:
                self._position += speed
                return f"{self._name} successfully moved at Nitro Boost speed for {speed} units."
        else:
            return f"{self._name} does not have enough energy for Nitro Boost!"
