
import sys
import os
from player import Player
from deck import Deck
from tkinter import *
from tkinter import ttk
'''
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
'''

if __name__ == "__main__":

    '''
    app = Application()
    app.master.title("BlackJack")
    app.master.geometry('250x150')
    app.master.iconbitmap("assets/card.ico")
    '''

    mainDeck = Deck()
    mainDeck.shuffle()
    print(mainDeck.cardsLeft())

    #name = input("Enter your name, or don't ")
    #player = Player(name)
    player = Player("Seth")
    player.drawCard(mainDeck)
    player.drawCard(mainDeck)
    #player.printHand()

    '''
    style = ttk.Style()
    style.theme_use("vista")
    app.mainloop()
    '''