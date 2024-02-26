# To generate unique ID
import uuid

class Actor:
    def __init__(self, id=None, startingZoneId=None, actions: int = 1):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        
        self.zoneId = startingZoneId 
        self.actions = actions

    def __str__(self) -> str:
        return f"Actor in Zone {self.zoneId}"
    
    ## Getters
    def getId(self): return self.id
        
    def getZoneId(self): return self.zoneId

    def getActions(self): return self.actions

    ## Methods

    # Move to an adjacent zone.
    def moveToZone(self, adjZoneId):
        self.zoneId = adjZoneId
        self.actions -= 1


