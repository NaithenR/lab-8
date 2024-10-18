from vehicle import Vehicle
import random

class Motorcycle(Vehicle):
    '''
    A class to represent a Motorcycle, inheriting from the Vehicle class.
    '''
    def __init__(self):
        '''
        Initializes the Motorcycle class with the given parameters.
        Calls the superclass’s init with values for name (“Swift Bike”),
        initial (‘M’), min_speed (6), and max_speed (8).
        '''
        super().__init__("Swift Bike", "M", 6, 8)
    
    def slow(self, dist):
        '''
        Moves the motorcycle at 75% of its maximum speed.
        If there is an obstacle, it avoids it and travels the minimum distance
        between the calculated speed and the distance to the obstacle.

        Parameters:
        dist (int): The distance to the next obstacle.

        Returns:
        str: A string describing the slow move event.
        '''
        speed = int(random.randint(self._min_speed, self._max_speed) * 2)  # Calculate boosted speed
        if dist is not None:  
            travel_distance = min(speed, dist)  
            self._position += travel_distance  
            self._position = max(0, self._position)

            return f"{self._name} traveled at 75% speed for {travel_distance} units, avoiding an obstacle."
        else:  
            self._position += speed  # Move at 75% speed
            self._position = max(0, self._position)
            return f"{self._name} traveled at 75% speed with no obstacles."
    
    def description_string(self):
        '''
        Returns a string with the motorcycle’s stats and abilities.

        Returns:
        str: A string describing the motorcycle's stats and abilities.
        '''
        return f"Motorcycle Name: {self._name}, Initial: {self._initial}, Speed Range: {self._min_speed}-{self._max_speed}, Energy: {self._energy}"
    
    def special_move(self, dist):
        '''
        Implements the special move for the Motorcycle.
        If there is sufficient energy (>= 15), deduct 15 energy and move the motorcycle at 2x speed,
        with a 75% chance of success. If successful, it moves at 2x speed, otherwise, it crashes.

        Parameters:
        dist (int): The distance to the next obstacle.

        Returns:
        str: A string describing the special move event.
        '''
        if self._energy >= 15:
            self._energy -= 15
            if random.random() < 0.75:  # 75% chance of success
                speed = 2 * self._max_speed
                if dist is not None and speed >= dist:
                    self._position += dist - 1  
                    return f"{self._name} crashed into an obstacle after moving {dist - 1} units."
                else:
                    self._position += speed
                    return f"{self._name} successfully moved at 2x speed for {speed} units."
            else:
                self._position += dist - 1  
                return f"{self._name} crashed and stopped at {dist - 1} units."
        else:
            return f"{self._name} did not have enough energy to perform the special move."