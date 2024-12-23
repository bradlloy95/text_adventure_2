from player import Player
from locations import Location
from start import start
from initilize import initizile_objects
from utils import save_game, clear_terminal
import json
def main():
    #player, locations = load_game()
    player, locations, save_name = start()
    
    save_game(player, locations, filename=save_name)

if __name__ == "__main__":
    main()