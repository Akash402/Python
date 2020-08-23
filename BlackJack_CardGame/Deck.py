# Imports
from random import shuffle
from Card import Card
from Variables import Variables

# Deck Class
class Deck:
    # Instantiation method
    def __init__(self):
        self.init_variables = Variables()
        self.all_cards = []
        for suit in self.init_variables.suits:
            for rank in self.init_variables.ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    # Shuffle Deck method
    def shuffle(self):
        shuffle(self.all_cards)

    # Deal one card method
    def deal_card(self):
        return self.all_cards.pop()


# new_deck = Deck()
# new_deck.shuffle()
# print(new_deck.deal_card())