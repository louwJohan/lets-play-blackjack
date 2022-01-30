import random

def deck_of_cards():
    """
    The function generates a deck of cards from 2 lists and 
    shuffles the deck
    """
    numbers = ["A", "2","3","4","5","6","7",
    "8","9","10","J","Q","K"]
    suite = ["S","H","C","D"]

    deck = []
    for number in numbers:
        for shape in suite:
            deck.append(number + shape)

    random.shuffle(deck)
    return deck


def main():
    game_deck = deck_of_cards()


main()
