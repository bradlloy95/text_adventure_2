class Location:
    def __init__(self, name):
        self.name = name
        self.locations = {}
        self.set_paths()
        
    def set_paths(self, north = None, east = None, south = None, west= None):
       # Update paths only if a value is provided; default to the existing or "No path"
        self.locations["North"] = north if north is not None else self.locations.get("North", "No path")
        self.locations["East"] = east if east is not None else self.locations.get("East", "No path")
        self.locations["South"] = south if south is not None else self.locations.get("South", "No path")
        self.locations["West"] = west if west is not None else self.locations.get("West", "No path")
        
    def __str__(self):
        connections = {direction: (loc.name if isinstance(loc, Location) else loc) 
                   for direction, loc in self.locations.items()}
        return f"{self.name}:\n" + "\n".join([f"  {direction}: {destination}" for direction, destination in connections.items()])

    
