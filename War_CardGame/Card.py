# Imports
from Variables import Variables

# Card Class
class Card:
    # Instantiation method
    def __init__(self, suit, rank):
        init_variables = Variables()
        self.suit = suit
        self.rank = rank
        self.value = init_variables.values[rank]

    # Rank and Suit
    def __str__(self):
        return self.rank + " of " + self.suit