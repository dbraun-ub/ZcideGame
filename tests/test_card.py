import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src import *

@pytest.fixture
def basicWeapon():
    pistol = Weapon("pistol", "ranged", [0,1], 1, 4, 1, "dual")
    return pistol

@pytest.fixture
def basicWeapon2():
    pistol = Weapon("pistol", "ranged", [0,1], 2, 4, 1, "dual")
    return pistol

def test_basicWeapon(basicWeapon):
    assert(basicWeapon.name == "pistol")
    assert(basicWeapon.type == "ranged")
    assert(basicWeapon.range == [0,1])
    assert(basicWeapon.dice == 1)
    assert(basicWeapon.accuracy == 4)
    assert(basicWeapon.damage == 1)
    assert(basicWeapon.description == "dual")

@pytest.mark.parametrize("random_values, expected_results", [([0.1, 0.51, 0.9], [0, 1, 1])])
def test_attack(basicWeapon, monkeypatch, random_values, expected_results):
    def mock_rand(size):
        return random_values.pop(0) if size == 1 else random_values[:size]

    monkeypatch.setattr(np.random, 'rand', mock_rand)

    results = [basicWeapon.attack() for _ in expected_results]

    assert results == expected_results

@pytest.mark.parametrize("random_values, expected_results", [
                            (np.array([0.1,0.2]), 0),
                            (np.array([0.1,0.8]), 1),
                            (np.array([0.8,0.6]), 2)
                        ])
def test_attack2(basicWeapon2, monkeypatch, random_values, expected_results):
    def mock_rand(size):
        return random_values.pop(0) if size == 1 else random_values[:size]
        
    monkeypatch.setattr(np.random, 'rand', mock_rand)

    results = basicWeapon2.attack() 

    assert (results == expected_results)