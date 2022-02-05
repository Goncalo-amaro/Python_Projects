"""
This is an example of a simple card game computed in python. 
--- It is also very usefull to check how classes can be used. ---
"""

# create a dictionary with the card values, suits and ranks stored
import random
import pdb

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# card class ->
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# deck class ->
class Deck:
    def __init__(self):
        self.all_cards = []

        for s in suits:
            for r in ranks:
                new_card = Card(s,r)
                self.all_cards.append(new_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# player class ->
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def remove_one(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards in is hand.'

# Game logic setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26): # THIS ESTABLISHES THE BEGINNING DECKS FOR EACH PLAYER
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Current round: {round_num}')

    if len(player_one.all_cards) == 0: # CHECKS IF THE PLAYER STILL HAS CARDS
        print('Player One is out of cards! Player Two wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two is out of cards! Player One wins!')
        game_on = False
        break
    
    # start a new round -> STARTING BY CREATING THE CURRENT CARS IN HAND (ln. 84 to 88) <-
    player_one_cards = []
    player_one_cards.append(player_one.remove_one()) # ADDS THE LAST CARD OF THE CURRENT PLAYER'S DECK

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value: # IN CASE THERE IS NO WAR AND PLAYER'S 1 CARD IS HIGHER
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
            break
        
        elif player_one_cards[-1].value < player_two_cards[-1].value: # IN CASE THERE IS NO WAR AND PLAYER'S 2 CARD IS HIGHER
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
            break

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5: # CHECKS IF PLAYER 1 HAS ENOUGH CARDS TO PROCEDE TO WAR 
                print('Player One unable to declare war.')
                print('Player Two WINS!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5: # CHECKS IF PLAYER 2 HAS ENOUGH CARDS TO PROCEDE TO WAR 
                print('Player Two is unable to declare war.')
                print('Plaeyr One WINS!')
                game_on = False
                break

            else:                     # THE TWO PLAYERS ARE ATE WAR AND EACH OF THEM DRAW 5 CARDS FROM THEIR DECKS 
                for num in range(5):  # -> ABOVE THE CYCLE THE LAST CARD REMOVED WILL BE AGAIN COMPARED! <-
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
