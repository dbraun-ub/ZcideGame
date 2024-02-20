from .zone import Zone
from .actor import Actor
from .card import Card

class Survivor(Actor):
    def __init__(self, startingZone: Zone, name: str):
        actions = 3
        super().__init__(startingZone, actions)
        self.health = 2
        self.xp = 0
        self.name = name
        self.inventory = {"hands": [], "backpack": []}
        self.maxInventorySlots = {"hands": 2, "backpack": 3} 
        self.handsInventory = []
        self.backpackInventory = []
        self.maxHandsSlots = 2
        self.maxBackpackSlots = 3

    def __str__(self) -> str:
        return f"{self.name} is in {self.currentZone}, has {self.health} health points, {self.xp} xp and {self.actions} action{'s' if self.actions > 1 else ''} left."

    def takeDamage(self, damageDealt: int, hits: int):
        self.health -= (hits * damageDealt)

    def isAlive(self):
        return self.health > 0
    
    def equip(self, newCard: Card, location: str):
        if not self.validInventoryLocation(location) or self.isInInventory(newCard):
            return False
        
        # Card already in someone else's inventory
        if newCard.owner is not None:
            return False
        
        if len(self.inventory[location]) < self.maxInventorySlots[location]:
            self.inventory[location].append(newCard)
            newCard.updateOwner(self)
            return True
        
        return False
    
    def reorganize(self, cardsHands: list, cardsBackpack: list):
        # test if the cards are the same
        if len(self.inventory["hands"] + self.inventory["backpack"]) != len(cardsHands + cardsBackpack):
            return False
        for card in self.inventory["hands"] + self.inventory["backpack"]:
            if card not in cardsHands + cardsBackpack:
                return False
        
        # New organisation don't exceed the allowed slots
        if (len(cardsHands) > self.maxInventorySlots["hands"]) or (len(cardsBackpack) > self.maxInventorySlots["backpack"]):
            return False
        
        self.inventory = {"hands": cardsHands, "backpack": cardsBackpack}
        

        return True
    
    def removeCard(self, toRemoveCard: Card):
        for key in self.inventory.keys():
            if toRemoveCard in self.inventory[key]:
                self.inventory[key].remove(toRemoveCard)
                toRemoveCard.updateOwner(None)
                return True
        return False
    
    def validInventoryLocation(self, location: str):
        return True if location in self.inventory.keys() else False
    
    def isInInventory(self, card: Card):
        for key in self.inventory.keys():
            if card in self.inventory[key]:
                return True
        return False
    



