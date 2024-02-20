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


testInventory = [
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "regorginize":   {"hands": [2,1], "backpack": [0,3,4]},
     "expected":      {"hands": [2,1], "backpack": [0,3,4]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0], "backpack": [2,3,4]},
     "regorginize":   {"hands": [3,4], "backpack": [0,2]},
     "expected":      {"hands": [3,4], "backpack": [0,2]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "regorginize":   {"hands": [], "backpack": [0,1,2,3,4]},
     "expected":      {"hands": [0,1], "backpack": [2,3,4]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "regorginize":   {"hands": [0,1,2,3,4], "backpack": []},
     "expected":      {"hands": [0,1], "backpack": [2,3,4]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "regorginize":   {"hands": [0,1], "backpack": [2,3]},
     "expected":      {"hands": [0,1], "backpack": [2,3,4]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "regorginize":   {"hands": [0], "backpack": [2,3]},
     "expected":      {"hands": [0,1], "backpack": [2,3,4]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "regorginize":   {"hands": [0], "backpack": [2,3,3]},
     "expected":      {"hands": [0,1], "backpack": [2,3,4]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4"), Card("5")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "regorginize":   {"hands": [0,1], "backpack": [2,3,5]},
     "expected":      {"hands": [0,1], "backpack": [2,3,4]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4"), Card("5")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "regorginize":   {"hands": [0,5], "backpack": [1,3,4]},
     "expected":      {"hands": [0,1], "backpack": [2,3,4]}
    }
]

@pytest.mark.parametrize("testInput", testInventory)
def test_reorganizeInventory(testInput, Ned):
    cards = testInput["cards"]
    inventory = {}
    for key in testInput["initInventory"]:
        inventory[key] = []
        for id in testInput["initInventory"][key]:
            inventory[key].append(cards[id])
            Ned.equip(cards[id], key)
    assert(Ned.inventory == inventory)

    # reorganize
    inventory = {}
    for key in testInput["regorginize"]:
        inventory[key] = []
        for id in testInput["regorginize"][key]:
            inventory[key].append(cards[id])
    
    expected = {}
    for key in testInput["expected"]:
            expected[key] = []
            for id in testInput["expected"][key]:
                expected[key].append(cards[id])

    Ned.reorganize(inventory["hands"], inventory["backpack"])
    assert(Ned.inventory == expected)


testRemove = [
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "cardToRemove":  0,
     "functionReturn": True,
     "expected":      {"hands": [1], "backpack": [2,3,4]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0,1], "backpack": [2,3,4]},
     "cardToRemove":  4,
     "functionReturn": True,
     "expected":      {"hands": [0,1], "backpack": [2,3]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Card("4")],
     "initInventory": {"hands": [0,1], "backpack": [2,3]},
     "cardToRemove":  4,
     "functionReturn": False,
     "expected":      {"hands": [0,1], "backpack": [2,3]}
    },
    {"cards": [Card("0"), Card("1"), Card("2"), Card("3"), Survivor(Zone(1), "Not a card")],
     "initInventory": {"hands": [0,1], "backpack": [2,3]},
     "cardToRemove":  4,
     "functionReturn": False,
     "expected":      {"hands": [0,1], "backpack": [2,3]}
    }
]

@pytest.mark.parametrize("testInput", testRemove)
def test_reorganizeInventory(testInput, Ned):
    cards = testInput["cards"]
    inventory = {}
    for key in testInput["initInventory"]:
        inventory[key] = []
        for id in testInput["initInventory"][key]:
            inventory[key].append(cards[id])
            Ned.equip(cards[id], key)
    assert(Ned.inventory == inventory)

    assert(Ned.removeCard(cards[testInput["cardToRemove"]]) == testInput["functionReturn"])

    inventory = {}
    for key in testInput["expected"]:
        inventory[key] = []
        for id in testInput["expected"][key]:
            inventory[key].append(cards[id])

    assert(Ned.inventory == inventory)

testValidLocation = [
    {"location": "hands",
     "valid": True
    },
    {"location": "backpack",
     "valid": True
    },
    {"location": "test",
     "valid": False
    },
    {"location": "hand",
     "valid": False
    },
    {"location": "Backpack",
     "valid": False
    }
]

@pytest.mark.parametrize("testInput", testValidLocation)
def test_validInventoryLocation(Ned, testInput):
    assert(Ned.validInventoryLocation(testInput["location"]) == testInput["valid"])


def test_isInInventory(Ned):
    card1 = Card("test") 
    card2 = Card("test2")
    assert(Ned.isInInventory(card1) == False)
    assert(Ned.isInInventory(card2) == False)

    Ned.equip(card1, "hands")
    assert(Ned.isInInventory(card1) == True)
    assert(Ned.isInInventory(card2) == False)

    Ned.removeCard(card1)
    assert(Ned.isInInventory(card1) == False)
    assert(Ned.isInInventory(card2) == False)

    Amy = Survivor(Zone(1), "Amy")
    Amy.equip(card1, "backpack")
    assert(Ned.isInInventory(card1) == False)
    assert(Amy.isInInventory(card1) == True)