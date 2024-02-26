from .actor import Actor


class Zombie(Actor):
    def __init__(self, startingZoneId: int, actions: int, damageToKill: int, damagePerAttack: int, attackRange: int, numberOfZombies: int, xp: int, id=None):
        super().__init__(id, startingZoneId, actions)
        self.damageToKill = damageToKill
        self.damagePerAttack = damagePerAttack
        self.attackRange = attackRange
        self.numberOfZombies = numberOfZombies
        self.xpReward = xp
        self.type = "zombie"

    def __str__(self) -> str:
        return f"{self.numberOfZombies} {self.type}{'s' if self.numberOfZombies > 1 else ''} in Zone {self.zoneId}"
    
    # Getters
    def getDamageToKill(self): return self.damageToKill

    def getDamagePerAttack(self): return self.damagePerAttack

    def getAttackRange(self): return self.attackRange

    def getNumberOfZombies(self): return self.numberOfZombies

    def getXpReward(self): return self.xpReward

    def getType(self): return self.type


    # Methods
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
    def __init__(self, startingZoneId: int, numberOfZombies: int, id=None):
        actions = 1
        damageToKill = 1
        damagePerAttack = 1
        attackRange = 0
        xp = 1
        super().__init__(startingZoneId, actions, damageToKill, damagePerAttack, attackRange, numberOfZombies, xp, id)
        self.type = "walker"

class Runner(Zombie):
    def __init__(self, startingZoneId: int, numberOfZombies: int, id=None):
        actions = 2
        damageToKill = 1
        damagePerAttack = 1
        attackRange = 0
        xp = 1
        super().__init__(startingZoneId, actions, damageToKill, damagePerAttack, attackRange, numberOfZombies, xp, id)
        self.type = "runner"
    
class Brute(Zombie):
    def __init__(self, startingZoneId: int, numberOfZombies: int, id=None):
        actions = 1
        damageToKill = 2
        damagePerAttack = 1
        attackRange = 0
        xp = 1
        super().__init__(startingZoneId, actions, damageToKill, damagePerAttack, attackRange, numberOfZombies, xp, id)
        self.type = "brute"

def createZombie(zombietype: str, startingZoneId: int, numberOfZombies: int, id=None):
    zType = {
        "walker": Walker,
        "runner": Runner,
        "brute": Brute
    }

    return zType[zombietype](startingZoneId, numberOfZombies, id)