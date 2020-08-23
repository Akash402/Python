# Imports
from Variables import Variables

# Card Class
class Card:
    # Instantiation method
    def __init__(self, suit, rank):
        self.init_variables = Variables()
        self.suit = suit # choice(self.init_variables.suits)
        self.rank = rank # choice(self.init_variables.ranks)
        self.value = self.init_variables.values[rank]

    # Rank and Suit
    def __str__(self):
        return f"{self.rank} of {self.suit}"

# new_card = Card("Spades", "Ace")
# print(new_card)
