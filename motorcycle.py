from vehicle import Vehicle
import random

class Motorcycle(Vehicle):
    
    def __init__(self):
        super().__init__("Swift Bike", "M", 6, 8)
    
    def description_string(self):
        return "Swift Bike - a speedy motorcycle (6-8 units). Special: Wheelie (2x speed but may crash)."

    def slow(self, dist):
        speed = 0.75 * self._max_speed
        if dist is not None:
            travel_distance = min(speed, dist)
            return f"{self._name} traveled at 75% speed for {travel_distance} units, avoiding an obstacle."
        else:
            return f"{self._name} traveled at 75% speed with no obstacles."
        
    def special_move(self, dist):
        if self._energy >= 15:
            self._energy -= 15
            if random.random() < 0.75:  # 75% chance of success
                speed = random.randint(self._min_speed, self._max_speed) * 2
                if speed < dist:
                    self._position += speed
                    return f"{self._name} pops a wheelie and moves {int(speed)} units!"
                else:
                    self._position += (dist - 1)
                    return f"{self._name} crashes into an obstacle!"
            else:
                self._position += 1
                return f"{self._name} crashes while trying to pop a wheelie and only moves 1 unit!"
        return f"{self._name} does not have enough energy for Wheelie!"

    