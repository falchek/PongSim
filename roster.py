# represents the roster of players that Judah is able to play


class Roster:
    def __init__(self):
        self.pongWarriors = []

    def addWarrior(self, pongWarrior):
        self.pongWarriors.append(pongWarrior)

    def checkForWarrior(self, name):
        for warrior in self.pongWarriors:
            if warrior.name == name:
                return True
        return False

    def getWarrior(self, name):
        for warrior in self.pongWarriors:
            if warrior.name == name:
                return warrior
