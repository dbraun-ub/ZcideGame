import numpy as np

class Card():
    def __init__(self, name: str) -> None:
        self.name = name
        self.description = ""
        self.owner = None

    def updateOwner(self, newOwner):
        self.owner = newOwner

class Weapon(Card):
    def __init__(self, name: str, type: str, range: list, dice: int, accuracy: int, damage: int, description: str) -> None:
        super().__init__(name)
        self.type = type
        self.range = range
        self.dice = dice
        self.accuracy = accuracy
        self.damage = damage
        self.description = description

    def attack(self):
        roll = np.random.rand(self.dice) * 6 + 1
        print(roll)
        hits = np.sum(roll >= self.accuracy)
        return hits