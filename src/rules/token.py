from zone import Zone

class Token:
    def __init__(self, currentZone: Zone):
        self.setZone(currentZone)

    def setZone(self, currentZone):
        self.currentZone = currentZone
        self.currentZone.addToken(self)

class ObjectiveToken(Token):
    def __init__(self, currentZone: Zone, xp=5, color="red"):
        super().__init__(currentZone)
        self.xp = 5
        self.color = color