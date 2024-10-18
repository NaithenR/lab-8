#Naithen Ramirez, Cris Padilla Castillo, Group 2
#October 17, 2024
# A racing game in which a car, motorcycle, and truck move across a track in which there is obstacles.
import random
from check_input import get_int_range
from car import Car
from truck import Truck
from motorcycle import Motorcycle

def main():
    '''
    Main function to run the Rad Racer game.
    Initializes the track, creates vehicles, and handles the game loop.
    '''
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

    # Display the game instructions and vehicle options
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    for i, vehicle in enumerate(vehicles, start=1):
        print(f"{i}. {vehicle.description_string()}")

    player_choice = get_int_range("Choose your vehicle (1-3): ", 1, 3) - 1
    player = vehicles[player_choice]
    opponents = [o for i, o in enumerate(vehicles) if i != player_choice]

    # Initialize previous positions
    previous_positions = {vehicle: [] for vehicle in vehicles}

    finished_vehicles = []

    while len(finished_vehicles) < 3:
        print(f"\n{player._name} [Position - {player.position}, Energy - {player.energy}]")
        for opponent in opponents:
            print(f"{opponent._name} [Position - {opponent.position}, Energy - {opponent.energy}]")

        for i, lane in enumerate(track):
            lane_display = lane[:]
            if i == player_choice:
                for pos in previous_positions[player]:
                    lane_display[pos] = '*'
                if player.position < len(lane_display):
                    lane_display[player.position] = "P"
            else:
                opponent = opponents[i - (1 if i > player_choice else 0)]
                for pos in previous_positions[opponent]:
                    lane_display[pos] = '*'
                if opponent.position < len(lane_display):
                    lane_display[opponent.position] = opponent.initial
            print(''.join(lane_display))

        # Player action
        if player not in finished_vehicles:
            action = get_int_range("\nChoose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
            try:
                dist_to_obstacle = track[player_choice][player.position:].index('0')
            except ValueError:
                dist_to_obstacle = len(track[player_choice]) - player.position

            previous_positions[player].append(player.position)
            if action == 1:
                result = player.fast(dist_to_obstacle)
            elif action == 2:
                result = player.slow(dist_to_obstacle)
            elif action == 3:
                result = player.special_move(dist_to_obstacle)
            
            print(result)
            
            if player.position >= len(track[player_choice]):
                finished_vehicles.append(player)
                print(f"{player.name} has finished the race!")

        # Opponents' actions
        for opponent in opponents:
            if opponent not in finished_vehicles:
                try:
                    dist_to_obstacle = track[opponents.index(opponent) + (1 if opponents.index(opponent) >= player_choice else 0)][opponent.position:].index('0')
                except ValueError:
                    dist_to_obstacle = len(track[opponents.index(opponent) + (1 if opponents.index(opponent) >= player_choice else 0)]) - opponent.position

                previous_positions[opponent].append(opponent.position)
                if opponent.energy < 5:
                    action = 2  # Move slow if out of energy
                else:
                    action = random.choices([1, 2, 3], weights=[30, 40, 30])[0]

                if action == 1:
                    result = opponent.fast(dist_to_obstacle)
                elif action == 2:
                    result = opponent.slow(dist_to_obstacle)
                elif action == 3:
                    result = opponent.special_move(dist_to_obstacle)
                print(result)

                if opponent.position >= len(track[opponents.index(opponent) + (1 if opponents.index(opponent) >= player_choice else 0)]):
                    finished_vehicles.append(opponent)
                    print(f"{opponent._name} has finished the race!")

    # Display the final results in order of finish
    print("\nRace Over! Final Results:")
    for i, vehicle in enumerate(finished_vehicles):
        place = ["1st", "2nd", "3rd"][i]
        print(f"{place} place: {vehicle.name} [Position: {vehicle.position}]")

if __name__ == "__main__":
    main()