class Actor:
    def __init__(self, id, startingZoneId=None, actions: int = 1):
        # zone id
        self.id = id
        self.zoneId = startingZoneId 
        self.actions = actions

    def __str__(self) -> str:
        return f"Actor in Zone {self.zoneId}"
    
    ## Getter
    def getId(self): return self.id
        
    def getZoneId(self): return self.zoneId

    # Move to an adjacent zone.
    def moveToZone(self, adjZoneId):
        # The verifications of the possibilty of the movement is done elsewhere.
        self.zoneId = adjZoneId
        self.actions -= 1
        # if adjZoneId in self.zoneId.connectedZones:
        #     # self.currentZone.removeActor(self)
        #     self.zoneId = adjZoneId
        #     # self.currentZone.addActor(self)
        #     self.actions -= 1

