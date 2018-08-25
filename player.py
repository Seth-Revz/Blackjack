from deck import Deck

class Player:
    def __init__(self, name = ''):
        self.name = name
        self.hand = []
        self.busted = False
        self.holding = False
        self.pointTotal = 0
        self.aces = 0

    def drawCard(self, deck):
        self.hand.append(deck.getCard())

    def printHand(self):
        for i in range(0, len(self.hand)):
            print(self.hand[i])

    def getHandValue(self, deck):
        dict = deck.dictionary()
        self.pointTotal = 0

        for i in range(0, len(self.hand)):
            str = self.hand[i].split(' ', 1)[0]
            self.pointTotal += dict[str]
            if str == "Ace":
                self.aces += 1

        if self.pointTotal > 21:
            while self.aces:
                self.pointTotal -= 10
                self.aces -= 1

        return self.pointTotal

    def emptyHand(self):
        self.hand.clear()

    def __str__(self):
        str = "\nName: "
        str = str + self.name + "\n"
        for i in range(0, len(self.hand)):
            str = str + self.hand[i] + "\n"
        
        return str