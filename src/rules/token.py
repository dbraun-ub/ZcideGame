class Token:
    def __init__(self, name:str, zoneId: int):
        self.name = name
        self.zoneId = zoneId


class ObjectiveToken(Token):
    def __init__(self, name: str, zoneId: int, xp: int=5, color: str="red"):
        super().__init__(name, zoneId)
        self.xp = 5
        self.color = color

def createToken(name: str, zoneId: int, xp: int, color: str):
    tokenTypes = {"Objective": ObjectiveToken}

    return tokenTypes[name](name, zoneId, xp, color)