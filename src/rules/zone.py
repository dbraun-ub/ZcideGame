class Zone:
    def __init__(self, id: int):
        self.id = id
        self.connectedZones = []

    def __str__(self) -> str:
        return f"Zone {id}"
    
    def addConnection(self, newZone):
        if newZone not in self.connectedZones:
            self.connectedZones.append(newZone)