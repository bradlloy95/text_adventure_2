class Location:
    def __init__(self, name):
        self.name = name
        self.paths = {}
        self.set_paths()
        self.items = []
        
    def set_paths(self, north = None, east = None, south = None, west= None):
       # Update paths only if a value is provided; default to the existing or "No path"
        self.paths["north"] = north if north is not None else self.paths.get("North", "No path")
        self.paths["east"] = east if east is not None else self.paths.get("East", "No path")
        self.paths["south"] = south if south is not None else self.paths.get("South", "No path")
        self.paths["west"] = west if west is not None else self.paths.get("West", "No path")
        
    def set_items(self, list_of_items):
        for item in list_of_items:
            self.items.append(item)
            
    def to_dict(self):
        # Serialize the Location object to a dictionary
        return {
            "name": self.name,
            "paths": {direction: loc.name if isinstance(loc, Location) else loc 
                          for direction, loc in self.paths.items()},
            "items": self.items
        }
    
    @classmethod
    def from_dict(cls, data):
        # Deserialize a dict to an object
        location = cls(data["name"])
        location.set_paths(**data["paths"])
        location. set_items(data["items"])
        return location
        
    def __str__(self):
        connections = {direction: (loc.name if isinstance(loc, Location) else loc) 
                   for direction, loc in self.paths.items()}
        return f"{self.name}:\n" + "\n".join([f"  {direction}: {destination}" for direction, destination in connections.items()])

    
