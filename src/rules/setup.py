from gameMap import GameMap
from token import ObjectiveToken
from zombie import Walker
from survivor import Survivor

def setup():
    # For this first implementation, the map will be hard coded. 
    # At a later time, it will be possible to import a mission from a data file.

    # Setup game map 00: Tutorial
    connections = {0:[1], 1:[2,4], 2:[1,5], 
                   3:[0,6], 4:[1,5,7], 5:[2,4],
                   6:[3,7], 7:[4,6,8], 8:[7,10],
                   9:[11,12], 10:[8,13],
                   11:[9,12], 12:[9,11,13], 13:[10,12]}
    
    missionMap = GameMap(connections)

    # Add tokens
    # Objective token
    zone2 = missionMap.findZonePerId(id=2)
    redObjective = ObjectiveToken(zone2)

    # Add deck of cards
    
    # Add players
    zone11 = missionMap.findZonePerId(id=11)
    survivors = []
    survivors.append(Survivor(zone11, "Ned"))
    survivors.append(Survivor(zone11, "Amy"))
    survivors.append(Survivor(zone11, "Wanda"))
    survivors.append(Survivor(zone11, "Josh"))

    # Add Zombies
    zombies = []
    zombies.append(Walker(missionMap.findZonePerId(id=3), 1))
    zombies.append(Walker(missionMap.findZonePerId(id=10), 1))

    pass

if __name__ == "__main__":
    setup()