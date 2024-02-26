import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src import Actor

def test_createActor():
    Ned = Actor(1)
    assert(Ned.getId() == 1)
    assert(Ned.getZoneId() == None)
    
    Amy = Actor(2, 1)
    assert(Amy.getId() == 2)
    assert(Amy.getZoneId() == 1)

def test_moveActor():
    Ned = Actor(1, 0)
    Ned.moveToZone(2)
    assert(Ned.getZoneId() == 2)