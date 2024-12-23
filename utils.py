import os
import platform
import json
from locations import Location
from player import Player



def save_game(player, locations, inventory=None, quests=None, folder="saves", filename="savefile.json"):
    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)
    
    # Construct the full path to the file
    file_path = os.path.join(folder, filename)
    
    # Convert locations to dictionaries
    if isinstance(locations, list):
        serialized_locations = {loc.name: loc.to_dict() for loc in locations}
    else:
        serialized_locations = {loc.name: loc.to_dict() for loc in locations.values()}
    
    serialized_player = player.to_dict()
    
    # Save everything to a dictionary
    game_state = {
        "locations": serialized_locations,
        "player": serialized_player,
        "inventory": inventory,
        "quests": quests
    }
    
    # Write the game state to the JSON file
    try:
        with open(file_path, "w") as save_file:
            json.dump(game_state, save_file, indent=4)
        print(f"Game saved successfully to {file_path}!")
    except Exception as e:
        print(f"Error saving game: {e}")
        
def load_game(folder="saves", filename="savegame.json"):
    
    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)
    
    # Construct the full path to the file
    file_path = os.path.join(folder, filename)
    
    try:
        with open(file_path, "r") as save_file:
            game_state = json.load(save_file)
        
        # Reinitialize locations
        locations = {name: Location.from_dict(data) for name, data in game_state["locations"].items()}
        
        # Reconnect locations (paths between rooms)
        for loc in locations.values():
            for direction, destination in loc.paths.items():
                if destination != "No path":
                    loc.paths[direction] = locations.get(destination, "No path")
        
        # Recreate the player
        player_data = game_state["player"]
        player = Player.from_dict(player_data, locations)
        
        print("Game loaded successfully!")
        return player, locations, filename
            
            
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return None, {}, filename
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, {}, filename
    


def yes_no():
    while True:
        print("1>   Yes")
        print("2>   No")
        user_input = input("> ")
            
        if user_input == "1":
            return True
        elif user_input == "2":
            return False
        
def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")  # Windows command to clear the terminal
    else:
        os.system("clear")  # Unix/Linux/MacOS command to clear the terminal
