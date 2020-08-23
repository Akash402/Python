# Imports
from Player import Player
from Deck import Deck

# Creating Players and shuffling
player_one = Player("PlayerOne")
player_two = Player("PlayerTwo")
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# Game begin
game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player one looses! Player two wins')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player two looses! Player one wins')
        game_on = False
        break
    
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    war_compare = True

    while war_compare:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            war_compare = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            war_compare = False

        else:
            print("WAR!!!!!")
            if len(player_one.all_cards) < 3:
                print("Not enough cards for player one! Player two wins")
                game_on = False
                break

            elif len(player_two.all_cards) < 3:
                print("Not enough cards for player two! Player one wins")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

