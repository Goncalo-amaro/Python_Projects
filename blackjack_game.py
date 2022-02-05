
import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

playing = True

#------------------------------------------------------------------------------------------------------------------------------------------
# FIRST STEP -> CLASSES DEFINITION 
#------------------------------------------------------------------------------------------------------------------------------------------
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        #self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.allcards = []
        for s in suits:
            for r in ranks:
                n_card = Card(r,s)
                self.allcards.append(n_card)
    
    def __str__(self):
        deck_comp = ''
        for n in self.allcards:
            deck_comp += '\n'+ Card.__str__()
        return "The deck has: " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.allcards)
    
    def deal(self):
        single_card = self.allcards.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces +=1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces += 1

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
         self.total -= self.bet

#------------------------------------------------------------------------------------------------------------------------------------------
# SECOND STEP -> FUNCTIONS DEFINITION
#------------------------------------------------------------------------------------------------------------------------------------------
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide an integer!")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have {chips.total}")
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? \n" + "Please enter 'H' or 'S' ")

        if x[0].upper() == 'H':
            hit(deck,hand)
        elif x[0].upper() == 'S':
            print('Player stands. It,s dealers turn!')
            playing = False
        else: 
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    
    print("\n Dealer's Hand: ")
    print("First card is hidden!")
    print(dealer.cards[1])

    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's Hand is: {dealer.value}")

    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's Hand is: {player.value}")

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and player tie! PUSH")

#------------------------------------------------------------------------------------------------------------------------------------------
# THIRD STEP -> GAME LOGIC COOCK UP
#------------------------------------------------------------------------------------------------------------------------------------------
while True:
    print("WELCOME TO BLACKJACK")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    for n in range(2):
        player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    for n in range(2):
        dealer_hand.add_card(deck.deal())
    
    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            player_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        
    print(f"\n Player's total chips are at: {player_chips.total}")

    new_game = input("Would you like to keep playing? Input 'Y' for yes and 'N' for no. ")

    if new_game[0].upper() == 'Y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break
    