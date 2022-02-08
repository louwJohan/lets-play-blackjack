import random

def deck():
    """
    Function creates a deck of cards, shuffles the cards and returns a list
    of 52 cards
    """
    numbers = ["A", "2","3","4","5","6","7","8","9","10","J","Q","K"]
    suite = ["♣","♠","♥","♦"]
    playing_deck = []
    for number in numbers:
        for shape in suite:
            playing_deck.append([number,shape])

        random.shuffle(playing_deck)
    return playing_deck


def deal_cards(cards,number):
    """
    Function takes the deck of cards and returns list of cards.
    It takes a number parameter it specifies how many cards must be 
    handed out.It reduces the amount of cards in the deck
    """
    player_cards = []
    for i in range(number):
        player_cards.append(cards.pop())

    return player_cards

def check_totals(cards, num):
    """
    Checks totals of cards. Takes the list of cards 
    generated by first_2_cards() and returns a total
    """
    player_total = 0
    for i in range(num):
        card_num = cards[i][0]
        if card_num.isnumeric():
            player_total += int(card_num)
        elif card_num == "J":
            player_total += 10
        elif card_num == "Q":
            player_total += 10
        elif card_num == "K":
            player_total += 10        
        elif card_num == "A":
            if player_total > 10:
                player_total += 1
            elif player_total <= 10:
                player_total += 11

    return  player_total          


def start_game_validation(player_input):
    """
    Check if player input is a certain string to start game
    or display the rules
    """
    try:
        if player_input == "start" or player_input == "rules" or player_input == "exit":
            print("Valid input!")
        else:  
            raise ValueError(
                f"Please enter start to start game or rules for the rules"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False

    return True

def play_game_validation(player_input):
    """
    Compares player input to string to ask for another card to stay or 
    to exit the game
    """
    try:
        if player_input == "hit" or player_input == "stay" or player_input == "exit":
            print("Valid input")
        else:
            raise ValueError(
                f"Please enter hit for another card or stay to continue"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

def print_rules():
    """
    The Function prints out the rules of the game
    """
    print('''Beginners Guide to Blackjack 
Introduction
Blackjack is a popular American casino game, now found throughout the
world. It is a banking game in which the aim of the player is to achieve
a hand whose points total nearer to 21 than the banker's hand, but
without exceeding 21.

The following outline explains the basic rules of standard blackjack (21),
along with the house rules most commonly featured in casinos.

Game objective
Although many players may play in a single round of blackjack, it's fundamentally a 
two-player game. In blackjack, players don't play against each other; and they don't co-operate.
The only competition is the dealer.The aim of the game is to accumulate a higher point 
total than the dealer, but without going over 21. You compute your score by adding the values of 
your individual cards. The cards 2 through 10 have their face value, J, Q, and K are 
worth 10 points each, and the Ace is worth either 1 or 11 points (player's choice).
    
The deal and "blackjack"
At the start of a blackjack game, the players and the dealer receive two cards each. 
The players' cards are normally dealt face up, while the dealer has one face down 
(called the hole card) and one face up.The best possible blackjack hand is an opening 
deal of an ace with any ten-point card. This is called a "blackjack", or a natural 21, 
and the player holding this automatically wins unless the dealer also has a blackjack. 
If a player and the dealer each have a blackjack, the result is a push for that player. 
If the dealer has a blackjack, all players not holding a blackjack lose.

The players' turns
After the cards have been dealt, the game goes on with each player taking action - in 
clockwise order starting to dealer's left.Then the player can keep his hand as it is 
(stand) or take more cards from the deck (hit), one at a time, until either the player
judges that the hand is strong enough to go up against the dealer's hand and stands, 
or until it goes over 21, in which case the player immediately loses (busts).
In most places, players can take as many cards as they like, as long as they don't bust, 
but some casinos have restrictions regarding this.

 
The dealer's turn
When all players have finished their actions, either decided to stand or busted, 
the dealer turns over his hidden hole card. If the dealer has a natural 21 (blackjack) 
with his two cards, he won't take any more cards.All players lose, except players
who also have a blackjack, in which case it is a push - the bet is returned
to the player.If the dealer doesn't have a natural, he hits (takes more cards) or
stands depending on the value of the hand. Contrary to the player, though, the dealer's 
action is completely dictated by the rules. The dealer must hit if the value of the hand is 
lower than 17, otherwise the dealer will stand.Whether or not the dealer must hit on a soft 
17 (a hand of 17 containing an ace being counted as 11) differs from casino to casino. 
There might even be blackjack tables with different rules within the same casino.

 
Showdown
If the dealer goes bust, all players who are left in the game win. 
Otherwise players with higher point totals than the dealer win, while 
players with lower totals than the dealer lose. For those with the same 
total as the dealer the result is a push: their stake is returned to them 
and they neither win nor lose.Players with a blackjack win a bet plus 
a bonus amount, which is normally equal to half their original wager. 
A blackjack hand beats any other hand, also those with a total value 
of 21 but with more cards.As described above, if the dealer has a 
blackjack, players with blackjack make a push, while all other players lose.''')


def player_game(players_cards,cards_total,computer_cards,cards):

    """
    This Function controlls the game for the player it will update the 
    variables for the players cards ,score and card totals.
    """
    print(f"Your cards are {players_cards}")
    print(f"Your total is {cards_total}")
    print(f"Dealers first card is {computer_cards[0]}")
    print(f"Dealers total is {check_totals(computer_cards,1)}")
    final_player_total = cards_total

    while True:
        while True:
            player_input = input("Do you want to hit or stay?\nType hit for another card or stay to continue\n")
            if play_game_validation(player_input):
                break
        if player_input == "hit":
            new_card = deal_cards(cards,1)
            print(f"Your new card is {new_card}")
            new_card_total = check_totals(new_card,1)
            if new_card_total == 11:
                if final_player_total > 10:
                    final_player_total += 1
                elif final_player_total <= 10:
                    final_player_total += 11
            elif new_card_total != 11:
                final_player_total += new_card_total
            print(f"Your new total is {final_player_total}")            
        
        if  final_player_total > 21:
                break
        elif player_input == "stay":
            break
    return final_player_total

def computer_play(computer_cards, computer_total, cards):
    """
    Function take two parameters the dealers cards and the total.
    It checks if the total is below 17 if true then deals a new card
    and updates the total
    """
    print(f"Dealers cards are {computer_cards}")
    print(f"Dealers total is {computer_total}")
    
    while computer_total < 17:
            comp_new_card = deal_cards(cards,1)
            print(f"Dealers new card is {comp_new_card}")
            comp_new_card_total = check_totals(comp_new_card,1)
            if comp_new_card_total == 11:
                if computer_total <= 10:
                    computer_total += 11
                elif computer_total > 10:
                    computer_total += 1
            elif comp_new_card_total != 11:
                computer_total += comp_new_card_total
            print(f"Dealers new total is {computer_total}")
    return computer_total


def check_winner(player_total,dealer_total):

    if player_total > 21:
        print(f"Your total is {player_total}. You Bust! ")
    elif dealer_total > 21 and player_total <= 21 :
        print(f"Dealer's total is {dealer_total}. Dealer Bust!")
        print("You win!!")
    elif player_total > dealer_total and dealer_total <=21 and player_total <=21:
        print("You win!")
    elif player_total < dealer_total and dealer_total <=21 and player_total <=21:
        print("Dealer wins!")
    elif player_total == computer_total:
        print("It's a draw!!")
    
def play_game():
    cards = deck()
    player_one = deal_cards(cards, 2)
    computer_cards = deal_cards(cards,2)
    player_one_total = check_totals(player_one, len(player_one))
    computer_total = check_totals(computer_cards, len(computer_cards))
    final_player_one_total = player_game(player_one,player_one_total,computer_cards,cards)
    final_computer_total = computer_play(computer_cards, computer_total, cards)
    check_winner(final_player_one_total,final_computer_total)


def main():

    while True:
        print('''
             _____
            |A .  | _____
            | /.\ ||A ^  | _____
            |(_._)|| / \ ||A _  | _____
            |  |  || \ / || ( ) ||A_ _ |
            |____V||  .  ||(_'_)||( v )|
                   |____V||  |  || \ / |
                          |____V||  .  |
                                 |____V|
        
                 Are you feeling lucky?

                Let' Play Blackjack!!!!!
        ''')     
        print("To start game type 'start'.")
        print("For the rules type 'rules'.") 
        print("Type 'exit' to close game.")
        player_input = input() 
        validation = start_game_validation(player_input)
        if validation:
            break
            

    if player_input == "start":
        play_game()
    elif player_input == "rules":
        print_rules()
    elif player_input == "exit":
        pass


main()
