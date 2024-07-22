
import random
import numpy as np

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_first_hand():
    user_cards = [random.choice(cards), random.choice(cards)]
    user_sum = np.sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_sum}")

    computer_cards = [random.choice(cards), random.choice(cards)]
    print(f"Computer's first card: {computer_cards[0]}")

    return(user_cards, computer_cards)

def ace_exception_check(card_list):
    if 11 in card_list:
        for idx, card in enumerate(card_list):
            if card == 11:
                card_list[idx] = 1
                new_sum = np.sum(card_list)
                if new_sum <= 21:
                    return card_list
                else:
                    card_list[idx] = 11
                    return card_list

    else:
        return card_list

def deal_more_cards_player(player_card_list):
    player_card_list.append(random.choice(cards))
    ace_exception_check(player_card_list)
    print(f"Your cards {player_card_list}, current score: {np.sum(player_card_list)}")
    return(player_card_list)

def deal_more_cards_computer(computer_card_list):
    while np.sum(computer_card_list) <= 16:
        computer_card_list.append(random.choice(cards))
        ace_exception_check(computer_card_list)
    return(computer_card_list)


def check_bust(user_cards, computer_cards):
    if np.sum(user_cards) > 21:
        ace_exception_check(user_cards)
        if np.sum(user_cards) > 21:
            get_final_hands(user_cards, computer_cards)
            game_over = True
            print("You went over. You Lose!")
            return(game_over)
    elif np.sum(computer_cards) > 21:
        ace_exception_check(computer_cards)
        if np.sum(computer_cards) > 21:
            get_final_hands(user_cards, computer_cards)
            print("The opponent went over. You Win!")
            game_over = True
            return(game_over)
    else:
        game_over = False
        return(game_over)
def check_game_over(user_cards, computer_cards):
    game_over = False
    if np.sum(user_cards) == 21 and np.sum(computer_cards) < 21:
        deal_more_cards_computer(computer_cards)

        if np.sum(user_cards) == 21 & np.sum(computer_cards) < 21:
            print("Congratulations You Win!")
            game_over = True
    if np.sum(computer_cards) > 21:
        print("Opponent went over. You win")
        game_over = True

    elif np.sum(user_cards) == 21 and np.sum(computer_cards) == 21:
        print("It's a draw, no one wins")
        game_over = True

    elif np.sum(user_cards) == 21 and np.sum(computer_cards) < 21:
        print("Congratulations You've Won the Game")
        game_over = True

    elif np.sum(user_cards) < np.sum(computer_cards):
        print("You've lost the game. Computer Wins! ")
        game_over = True

    elif np.sum(user_cards) > np.sum(computer_cards):
        print("You've won the game! Congratulations")
        game_over = True
    return(game_over)

def get_final_hands(user_cards, computer_cards):
    print(f"Your final hand: {user_cards}, final score: {np.sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {np.sum(computer_cards)}")