import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src import *


# Variables

zombieTypes = [
    {"class": Walker, 
     "startingZone": Zone(1), 
     "actions": 1, 
     "damageToKill": 1,
     "damagePerAttack": 1,
     "attackRange": 0,
     "numberOfZombies": 1,
     "xp": 1,
     "ExpectedString": "1 walker in Zone 1"
    },
    {"class": Walker, 
     "startingZone": Zone(1), 
     "actions": 1, 
     "damageToKill": 1,
     "damagePerAttack": 1,
     "attackRange": 0,
     "numberOfZombies": 5,
     "xp": 1,
     "ExpectedString": "5 walkers in Zone 1"
    },
    {"class": Runner, 
     "startingZone": Zone(2), 
     "actions": 2, 
     "damageToKill": 1,
     "damagePerAttack": 1,
     "attackRange": 0,
     "numberOfZombies": 5,
     "xp": 1,
     "ExpectedString": "5 runners in Zone 2"
    },
    {"class": Brute, 
     "startingZone": Zone(2), 
     "actions": 1, 
     "damageToKill": 2,
     "damagePerAttack": 1,
     "attackRange": 0,
     "numberOfZombies": 4,
     "xp": 1,
     "ExpectedString": "4 brutes in Zone 2"
    }
]

@pytest.mark.parametrize("testInput", zombieTypes)
def test_createZombie(testInput):
    zombie = testInput["class"](testInput["startingZone"].getId(), testInput["numberOfZombies"])

    assert(str(zombie) == testInput["ExpectedString"])
    assert(zombie.getZoneId() == testInput["startingZone"].getId())
    assert(zombie.getActions() == testInput["actions"])
    assert(zombie.getDamageToKill() == testInput["damageToKill"])
    assert(zombie.getDamagePerAttack() == testInput["damagePerAttack"])
    assert(zombie.getAttackRange() == testInput["attackRange"])
    assert(zombie.getNumberOfZombies() == testInput["numberOfZombies"])
    assert(zombie.getXpReward() == testInput["xp"])

    