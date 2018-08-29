import random

# represents a pong warrior!


class PongWarrior:
    def __init__(self, name=""):
        self.name = name

    def __str__(self):
        return self.name

# Represents our hero, Judah.  This is a inherited class of PongWarrior.  We always have one.


class Judah(PongWarrior):
    def __init__(self):
        super().__init__("Judah")

    def __str__(self):
        return self.name + "-" + self.randomSuffix()

    def randomSuffix(self):
        suffixes = ["chan", "kun", "sama", "senpai", "desu"]
        randomIndex = random.randint(0, len(suffixes) -1)
        return suffixes[randomIndex]
