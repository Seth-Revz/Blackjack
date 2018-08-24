
class Player:
    def __init__(self, name = ''):
        self.name = name
        self.hand = []

    def drawCard(self, deck):
        self.hand.append(deck.getCard())

    def printHand(self):
        for i in range(0, len(self.hand)):
            print(self.hand[i])

    def emptyHand(self):
        self.hand.clear()

    def __str__(self):
        str = "\nName: "
        str = str + self.name + "\n"
        for i in range(0, len(self.hand)):
            str = str + self.hand[i] + "\n"
        
        return str