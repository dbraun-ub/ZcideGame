class Zone:
    def __init__(self, id: int):
        self.id = id
        self.connectedZones = []
        self.actors = []

    def __str__(self) -> str:
        return f"Zone {id}"
    
    def addConnection(self, newZone):
        if newZone not in self.connectedZones:
            self.connectedZones.append(newZone)

    def addActor(self, newActor):
        if newActor not in self.actors:
            self.actors.append(newActor)

    def removeActor(self, oldActor):
        self.actors.remove(oldActor)