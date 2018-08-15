import random

class Deck:
    def __init__(self):
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.cards = []

        for i in range (0, len(self.suits)):
            for j in range (0, len(self.ranks)):
                self.cards.append(self.ranks[j] + " of " + self.suits[i])

    def shuffle(self):
        random.shuffle(self.cards)

    def getCard(self):
        card = self.cards[0]
        self.cards.pop(0)
        return card

    def resetShuffle(self):
        self.cards.clear()
        for i in range (0, len(self.suits)):
            for j in range (0, len(self.ranks)):
                self.cards.append(self.ranks[j] + " of " + self.suits[i])
        self.shuffle()

class Player:
    def __init__(self, name = ''):
        self.name = name
        self.hand = []

    def drawCard(self, deck):
        self.hand.append(deck.getCard())

    def printHand(self):
        for i in range(0, len(self.hand)):
            print(self.hand[i])

if __name__ == "__main__":

    playDeck = Deck()
    playDeck.shuffle()
    player = Player()
    player.drawCard(playDeck)
    player.drawCard(playDeck)
    player.printHand()