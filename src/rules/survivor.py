from .zone import Zone
from .actor import Actor

class Survivor(Actor):
    def __init__(self, startingZone: Zone, name: str):
        actions = 3
        super().__init__(startingZone, actions)
        self.health = 2
        self.xp = 0
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} is in {self.currentZone}, has {self.health} health points, {self.xp} xp and {self.actions} action{'s' if self.actions > 1 else ''} left."

    def takeDamage(self, damageDealt: int, hits: int):
        self.health -= (hits * damageDealt)

    def isAlive(self):
        return self.health > 0