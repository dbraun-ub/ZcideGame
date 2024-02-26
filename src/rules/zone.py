from .token import Token
from .actor import Actor

class Zone:
    def __init__(self, id: int):
        self.id = id
        self.connectedZones = []
        self.actors = []
        self.lineOfSight = {}
        self.tokens = []

    def __str__(self) -> str:
        return f"Zone {self.id}"
    
    ## Getters
    def getId(self): return self.id
    
    def getConnectedZones(self): return self.connectedZones

    def getActors(self): return self.actors

    def getLineOfSight(self): return self.lineOfSight

    def getTokens(self): return self.tokens
    

    ## Methods
    
    def addConnection(self, newZone) -> None:
        if (newZone not in self.connectedZones) and (newZone is not self):
            self.connectedZones.append(newZone)

    def addActor(self, newActor: Actor) -> None:
        if newActor not in self.actors:
            self.actors.append(newActor)
            newActor.moveToZone(self.id)

    def removeActor(self, oldActor) -> None:
        if oldActor in self.actors:
            self.actors.remove(oldActor)
            oldActor.moveToZone(None)

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
    
    # TO TEST
    def addToken(self, newToken: Token):
        if newToken not in self.tokens:
            self.tokens.append(newToken)
    
    # TO TEST
    def removeToken(self, oldToken: Token):
        if oldToken in self.tokens:
            self.tokens.remove(oldToken)


class BuildingZone(Zone):
    # Building Zones properties:
    # - can be searched
    # - Limit line of sight to range one
    # - Zombie spawn when the building is opened for the first time 
    # - Each adjacent zone is connected with an open or closed door
    def __init__(self, id: int):
        super().__init__(id)
        self.type = "building"
        self.canBeSearched = True


class StreetZone(Zone):
    # Street Zones properties:
    # - can't be searched
    # - don't block line of sight
    # - Zombie don't spawn in street zone (except if there is a spawn token)
    # - Only connected with doors to building zones.
    def __init__(self, id: int):
        super().__init__(id)
        self.type = "street"
        self.canBeSearched = False

def createZone(zoneType: str, id):
    zoneTypes = {"BuildingZone": BuildingZone, "StreetZone": StreetZone}
    
    return zoneTypes[zoneType](id)