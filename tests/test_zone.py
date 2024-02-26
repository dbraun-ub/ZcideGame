import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src import Zone, Actor, BuildingZone, StreetZone

def testCreateZone():
    zone1 = Zone(1)
    assert(str(zone1) == "Zone 1")
    assert(zone1.getId() == 1)

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
    Ned = Actor(0, None)
    zone1.addActor(Ned)
    assert(Ned in zone1.actors)
    assert(Ned.getZoneId() == 1)


def testRemoveActor():
    zone1 = Zone(1)
    Ned = Actor(0, None)
    zone1.addActor(Ned)
    assert(Ned in zone1.actors)

    zone1.removeActor(Ned)
    assert(Ned not in zone1.actors)
    assert(Ned.getZoneId() == None)


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


def testTypeOfZones():
    zone2 = BuildingZone(2)
    zone3 = StreetZone(3)

    assert(zone2.canBeSearched == True)
    assert(zone3.canBeSearched == False)