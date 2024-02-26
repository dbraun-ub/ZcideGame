import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src import *


# Variables

inputs = [
    {"trueShortestPath": [[0,1]], 
     "connections": {0:[1], 1:[0]}, 
     "startPosition": 0, 
     "endPosition": 1
    },
    {"trueShortestPath": [[0,3,4,7]], 
     "connections": {0:[1,2,3], 1:[0,3], 2:[0,5], 3:[0,1,4], 4:[3,7], 5:[2,6], 6:[5,7], 7:[4,6]}, 
     "startPosition": 0, 
     "endPosition": 7
    },
    {"trueShortestPath": [[1,2,4,8,7],[1,3,4,8,7]], 
     "connections": {0:[1], 1:[0,2,3], 2:[1,4], 3:[1,4], 4:[2,3,8], 5:[6], 6:[5,7], 7:[6,8], 8:[4,7,9], 9:[8]}, 
     "startPosition": 1, 
     "endPosition": 7
    }
]


# Test functions

def test_createZones():
    myMap = GameMap()
    zone1 = Zone(1)
    zone2 = Zone(2)

    myMap.addZone(zone1)
    myMap.addZone(zone2)
    myMap.connectZones(zone1, zone2)

    assert(zone1.getConnectedZones() == myMap.zones[zone1.getId()].getConnectedZones())
    assert(zone2.getConnectedZones() == myMap.zones[zone2.getId()].getConnectedZones())


@pytest.mark.parametrize("testInput", inputs)
def test_shortestPathZones(testInput):
    connections = testInput["connections"]
    startPosition = testInput["startPosition"]
    endPosition = testInput["endPosition"]
    trueShortestPath = testInput["trueShortestPath"]

    myMap = GameMap()

    for k in connections.keys():
        for c in connections[k]:
            myMap.connectZonesWithId(k, c)

    shortestPath = myMap.shortestPathZones(myMap.zones[startPosition], myMap.zones[endPosition])

    for i in range(len(trueShortestPath)):
        for j in range(len(trueShortestPath[i])):
            assert(shortestPath[i][j].id == trueShortestPath[i][j])

@pytest.mark.parametrize("testInput", inputs)
def test_shortestPathZonesPerId(testInput):
    connections = testInput["connections"]
    startPosition = testInput["startPosition"]
    endPosition = testInput["endPosition"]
    trueShortestPath = testInput["trueShortestPath"]

    # Init map
    myMap = GameMap(connections)

    shortestPath = myMap.shortestPathZonesPerId(startPosition, endPosition)

    for i in range(len(trueShortestPath)):
        for j in range(len(trueShortestPath[i])):
            assert(shortestPath[i][j].id == trueShortestPath[i][j])

@pytest.mark.parametrize("testInput", inputs)
def test_addConnections(testInput):
    connections = testInput["connections"]

    map1 = GameMap()
    for k in connections.keys():
        for c in connections[k]:
            map1.connectZonesWithId(k, c)

    map2 = GameMap(connections)

    # the objects themselves will be different, but the ids must be the same 
    for zoneId1, zoneId2 in zip(map1.zones.keys(), map2.zones.keys()):
        assert(zoneId1 == zoneId2)
        for cZone1, cZone2 in zip(map1.zones[zoneId1].getConnectedZones(), map1.zones[zoneId2].getConnectedZones()):
            assert(cZone1.getId() == cZone2.getId())