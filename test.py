import random
from check_input import get_int_range
from car import Car
from truck import Truck
from motorcycle import Motorcycle

def main():
    # Create the track
    track_length = 100
    track = [['-'] * track_length for _ in range(3)]
    
    # Randomly place 2 obstacles in each lane
    for lane in track:
        obstacles = random.sample(range(1, 99), 2)
        for pos in obstacles:
            lane[pos] = "0"

    # Create vehicles
    car = Car()
    motorcycle = Motorcycle()
    truck = Truck()

    vehicles = [car, motorcycle, truck]

    # Display game instructions and vehicle options
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("1. Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle (6-8 units). Special: Wheelie (2x speed but may crash).")
    print("3. Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and smashes obstacles).")

    player_choice = get_int_range("Choose your vehicle (1-3): ", 1, 3) - 1
    player = vehicles[player_choice]
    opponents = [o for i, o in enumerate(vehicles) if i != player_choice]

    finished_vehicles = []

    while len(finished_vehicles) < 3:
        # Display vehicle statuses
        print(f"\n{player.name} [Position - {player.position}, Energy - {player.energy}]")
        for opponent in opponents:
            print(f"{opponent.name} [Position - {opponent.position}, Energy - {opponent.energy}]")

        # Display the track for each lane
        for i, lane in enumerate(track):
            lane_display = lane[:]
            if i == player_choice:
                if player.position > 0:
                    lane_display[player.position - 1] = '*'  # Mark previous position
                lane_display[player.position] = "P"  # Mark current position
            else:
                opponent = opponents[i - (1 if i > player_choice else 0)]
                if opponent.position > 0:
                    lane_display[opponent.position - 1] = '*'  # Mark previous position
                lane_display[opponent.position] = opponent.initial  # Mark current position
            print(''.join(lane_display))  # Show lane after updating

        # Player action
        if player not in finished_vehicles:
            action = get_int_range("\nChoose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
            # Determine distance to the next obstacle
            try:
                next_obstacle = track[player_choice].index("0", player.position + 1)
                dist_to_next_obstacle = next_obstacle - player.position
            except ValueError:
                dist_to_next_obstacle = track_length  # No obstacle ahead

            # Execute player action
            if action == 1:
                print(player.fast(dist_to_next_obstacle))
            elif action == 2:
                print(player.slow(dist_to_next_obstacle))
            elif action == 3:
                print(player.special_move(dist_to_next_obstacle))

            # Check if the player finishes the race
            if player.position >= track_length and player not in finished_vehicles:
                finished_vehicles.append(player)
                print(f"\n{player.name} finished the race!")

        # Opponents' actions
        for opponent in opponents:
            if opponent in finished_vehicles:
                continue  # Skip if the opponent has already finished
            
            # Determine distance to the next obstacle
            try:
                next_obstacle = track[vehicles.index(opponent)].index("0", opponent.position + 1)
                dist_to_next_obstacle = next_obstacle - opponent.position
            except ValueError:
                dist_to_next_obstacle = track_length  # No obstacle ahead

            # Opponent's move decision
            if opponent.energy < 5:
                print(opponent.slow(dist_to_next_obstacle))  # Moves slowly due to low energy
                print(f"{opponent.name} moves slowly due to low energy.")
            else:
                # Randomly choose fast, slow, or special move
                opponent_action = random.choices(
                    [opponent.slow, opponent.fast, opponent.special_move], 
                    [0.4, 0.3, 0.3]
                )[0]
                
                # Execute the action
                move_result = opponent_action(dist_to_next_obstacle)
                if opponent_action == opponent.fast:
                    print(f"{opponent.name} chooses to move quickly.")
                elif opponent_action == opponent.slow:
                    print(f"{opponent.name} chooses to move slowly.")
                elif opponent_action == opponent.special_move:
                    print(f"{opponent.name} uses a special move.")

                # Display the result of the opponent's move
                print(move_result)

            # Check if the opponent finishes the race
            if opponent.position >= track_length and opponent not in finished_vehicles:
                finished_vehicles.append(opponent)
                print(f"\n{opponent.name} finished the race!")

    # Display the final results in order of finish
    print("\nRace Over! Final Results:")
    for i, vehicle in enumerate(finished_vehicles):
        place = ["1st", "2nd", "3rd"][i]
        print(f"{place} place: {vehicle.name} [Position: {vehicle.position}]")

if __name__ == "__main__":
    main()
