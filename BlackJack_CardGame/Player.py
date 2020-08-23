# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.bet_cards = []
        self.score = 0
        self.one_bet_limit = 500
        self.chips_available = 100000
    
    def place_bet(self, amount):
        self.chips_available -= amount

    def add_win_amount(self, amount):
        self.chips_available += amount
