import random
import math
import time
from itertools import product
from turtle import clear

class Card:
    def __init__(self, suit, cards, card_val):
        self.suit = suit
        self.cards = cards
        self.card_val = card_val





def blackjack(deck):
    global card_val

    player_count = 0
    dealer_count = 0

    while len(player)<2:
        player_card = random.choice(deck)
        player.append(player_card)
        deck.remove(player_card)
        
        player_count += player_card.card_val

        if len(player) == 2:
            if player[0].card_val == 11 and player[1].card_val:
                player[0].card_val = 1
                player_count -= 10
        print("Player cards: ", player[0], ", ", player[1])
        print("Your score: ", player_count)
        input()

        dealer_card = random.choice(deck)
        dealer.append(dealer_card)
        deck.remove(dealer_card)

        dealer_count += dealer_card.card_val

        print("Dealer cards: ")
        if len(dealer) == 1:
            print("Dealer score: ", dealer_count)
        if len(dealer) == 2:
            print("Dealer score: ", )
            if dealer[0].card_val == 11 and dealer[1].card_val:
                dealer[0].card_val = 1
                dealer_count -= 10
        input()
    if player_count == 21:
        ("Player wins")
        quit()
    while player_count < 21:
        choice = input("Choose H to hit or S to stand: ") 

        if len(choice != 1) or (choice.upper() != 'H' and choice.upper() != 'S'):
            print("Invalid input, try again")

        if choice.upper() == 'H':
            player_card = random.choice(deck)
            player.append(player_card)
            deck.remove(player_card)

            player_count += player_card.card_val

            c = 0
            while player_count > 21 and c < len(player):
                if player[c].card_val == 11:
                    player[c].card_val = 1
                    player_count -= 10
                    c += 1
                else:
                    c += 1
            clear()
            print("Dealer score: " , dealer_count)
            print()
            print("Player score: ", player_count)

        if choice.upper() == 'S':
            break
    if player_count == 21:
        print("You got blackjack")
        quit()
    if player_count>21:
        print("You busted")
        quit()
    while dealer_count <17:
        clear()
        print("Dealer hits")
        dealer_card = random.choice(deck)
        dealer.append(dealer_card)

        dealer_count += dealer_card.card_val

        c = 0
        while dealer_count > 21 and c < len(dealer):
            if dealer[c].card_val == 11:
                dealer[c].card_val = 1
                dealer_count -=10
                c += 1
            else:
                c += 1

            print("Dealer score: " , dealer_count)
            print()
            print("Player score: ", player_count)

            input()
    if dealer_count == 21:
        print("Dealer has blackjack, house wins.")
    elif dealer_count == player_count:
        print("Tie game, house wins")
    elif player_count>dealer_count:
        print("You won")
    else:
        print("House wins")
if __name__ == '__main__':
    card_val = {'Two' : 2,'Three' : 3,'Four' : 4,'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8,'Nine' : 9,'Ten' : 10,'Jack' : 10, 'Queen' : 10, 'King' : 10, 'Ace' : 11}
    suit = ['Hearts','Diamonds', 'Spades', 'Clubs']
    cards = ["king", "queen", "jack", "ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    player_count = 0
    dealer_count = 0
    player = []
    dealer = []
    deck = []
    for suits in suit:
        for card in cards:
            deck.append(Card(suit, cards, card_val))

    blackjack(deck)
