class Player:
    def __init__(self, name, location= None):
        self.name = name
        self.current_location = location
        
    def set_location(self, location):
        self.current_location = location
        
    def __str__(self):
        return f"{self.name} \nlocation: {self.current_location}"
    
