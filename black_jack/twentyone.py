import random

_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


# the function maps the card character strings to point values, and sums the values
# however, aces have to be handled separately because they can value 1 or 11 points
def _hand_total(hand):
    values = [None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, ]
    value_map = {k: v for k, v in zip(_cards, values)}

    total = sum([value_map[card] for card in hand if card != 'A'])
    ace_count = hand.count('A')

    for i in range(ace_count, -1, -1):
        if i == 0:
            total = total + ace_count
        elif total + (i * 11) + (ace_count - i) <= 21:
            total = total + (i * 11) + ace_count - i
            break

    return total


def _next_card():
    return random.choice(_cards)


class Dealer:
    def __init__(self):
        self.hand = []

    def new_round(self):  # the _next_card() function will be defined as a top-level function
        self.hand = [_next_card(), _next_card()]  # of the module, along with a definition of the cards

    def get_hand_total(self):  # ability for the dealer to total it's cards
        return _hand_total(self.hand)

    def determine_play(self, total):
        if total < 17:
            return 'hit'
        else:
            return 'stand'

    def make_play(self):
        return self.determine_play(self.get_hand_total())