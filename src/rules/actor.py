from .zone import Zone

class Actor:
    def __init__(self, startingZone: Zone, actions: int = 1):
        self.currentZone = startingZone
        self.currentZone.addActor(self)
        self.actions = actions

    def __str__(self) -> str:
        return f"Actor in Zone {self.currentZone}"

    # Move to an adjacent zone.
    def move(self, adjZone: Zone):
        if adjZone in self.currentZone.connectedZones:
            self.currentZone.removeActor(self)
            self.currentZone = adjZone
            self.currentZone.addActor(self)
            self.actions -= 1

