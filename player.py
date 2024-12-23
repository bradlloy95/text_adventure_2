class Player:
    def __init__(self, name, location):
        self.name = name
        self.current_location = location
        
    def set_location(self, location):
        self.current_location = location
    
    def to_dict(self):
        return {
            "name" : self.name,
            "location" : self.current_location.name
        }
        
    @classmethod
    def from_dict(cls, data, locations):
        # Initialize player using data and find the location by name
        location_name = data["location"]
        location = locations.get(location_name)  # Get location from locations dictionary
        return cls(data["name"], location)
    
    def __str__(self):
        return f"{self.name} \npaths: {self.current_location}"
    




