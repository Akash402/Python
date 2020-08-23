# Player Class
class Player:
    # Instantiation method
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # Remove one card from player cards
    def remove_one(self):
        return self.all_cards.pop(0)

    # Add card(s) to player cards
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    # Display Player cards
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} card(s).'