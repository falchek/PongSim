import pongwarrior
import roster
import game

def getname():
    return input("Who do you challenge, Judah-chan?!!\n")

def buildRoster():
    labWarriors = ["Mike", "Kenway", "Ryan", "Christian", "Marc", "Tommy"]
    labRoster = roster.Roster()
    for warriorName in labWarriors:
        warrior = pongwarrior.PongWarrior(warriorName)
        labRoster.addWarrior(warrior)
    return labRoster


# Main function!
rosterOfOpponents = buildRoster()

name = getname()
found = rosterOfOpponents.checkForWarrior(name)
if found:
    print("You challenge " + name + "!!!")
    pingPongGame = game.Game(rosterOfOpponents.getWarrior(name))
    pingPongGame.declareGame()
    pingPongGame.judahObviouslyWins()
else:
    print("This person isn't in the lab to challenge.  Weeb.")
