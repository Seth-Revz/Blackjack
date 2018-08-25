import os
import platform

from player import Player
from deck import Deck

class Game:
    def __init__(self):
        self.mainDeck = Deck()
        self.mainDeck.shuffle()
        exitLoop = ""

    def play(self):
        self.dealer = Player("Dealer")
        self.dealer.drawCard(self.mainDeck)
        self.dealer.drawCard(self.mainDeck)

        self.player = Player("Player 1")
        self.player.drawCard(self.mainDeck)
        self.player.drawCard(self.mainDeck)

        while True:
            clear()

            if self.player.getHandValue(self.mainDeck) == 21:
                exitLoop = "21"
                break
            if self.player.getHandValue(self.mainDeck) > 21:
                exitLoop = "bust"
                break

            self.player.printHand()
            print("Hand value: " + str(self.player.getHandValue(self.mainDeck)) + "\n")

            self.dealer.printHand()
            print("Hand value: " + str(self.dealer.getHandValue(self.mainDeck)) + "\n")
            print("1: Hit, 2: Hold")
            choice = input("Input: ")

            if choice == "1" or choice == "Hit":
                self.player.drawCard(self.mainDeck)
            if choice == "2" or choice == "Hold":
                self.player.holding = True

            print(choice)

            if self.player.holding:
                exitLoop = "holding"
                break

        if exitLoop == "21":
            self.dealerAI()
        if exitLoop == "bust":
            self.gameOver("bust")
        if exitLoop == "holding":
            self.dealerAI()
    
    def dealerAI(self):
        while True:
            if self.dealer.getHandValue(self.mainDeck) == 21 and self.player.getHandValue(self.mainDeck) == 21:
                self.gameOver("draw")
                break
            if self.dealer.getHandValue(self.mainDeck) > 21:
                self.gameOver("win")
                break
            if self.player.getHandValue(self.mainDeck) > self.dealer.getHandValue(self.mainDeck):
                self.dealer.drawCard(self.mainDeck)
                continue
            if self.player.getHandValue(self.mainDeck) == self.dealer.getHandValue(self.mainDeck):
                self.gameOver("draw")
                break
            if self.player.getHandValue(self.mainDeck) < self.dealer.getHandValue(self.mainDeck):
                self.gameOver("lose")
                break
            


    def gameOver(self, condition=""):
        clear()
        if condition == "draw":
            self.player.printHand()
            print("Hand value: " + str(self.player.getHandValue(self.mainDeck)) + "\n")
            self.dealer.printHand()
            print("Hand value: " + str(self.dealer.getHandValue(self.mainDeck)) + "\n")
            print("House wins all ties\n")
        if condition == "win":
            self.player.printHand()
            print("Hand value: " + str(self.player.getHandValue(self.mainDeck)) + "\n")
            self.dealer.printHand()
            print("Hand value: " + str(self.dealer.getHandValue(self.mainDeck)) + "\n")
            print("You Won\n")
        if condition == "lose":
            self.player.printHand()
            print("Hand value: " + str(self.player.getHandValue(self.mainDeck)) + "\n")
            self.dealer.printHand()
            print("Hand value: " + str(self.dealer.getHandValue(self.mainDeck)) + "\n")
            print("Dealer Won\n")
        if condition == "bust":
            self.player.printHand()
            print("Hand value: " + str(self.player.getHandValue(self.mainDeck)) + "\n")
            self.dealer.printHand()
            print("Hand value: " + str(self.dealer.getHandValue(self.mainDeck)) + "\n")
            print("You Busted - You Lose\n")
        

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')