import sys
import os

from src.rules.survivor import Survivor

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src import *

@pytest.fixture
def Ned():
    zone = Zone(1)
    ned = Survivor(zone, "Ned")
    return ned

def test_survivor(Ned: Survivor):

    assert(str(Ned) == "Ned is in Zone 1, has 2 health points, 0 xp and 3 actions left.")
    assert(Ned.health == 2)
    assert(Ned.actions == 3)
    assert(Ned.xp == 0)

def test_takeDamage(Ned: Survivor):
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

def test_equip(Ned: Survivor):
    Expectedinventory = {"hands": [], "backpack": []}
    assert(Expectedinventory == Ned.inventory)

    # add card
    card1 = Card("bottle")
    assert(Ned.equip(card1, "backpack"))
    Expectedinventory["backpack"].append(card1)
    assert(Expectedinventory == Ned.inventory)

    # add card to unknown location (test fail)
    assert(not Ned.equip(card1, "unknown"))

    # add a card already in the inventory (should return False)
    assert(not Ned.equip(card1, "backpack"))
    assert(Expectedinventory == Ned.inventory)

    # add a card already in the inventory (should return False), equiped in hands
    assert(not Ned.equip(card1, "hands"))
    assert(Expectedinventory == Ned.inventory)

    # add more cards to overload the inventory
    card2 = Weapon("pistol", "ranged", [0,1], 1, 4, 1, "dual")
    card4 = Weapon("pistol", "ranged", [0,1], 1, 4, 1, "dual")
    card3 = Card("testCard")
    assert(Ned.equip(card2, "backpack"))
    Expectedinventory["backpack"].append(card2)
    assert(Expectedinventory == Ned.inventory)

    assert(Ned.equip(card3, "backpack"))
    Expectedinventory["backpack"].append(card3)
    assert(Expectedinventory == Ned.inventory)

    # backpack is full
    assert(not Ned.equip(card4, "backpack"))
    assert(Expectedinventory == Ned.inventory)

    # Can be added in hand
    assert(Ned.equip(card4, "hands"))
    Expectedinventory["hands"].append(card4)
    assert(Expectedinventory == Ned.inventory)





    