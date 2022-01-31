import random

def deck():
    """
    Function creates a deck of cards, shuffles the cards and returns a list
    of 52 cards
    """
    numbers = ["A", 2,3,4,5,6,7,
    8,9,10,"J","Q","K"]
    suite = ["♣","♠","♥","♦"]
    playing_deck = []
    for number in numbers:
        for shape in suite:
            playing_deck.append([number,shape])

        random.shuffle(playing_deck)
    return playing_deck

cards = deck()

def check_totals(player_cards, computer_cards):
    """
    Checks totals of cards 
    """
    player_total = 0
    computer_total = 0
    for i in range(2):
        if type(player_cards[i][0]) == int:
            player_total += player_cards[i][0]
        elif player_cards[i][0] == "A":
            if player_total > 10:
                player_total += 1
            else:
                player_total +=11
        elif player_cards[i][0] == "J" or "Q" or "K":
            player_total += 10

    for i in range(2):
        if type(computer_cards[i][0]) == int:
            computer_total += computer_cards[i][0]
        elif computer_cards[i][0] == "A":
            if computer_total > 10:
                computer_total += 1
            else:
                computer_total +=11
        elif computer_cards[i][0] == "J" or "Q" or "K":
            computer_total += 10

    return player_total, computer_total               

def play_game(cards):
    
    player_cards = []
    computer_cards = []

    for i in range(2):
        player_cards.append(cards.pop())
        computer_cards.append(cards.pop())  

    print(player_cards) 
    print(computer_cards) 

    print(check_totals(player_cards, computer_cards)) 
                  


play = play_game(cards)
print(len(cards))

