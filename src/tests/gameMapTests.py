import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from rules import GameMap, Zone

def simpleCase_createZones():
    myMap = GameMap()
    zone1 = Zone(1)
    zone2 = Zone(2)

    myMap.addZone(zone1)
    myMap.addZone(zone2)
    myMap.connectZones(zone1, zone2)

    assert(zone1.connectedZones == myMap.zones[0].connectedZones)
    assert(zone2.connectedZones == myMap.zones[1].connectedZones)

    print("simpleCase_createZones: OK")

def simpleCase_findPathZones(trueShortestPath: list, connections: map, startPosition: int, endPosition: int):
    myMap = GameMap()

    for k in connections.keys():
        for c in connections[k]:
            myMap.connectZonesWithId(k, c)

    for z in myMap.zones:
        if startPosition == z.id:
            zone1 = z
        if endPosition == z.id:
            zone2 = z

    shortestPath = myMap.shortestPathZones(zone1, zone2)

    for i in range(len(trueShortestPath)):
        for j in range(len(trueShortestPath[i])):
            assert(shortestPath[i][j].id == trueShortestPath[i][j])

    print("simpleCase_findPathZones: OK")



if __name__ == "__main__":
    simpleCase_createZones()
    simpleCase_findPathZones([[0,1]], {0:[1], 1:[0]}, 0, 1)
    simpleCase_findPathZones([[0,3,4,7]], {0:[1,2,3], 1:[0,3], 2:[0,5], 3:[0,1,4], 4:[3,7], 5:[2,6], 6:[5,7], 7:[4,6]}, 0, 7)
    simpleCase_findPathZones([[1,2,4,8,7],[1,3,4,8,7]], {0:[1], 1:[0,2,3], 2:[1,4], 3:[1,4], 4:[2,3,8], 5:[6], 6:[5,7], 7:[6,8], 8:[4,7,9], 9:[8]}, 1, 7)