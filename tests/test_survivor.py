import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src import *

@pytest.fixture
def Ned():
    zone = Zone(1)
    ned = Survivor(zone, "Ned")
    return ned

def test_survivor(Ned):

    assert(str(Ned) == "Ned is in Zone 1, has 2 health points, 0 xp and 3 actions left.")
    assert(Ned.health == 2)
    assert(Ned.actions == 3)
    assert(Ned.xp == 0)

def test_takeDamage(Ned):
    assert(Ned.health == 2)
    Ned.takeDamage(damageDealt=1, hits=1)
    assert(Ned.health == 1)
    assert(Ned.isAlive())
    Ned.takeDamage(damageDealt=1, hits=1)
    assert(Ned.health == 0)
    assert(not Ned.isAlive())

    Ned.health = 10
    assert(Ned.health == 10)
    assert(Ned.isAlive())
    Ned.takeDamage(damageDealt=2, hits=1)
    assert(Ned.health == 8)
    assert(Ned.isAlive())
    Ned.takeDamage(damageDealt=1, hits=2)
    assert(Ned.health == 6)
    assert(Ned.isAlive())
    Ned.takeDamage(damageDealt=3, hits=2)
    assert(Ned.health == 0)
    assert(not Ned.isAlive())





    