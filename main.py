from player import Player
from locations import Location

def main():
    # initialize locations
    # north west    
    bagend = Location("Bag end") 
    # north
    giant_oak = Location("The giant oak tree")
    # north east
    bindole_wood_entrance = Location("Bindole wood entrance")
    # west
    flower_garden = Location("The flower Garden")
    # middle
    market = Location("The market")
    # east
    dragon_inn = Location("The Dragon inn")
    # south west
    riverside_path_west = Location("River side path west")
    # south
    stone_bridge = Location("Stone bridge")
    #south east
    riverside_path_east = Location("River side path east")

    bagend.set_paths(east=giant_oak)

    giant_oak.set_paths(east=bindole_wood_entrance,south=market ,west=bagend)

    bindole_wood_entrance.set_paths(west=giant_oak)

    flower_garden.set_paths(east=market)

    market.set_paths(north=giant_oak, east=dragon_inn, south=stone_bridge, west=flower_garden)

    dragon_inn.set_paths(south=riverside_path_east, west=market)

    riverside_path_west.set_paths(east=stone_bridge)

    stone_bridge.set_paths(north=market, east=riverside_path_east, west=riverside_path_west)

    riverside_path_east.set_paths(north=dragon_inn, west=stone_bridge)
    
    # initilise player
    
    brad = Player("brad", market)
    print(brad)

if __name__ == "__main__":
    main()