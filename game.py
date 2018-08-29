import pongwarrior

# class repesents a game of pong

class Game:
    def __init__(self, warrior):
        self.opponent = warrior
        self.judah = pongwarrior.Judah() #judah is our hero, so he's always here.

    def declareGame(self):
        print(str(self.judah) + " looks " + str(self.opponent) + " square in the eye, and begins to power up!")


    def judahObviouslyWins(self):
        print(str(self.judah) + " utters, \"Omae wa mou shindeiru...\"")
        print(str(self.opponent) + " shakes his head in sorrow")
        print(str(self.judah) + " serves with a merciless backspin!!!")
        print(str(self.opponent) + " misses the ball completely, and falls to the floor in a crumpled heap!")
        print(str(self.judah) + " wins!")