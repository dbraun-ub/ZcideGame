from .zone import Zone

class Actor:
    def __init__(self, startingZone: Zone):
        self.currentZone = startingZone
        self.currentZone.addActor(self)

    # Move to an adjacent zone.
    def move(self, adjZone: Zone):
        if adjZone in self.currentZone.connectedZones:
            self.currentZone.removeActor(self)
            self.currentZone = adjZone
            self.currentZone.addActor(self)

    