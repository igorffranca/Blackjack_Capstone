import random
import os

def clear():
    if os.name == 'nt':
      os.system('cls')
    else:
       os.system('clear')
def print_final_result(u_score, comp_score, com_cards, u_cards):
    print(f"Your final hand: {u_cards}, final score: {u_score}")
    print(f"Computer's final hand: {com_cards}, final score: {comp_score}")

def verify_result(u_score, comp_score, com_cards, u_cards):
    if u_score > 21:
        print_final_result(u_score, comp_score, com_cards, u_cards)
        print("You went over! You lose 😤")
    elif comp_score > 21:
        print_final_result(u_score, comp_score, com_cards, u_cards)
        print("Opponent went over. You win 😁")
    elif u_score < 21 and comp_score < 21:
        if u_score > comp_score:
            print_final_result(u_score, comp_score, com_cards, u_cards)
            print("You win 😁")
        elif u_score == comp_score:
            print_final_result(u_score, comp_score, com_cards, u_cards)
            print("Draw")
        else:
            print_final_result(u_score, comp_score, com_cards, u_cards)
            print("You lose 😤") 
    

def game():
    
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    while True:
        clear()
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = []
        computer_cards = []
        user_current_score = 0
        computer_score = 0

        for _ in range(2):
            card = random.choice(cards)
            user_cards.append(card)
            user_current_score += card

        computer_first_card = random.choice(cards)
        computer_cards.append(computer_first_card)
        computer_score = computer_first_card

        print(f"Your cards: {user_cards}, current score: {user_current_score}")
        print(f"Computer's first card: {computer_first_card}")

        continue_game = True
        while continue_game:
            if computer_score > 21 or user_current_score > 21:
                verify_result(user_current_score, computer_score, computer_cards, user_cards)
                continue_game = False
            else:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
                if another_card == "y":
                    card = random.choice(cards)
                    user_cards.append(card)
                    user_current_score += card
                    if user_current_score < 21:
                        print_final_result(user_current_score, computer_score, computer_cards, user_cards)
                elif another_card == "n":
                    for _ in range(len(user_cards) - len(computer_cards)):
                        card = random.choice(cards)
                        computer_cards.append(card)
                        computer_score += card
                    verify_result(user_current_score, computer_score, computer_cards, user_cards)
                    continue_game = False
                else:
                    print("Invalid option. Type 'y' or 'n'.")

        another_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if another_game == 'y':
            game()
        elif another_game == 'n':
            break

game()