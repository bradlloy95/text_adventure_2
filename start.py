import os


from initilize import initizile_objects
from player import Player
from locations import Location
from player import Player
from utils import save_game, load_game, clear_terminal, yes_no
import json

def start():
    
    # Run loop for main menu
    while True:
        clear_terminal()
        print("Main  menu:\n")
        print("1>   New game")
        print("2>   Load game")
        
        # get user input using numers
        user_input = input("> ")
        if user_input == "1":
            print("new game")
            player, locations = new_game()
            print(f"Welcome to the shire {player.name}")
            
        # Load game
        elif user_input == "2":
            clear_terminal()
            print("load game")
            
            player, locations, filename = load(get_filenames())
            return player, locations, filename
            break
        
        # create save filename
        while True:
            save_name = input("Save file name > ")
            print(f"Save file as '{save_name}")
            print("Would you like to continue with this name?")
            yes = yes_no()
            
            if yes:
                save_name = f"{save_name}.json"
                return player, locations, save_name
    # start game opening - will be new function
    
    
def new_game():
    while True:
        clear_terminal()            
        
        # Get name
        print("What is your name?")
        user_name = input(">").capitalize()
        
        # chech lenght of name 
        if len(user_name) < 3 or len(user_name) > 10:
            print("Your name needs to be between 2-10 characters")
            continue
        
        clear_terminal()
        
        # Check is name is correct
        print(f"Your name is {user_name}.")
        print("Would you like to continue with this name?")
        user_input = yes_no()
        
        if user_input:
            clear_terminal()
            locations = initizile_objects()
            player = Player(user_name, locations[4])                      
            
            return player, locations
        else:
            continue

def load(filenames):
    while True:
        label = 1
        for save in filenames:
            print(f"{label}>   {save}")
            label += 1
        print("Pick your save")
        user_input = int(input("> "))
        if 0 < user_input <= len(filenames):
            print("yes")
            save_file = filenames[user_input - 1]
            player, locations, filename = load_game(filename=filenames[user_input - 1])
            return player, locations, filename
        else:
            print("nio")

def get_filenames(foldername = "saves"):
    # Get the full path to the folder
    folder_path = os.path.join(os.getcwd(), foldername)
    
    try:
        # List all filenames in the folder
        filenames = os.listdir(folder_path)
        #print(f"Filenames in '{foldername}': {filenames}")
        return filenames
    except FileNotFoundError:
        print(f"The folder '{foldername}' does not exist.")
        return []
    except Exception as e:
        print(f"Error reading filenames from folder: {e}")
        return []



       
