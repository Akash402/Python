# Imports
from Player import Player
from Deck import Deck
from Dealer import Dealer

def blackjack():
    # Creating Player
    player = Player("PlayerOne")
    dealer = Dealer()
    keep_playing_flag = True

    while keep_playing_flag:
        # Flags and Varibales
        hit_stay = True
        dealer_bets = True
        player.bet_cards = []
        player.score = 0
        dealer.bet_cards = []
        dealer.score = 0

        # Placing player bet
        print(f"Enter your bet value. One bet limit: {player.one_bet_limit}, Chips available: {player.chips_available}")
        bet_value = int(input("Bet value? "))
        if bet_value < player.chips_available and bet_value <= player.one_bet_limit:
            player.place_bet(bet_value)

        # Creating and Shuffling new deck for bet
        new_deck = Deck()
        new_deck.shuffle()

        player.bet_cards.append(new_deck.deal_card())
        player.score += player.bet_cards[-1].value
        player.bet_cards.append(new_deck.deal_card())
        player.score += player.bet_cards[-1].value
        dealer.bet_cards.append(new_deck.deal_card())
        dealer.score += dealer.bet_cards[-1].value
        print(f"Your first card - {player.bet_cards[0]}\nYour second card - {player.bet_cards[1]}")

        if player.score == 21:
            print(f"BLACKJACK!!! Your score is {player.score}. You get three times your bet!")
            blackjack_amount = bet_value * 3
            player.add_win_amount(blackjack_amount)
            hit_stay = False
            dealer_bets = False
        
        else:
            print(f"Dealers first card - {dealer.bet_cards[0]}, Score = {dealer.score}")

        while hit_stay:
            if player.score > 21:
                print(f"Your score - {player.score}, is more than 21! You Lose!!")
                hit_stay  = False
                dealer_bets = False
                break

            elif player.score < 21:
                print(f"Your score is {player.score}. Do you wish to hit or stay?")
                player_choice = input("Hit or Stay?\nPress H or h for Hit and S or s for Stay ")
                if player_choice == "H" or player_choice == "h":
                    player.bet_cards.append(new_deck.deal_card())
                    player.score += player.bet_cards[-1].value
                    print(f"Your new card - {player.bet_cards[-1]}")

                else:
                    print("You've decided to stay. You can't place any bets and no cards will be dealt")
                    print(f"Your score is {player.score}")
                    hit_stay = False
                    break

            elif player.score == 21:
                print(f"BLACKJACK!!! Your score is {player.score}. You get three times your bet!")
                blackjack_amount = bet_value * 3
                player.add_win_amount(blackjack_amount)
                hit_stay = False
                dealer_bets = False
                break
        
        while dealer_bets:
            if dealer.score < 21 and dealer.score < player.score:
                dealer.bet_cards.append(new_deck.deal_card())
                dealer.score += dealer.bet_cards[-1].value
                print(f"Dealers new card - {dealer.bet_cards[-1]}, Score = {dealer.score}")

            elif dealer.score > 21:
                print(f"Dealer busted! Score {dealer.score}, You win!!")
                win_amount = bet_value * 2
                player.add_win_amount(win_amount)
                dealer_bets = False
                break

            elif dealer.score > player.score:
                print(f"Dealer score - {dealer.score}, Your score {player.score}, You lose!!!")
                dealer_bets = False
                break

            elif dealer.score == player.score:
                print(f"Dealer score - {dealer.score}, Your score {player.score}, Tie!!!")
                print("Ypu get your bet money back")
                win_amount = bet_value
                player.add_win_amount(win_amount)
                dealer_bets = False
                break

        keep_playing = input("Do you wish to continue? Press Y or y for Yes, N or n for No ")
        if keep_playing == "Y" or keep_playing == "y":
            continue

        else:
            keep_playing_flag = False

if __name__ == "__main__":
    blackjack()
