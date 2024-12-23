import os
import platform
from initilize import initizile_objects

from player import Player

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
            break
        elif user_input == "1":
            clear_terminal()
            print("load game")
            break
    # start game opening - will be new function
    
    print(f"Welcome to the shire {player.name}")
    return player, locations
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
        print("1>   Yes")
        print("2>   No")
        user_input = input("> ")
        
        if user_input == "1":
            clear_terminal()
            locations = initizile_objects()
            player = Player(user_name, locations[4])                      
            
            return player, locations
        elif user_input == "2":
            continue
        

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")  # Windows command to clear the terminal
    else:
        os.system("clear")  # Unix/Linux/MacOS command to clear the terminal
        
