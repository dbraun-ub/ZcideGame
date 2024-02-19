from .actor import Actor
from .zone import Zone

class Zombie(Actor):
    def __init__(self, startingZone: Zone, actions: int, damageToKill: int, damagePerAttack: int, attackRange: int, numberOfZombies: int, xp: int):
        super().__init__(startingZone, actions)
        self.damageToKill = damageToKill
        self.damagePerAttack = damagePerAttack
        self.attackRange = attackRange
        self.numberOfZombies = numberOfZombies
        self.xp = xp
        self.type = "zombie"

    def __str__(self) -> str:
        return f"{self.numberOfZombies} {self.type}{'s' if self.numberOfZombies > 1 else ''} in Zone {self.currentZone.id}"

    def attack(self, targetActor: Actor):
        targetActor.takeDamage(self.damagePerAttack)

    def takeDamage(self, damageDealt: int, hits: int):
        if damageDealt >= self.damageToKill:
            self.numberOfZombies -= hits
        else:
            return hits
        
        if self.numberOfZombies < 0:
            hits = -self.numberOfZombies
            self.numberOfZombies = 0
            return hits

class Walker(Zombie):
    def __init__(self, startingZone: Zone, numberOfZombies: int):
        actions = 1
        damageToKill = 1
        damagePerAttack = 1
        attackRange = 0
        xp = 1
        super().__init__(startingZone, actions, damageToKill, damagePerAttack, attackRange, numberOfZombies, xp)
        self.type = "walker"

class Runner(Zombie):
    def __init__(self, startingZone: Zone, numberOfZombies: int):
        actions = 2
        damageToKill = 1
        damagePerAttack = 1
        attackRange = 0
        xp = 1
        super().__init__(startingZone, actions, damageToKill, damagePerAttack, attackRange, numberOfZombies, xp)
        self.type = "runner"
    
class Brute(Zombie):
    def __init__(self, startingZone: Zone, numberOfZombies: int):
        actions = 1
        damageToKill = 2
        damagePerAttack = 1
        attackRange = 0
        xp = 1
        super().__init__(startingZone, actions, damageToKill, damagePerAttack, attackRange, numberOfZombies, xp)
        self.type = "brute"