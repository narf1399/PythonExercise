from Goalkeeper import Goalkeeper
from Midfielder import Midfielder
from Defender import Defender
from Striker import Striker

myKeeper = Goalkeeper("Timo Horn", "german", 23, 1, "1. FC Koeln")
myKeeper.playerInformation()
myKeeper.playerAction()

myDefender = Defender("Jonas Hector", "german", 25, 14, "1. FC Koeln")
myDefender.playerInformation()
myDefender.playerAction()

myMidfielder = Midfielder("Kevin Vogt", "german", 24, 6, "1. FC Koeln")
myMidfielder.playerInformation()
myMidfielder.playerAction()

myStriker = Striker("Anthony Modeste", "french", 27, 27, "1. FC Koeln")
myStriker.playerInformation()
myStriker.playerAction()
