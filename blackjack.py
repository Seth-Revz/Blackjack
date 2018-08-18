import random
import sys
import os
from tkinter import *
from tkinter import ttk

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

class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        self.quitButton = ttk.Button(self, text='Quit', command=self.quit) 
        self.printPlayerButton = ttk.Button(self, text="Print player in console", command= lambda: print(player))
        self.shuffleDeckButton = ttk.Button(self, text="Shuffle", command= lambda: mainDeck.shuffle())
        self.emptyHandButton = ttk.Button(self, text="Empty Hand", command= lambda: player.emptyHand())
        self.drawCardButton = ttk.Button(self, text="Draw Card", command= lambda: player.drawCard(mainDeck))
        self.cardsLeftButton = ttk.Button(self, text="Cards Left", command= lambda: print(mainDeck.cardsLeft()))
        self.quitButton.grid(row=1, column=1)
        self.printPlayerButton.grid(row=3, column=2)
        self.shuffleDeckButton.grid(row=1, column=2, sticky="w")
        self.emptyHandButton.grid(row=2, column=2, sticky="w")
        self.drawCardButton.grid(row=2, column=1)
        self.cardsLeftButton.grid(row=3, column=1)

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

if __name__ == "__main__":

    app = Application()
    app.master.title("BlackJack")
    app.master.geometry('250x150')
    app.master.iconbitmap(get_script_path() + "/assets/card.ico")
    
    mainDeck = Deck()
    mainDeck.shuffle()
    print(mainDeck.cardsLeft())

    #name = input("Enter your name, or don't ")
    #player = Player(name)
    player = Player("Seth")
    player.drawCard(mainDeck)
    player.drawCard(mainDeck)
    #player.printHand()

    style = ttk.Style()
    style.theme_use("vista")

    app.mainloop()