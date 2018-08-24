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
        if not self.cards:
            self.resetShuffle()
            print("Deck Empty: Reshuffling then drawing")
        
        card = self.cards[0]
        self.cards.pop(0)
        return card

    def cardsLeft(self):
        return len(self.cards)

    def resetShuffle(self):
        self.cards.clear()
        for i in range (0, len(self.suits)):
            for j in range (0, len(self.ranks)):
                self.cards.append(self.ranks[j] + " of " + self.suits[i])
        self.shuffle()