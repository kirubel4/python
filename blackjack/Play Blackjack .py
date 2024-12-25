import random
import art
import os
def play_again():
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    computer_score = -1
    user_score = -1
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            add_card = input("Type 'y' to draw another card or type 'n' to exit.")
            if add_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
        
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    def compare():
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You LOSE 😭"
        elif computer_score > 21:
            return "Opponent went over. You WIN 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"
        
    print(f"Your final hand {user_cards}, final score {user_score}. ")
    print(f"Computer final hand {computer_cards}, final score {computer_score}.")
    print(compare())
    ask2 = input("Do you want to play blackjack game again type 'y' to play or type any key to EXIT. ")
    if ask2 == 'y':
        os.system('cls')
        print(art.logo)

        play_again()
        
        
ask = input("Do you want to play blackjack game type 'y' to play or type any key to EXIT. ")
if ask == 'y':
    print(art.logo)
    play_again()