import random
from tkinter import *

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

#class Game:
#    def __init__(self):

if __name__ == "__main__":

    mainGui = Tk()
    mainGui.title("BlackJack")
    mainGui.geometry('250x150')

    mainDeck = Deck()
    mainDeck.shuffle()
    print(mainDeck.cardsLeft())

    #name = input("Enter your name, or don't ")
    #player = Player(name)
    player = Player("Seth")
    player.drawCard(mainDeck)
    player.drawCard(mainDeck)
    #player.printHand()
    
    button1 = Button(mainGui, text="Print player in console", command= lambda: print(player))
    button2 = Button(mainGui, text="Shuffle", command= lambda: mainDeck.shuffle())
    button3 = Button(mainGui, text="Empty Hand", command= lambda: player.emptyHand())
    button4 = Button(mainGui, text="Draw Card", command= lambda: player.drawCard(mainDeck))
    button5 = Button(mainGui, text="Cards Left", command= lambda: print(mainDeck.cardsLeft()))

    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()

    mainGui.mainloop()