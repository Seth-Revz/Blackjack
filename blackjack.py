import random

class Deck(object):
    def __init__(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.cards = []

        for i in range (0, len(suits)):
            for j in range (0, len(ranks)):
                self.cards.append(ranks[j] + " of " + suits[i])

    def shuffle(self):
        random.shuffle(self.cards)

    def removeCard(self):
        self.cards.pop(0)

if __name__ == "__main__":

    deck = Deck()
    deck.shuffle()
    print(deck.cards[0])
    deck.removeCard()