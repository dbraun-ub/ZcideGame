import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src import GameMap, Zone, Actor

def testCreateZone():
    zone1 = Zone(1)
    assert(str(zone1) == "Zone 1")
    assert(zone1.id == 1)

    print("simpleCase_createZone: OK")

def testAddConnections():
    zone1 = Zone(1)
    zone2 = Zone(2)

    zone1.addConnection(zone2)
    assert(zone1.connectedZones[0] == zone2)
    assert(len(zone2.connectedZones) == 0)
    
    zone1.addConnection(zone2)
    assert(len(zone1.connectedZones) == 1)

    zone2.addConnection(zone2)
    assert(zone2 not in zone2.connectedZones)

    print("simpleCase_addConnections: OK")

def testAddActor():
    zone1 = Zone(1)
    zone2 = Zone(2)
    Ned = Actor(zone1)
    assert(Ned in zone1.actors)
    assert(Ned not in zone2.actors)

    Ned.move(zone2)
    assert(Ned in zone1.actors)
    assert(Ned not in zone2.actors)

    zone1.addConnection(zone2)
    zone2.addConnection(zone1)

    Ned.move(zone2)
    assert(Ned not in zone1.actors)
    assert(Ned in zone2.actors)

    print("simpleCase_addActor: OK")

def testRemoveActor():
    zone1 = Zone(1)
    Ned = Actor(zone1)
    assert(Ned in zone1.actors)

    zone1.removeActor(Ned)
    assert(Ned not in zone1.actors)

    print("simpleCase_removeActor: OK")

def testAddLineOfSight():
    zone1 = Zone(1)
    zone2 = Zone(2)
    zone3 = Zone(3)

    assert(not zone1.isInLineOfSight(zone2))
    zone1.addLineOfSight(zone2, 1)
    assert(zone1.isInLineOfSight(zone2))
    assert(zone2 in zone1.lineOfSight[1])
    zone1.addLineOfSight(zone2, 2)
    assert(zone2 not in zone1.lineOfSight[1])
    assert(zone2 in zone1.lineOfSight[2])

    print("simpleCase_addLineOfSight: OK")