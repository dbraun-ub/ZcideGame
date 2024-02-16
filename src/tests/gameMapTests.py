import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from rules import GameMap, Zone, Actor

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

def simpleTest_addConnections(connections: map):
    map1 = GameMap()
    for k in connections.keys():
        for c in connections[k]:
            map1.connectZonesWithId(k, c)

    map2 = GameMap(connections)

    # the objects themselves will be different, but the ids must be the same 
    for zone1, zone2 in zip(map1.zones, map2.zones):
        assert(zone1.id == zone2.id)
        for cZone1, cZone2 in zip(zone1.connectedZones, zone2.connectedZones):
            assert(cZone1.id == cZone2.id)

    print("simpleTest_addConnections: OK")

def simpleCase_moveActor(connections: map, startPosition: int, endPosition: int):
    # Init map
    myMap = GameMap(connections)

    for z in myMap.zones:
        if startPosition == z.id: zone1 = z
        if endPosition == z.id: zone2 = z

    shortestPath = myMap.shortestPathZones(zone1, zone2)

    for i in range(len(shortestPath)):
        testActor = Actor(zone1)
        for z in shortestPath[i]:
            testActor.move(z)
        assert(testActor.currentZone == zone2)

    print("simpleCase_moveActor: OK")


def main():
    simpleCase_createZones()

    connections1 = {0:[1], 1:[0]}
    startPosition1, endPosition1 = 0, 1  

    connections2 = {0:[1,2,3], 1:[0,3], 2:[0,5], 3:[0,1,4], 4:[3,7], 5:[2,6], 6:[5,7], 7:[4,6]}
    startPosition2, endPosition2 = 0, 7
    
    connections3 = {0:[1], 1:[0,2,3], 2:[1,4], 3:[1,4], 4:[2,3,8], 5:[6], 6:[5,7], 7:[6,8], 8:[4,7,9], 9:[8]}
    startPosition3, endPosition3 = 1, 7

    simpleCase_findPathZones([[0,1]], connections1, startPosition1, endPosition1)
    simpleCase_findPathZones([[0,3,4,7]], connections2, startPosition2, endPosition2)
    simpleCase_findPathZones([[1,2,4,8,7],[1,3,4,8,7]], connections3, startPosition3, endPosition3)

    simpleTest_addConnections(connections1)
    simpleTest_addConnections(connections2)
    simpleTest_addConnections(connections3)

    simpleCase_moveActor(connections1, startPosition1, endPosition1)
    simpleCase_moveActor(connections2, startPosition2, endPosition2)
    simpleCase_moveActor(connections3, startPosition3, endPosition3)

if __name__ == "__main__":
    main()