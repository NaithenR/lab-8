import random
from check_input import get_int_range
from car import Car
from truck import Truck
from motorcycle import Motorcycle



def main():
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'p'). SLow down for obstacle ('0') or else you'll crash")
    print("1. Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle (6-8 units). Special: Wheelie (2x speed but there's a chance you'll crash).")
    print("3. Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles).")
    
    choices = get_int_range("Choose your vehicle (1-3): ", 1, 3)
    
    
    track = [['-'] * 100 for _ in range(3)]
    for lane in track:
        obstacles = random.sample(range(1, 99), 2)
        for pos in obstacles:
            lane[pos] = "0"
    for lane in track:
        print("".join(lane))

    car = Car()
    truck = Truck()
    motorcycle = Motorcycle()

    vehicles = [car, truck, motorcycle]
main()