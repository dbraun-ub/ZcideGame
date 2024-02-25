import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src import *

def test_createActor():
    myZone = Zone(0)
    Ned = Actor(myZone)

def test_moveActor():
    zone1 = Zone(1)
    zone2 = Zone(2)
    zone1.addConnection(zone2)
    zone1.addConnection(zone1)

    Ned = Actor(zone1)
    Ned.move(zone2)

    assert(Ned.currentZone == zone2)

def test_moveActor2():
    zone1 = Zone(1)
    zone2 = Zone(2)
    zone3 = Zone(3)
    zone1.addConnection(zone2)
    zone1.addConnection(zone1)
    Ned = Actor(zone1)

    # Try a forbidden move
    Ned.move(zone3) 
    assert(Ned.currentZone == zone1)

    zone3.addConnection(zone2)
    zone2.addConnection(zone3)

    # Try a forbidden move again
    Ned.move(zone3) 
    assert(Ned.currentZone == zone1)

    # Move by zone 2 first to reach zone 3.
    Ned.move(zone2)
    Ned.move(zone3)
    assert(Ned.currentZone == zone3)