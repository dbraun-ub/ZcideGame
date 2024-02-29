import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
import json
from src import *

missionsPath = os.path.join(os.path.dirname(__file__), '..', "resources", "missions")

missionPath = [
    os.path.join(missionsPath, "Zombicide\\00-tutorial.json")
]

@pytest.mark.parametrize("testInput", missionPath)
def test_master(testInput):
    master = Master(testInput)
    features = json.load(open(testInput))

    gameMapFeatures = features["gameMap"]

    assert(master.missionMetaData == features["mission"])
    assert(master.gameMapFeatures == gameMapFeatures)

    
    for key in gameMapFeatures.keys():
        for element in gameMapFeatures[key]:
            if key == "zones":
                zoneType = element
                for zoneId in gameMapFeatures[key][zoneType]:
                    assert(master.gameMap.getZone(zoneId).getType() == zoneType)

            elif key == "connections":
                zoneId = element
                for connectedZone in master.gameMap.getZone(zoneId).getConnectedZones():
                    assert(connectedZone.getId() in gameMapFeatures["connections"][zoneId])

            elif key == "tokens":
                pass

            elif key == "zombies":
                zombieType = element
                zombieTested = 0
                for zoneId in gameMapFeatures[key][zombieType]:
                    for actor in master.gameMap.getZone(zoneId).getActors():
                        if actor.getType() == zombieType:
                            zombieTested += 1
                            assert(actor.getNumberOfZombies() == gameMapFeatures[key][zombieType][zoneId])
                # Verify the correct number of zombies objects have been tested.
                assert(zombieTested == len(gameMapFeatures[key][zombieType]))
                



