import random
from check_input import get_int_range
from car import Car
from truck import Truck
from motorcycle import Motorcycle

def main():
    track = [['-'] * 100 for _ in range(3)]

    for lane in track:
        obstacles = random.sample(range(1, 99), 2)
        for pos in obstacles:
            lane[pos] = "0"

    car = Car()
    motorcycle = Motorcycle()
    truck = Truck()

    vehicles = [car, motorcycle, truck]
    
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("1. Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle (6-8 units). Special: Wheelie (2x speed but there's a chance you'll crash).")
    print("3. Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles).")
    
    player_choice = get_int_range("Choose your vehicle (1-3): ", 1, 3) - 1
    player = vehicles[player_choice]
    opponents = [o for i, o in enumerate(vehicles) if i != player_choice]


    race_over = False

    while not race_over:
        print(f"\n{player.name} [Position - {player.position}, Energy - {player.energy}]")
        for opponent in opponents:
            print(f"{opponent.name} [Position - {opponent.position}, Energy - {opponent.energy}]")

        for i, lane in enumerate(track):
            lane_display = lane[:] 
            if i == player_choice:
                lane_display[0] = "P"  
            else:
                lane_display[0] = vehicles[i].initial  
            print(''.join(lane_display))  
        
        dist_to_obstacle = track[player_choice].index("0", player.position + 1) - player.position if "0" in track[player_choice][player.position + 1:] else 100
        
        action = get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
        
        if action == 1:
            result = player.fast(dist_to_obstacle)
        elif action == 2:
            result = player.slow(dist_to_obstacle)
        elif action == 3:
            result = player.special_move(dist_to_obstacle)
        print(result)

        for opponent in opponents:
            dist_to_obstacle = track[vehicles.index(opponent)].index("0", opponent.position + 1) - opponent.position if "0" in track[vehicles.index(opponent)][opponent.position + 1:] else 100
            action = random.choices([1, 2, 3], weights=[0.4, 0.3, 0.3])[0]  
            if action == 1:
                opponent.fast(dist_to_obstacle)
            elif action == 2:  
                opponent.slow(dist_to_obstacle)
            elif action == 3:  
                opponent.special_move(dist_to_obstacle)
        


if __name__ == "__main__":
    main()
