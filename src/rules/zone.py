class Zone:
    def __init__(self, id: int):
        self.id = id
        self.connectedZones = []
        self.actors = []
        self.lineOfSight = {}

    def __str__(self) -> str:
        return f"Zone {self.id}"
    
    def addConnection(self, newZone) -> None:
        if (newZone not in self.connectedZones) and (newZone is not self):
            self.connectedZones.append(newZone)

    def addActor(self, newActor) -> None:
        if newActor not in self.actors:
            self.actors.append(newActor)

    def removeActor(self, oldActor) -> None:
        self.actors.remove(oldActor)

    def addLineOfSight(self, newZone, distance: int) -> None:
        if distance not in self.lineOfSight.keys():
            self.lineOfSight[distance] = []

        # Verify unicity. A zone cannot be at two differente range
        for k in self.lineOfSight.keys():
            for z in self.lineOfSight[k]:
                if z == newZone:
                    self.lineOfSight[k].remove(z)
        
        self.lineOfSight[distance].append(newZone)

    def isInLineOfSight(self, zoneToLookFor) -> bool:
        for k in self.lineOfSight.keys():
            if zoneToLookFor in self.lineOfSight[k]:
                return True
            
        return False
