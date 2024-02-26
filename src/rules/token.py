class Token:
    def __init__(self):
        pass


class ObjectiveToken(Token):
    def __init__(self, xp=5, color="red"):
        super().__init__()
        self.xp = 5
        self.color = color