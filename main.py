from player import Player
from locations import Location
from start import clear_terminal, start, new_game
from initilize import initizile_objects
import json
def main():
    #player, locations = load_game()
    player, locations = start()
    save_game(player, locations)
    
def save_game(player, locations, inventory = None, quests= None, filename="savegame.json"):
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
    
    # Write the game state to a JSON file
    try:
        with open(filename, "w") as save_file:
            json.dump(game_state, save_file, indent=4)
        print("Game saved successfully!")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game(filename="savegame.json"):
    try:
        with open(filename, "r") as save_file:
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
        return player, locations
            
            
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return None, {}, [], {}
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, {}, [], {}


if __name__ == "__main__":
    main()