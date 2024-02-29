import json
from .gameMap import GameMap
from .zone import createZone
from .token import createToken
from .zombie import createZombie

class Master:
    def __init__(self, missionFileName: str):
        self.missionFileName = missionFileName
        features = json.load(open(self.missionFileName))
        self.missionMetaData = features["mission"]
        self.gameMapFeatures = features["gameMap"]
        self.gameMap = GameMap()

        self.setup()

    ## Getters
    def getMissionMetaData(self): return self.missionMetaData

    def getMissionFileName(self): return self.missionFileName

    def getGameMapFeatures(self): return self.gameMapFeatures

    ## Methods
    def setup(self):
        # Create zones
        zones = self.gameMapFeatures["zones"]
        for zoneType in zones:
            for zoneId in zones[zoneType]:
                self.gameMap.addZone(createZone(zoneType, zoneId))

        # Create connections between zones
        self.gameMap.addConnections(self.gameMapFeatures["connections"]) 

        # Add tokens (optional)
        if "tokens" in self.gameMapFeatures:
            if "Objective" in self.gameMapFeatures["tokens"]:
                objective = self.gameMapFeatures["tokens"]["Objective"]
                for obj in objective:
                    self.gameMap.getZone(obj["position"]).addToken(createToken("Objective", 
                                                                               obj["position"], 
                                                                               obj["xp"], 
                                                                               obj["color"]))
            
        # Add zombies (optional)
        if "zombies" in self.gameMapFeatures:
            zombies = self.gameMapFeatures["zombies"]
            for zombieType in zombies.keys():
                for zoneId in zombies[zombieType].keys():
                    newZombie = createZombie(zombieType, zoneId, zombies[zombieType][zoneId])
                    self.gameMap.getZone(zoneId).addActor(newZombie)