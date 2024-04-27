

import random

# deck cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# function do pick two of this cards


def picking_cards(cards):
    random_card = random.choice(cards)
    return random_card

def calculation(score):
    if sum(score) == 21 and len(score) == 2:
        return 0
    if 11 in score and sum(score) > 21:
        score.remove(11)
        score.append(1)
    return sum(score)

def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over, you lose."
        
    elif player_score == 0:
        return "You won is a blackjack."
    elif computer_score == 0:
        return "You lose computer have a blackjack."
    elif player_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Computer went over, you won."
    elif player_score == computer_score:
        return "It´s a draw."
    elif player_score > computer_score:
        return "You won."
    else:
        return "You lose."
        

def play_game():

    player_cards = []
    computer_cards = []
    end_game = False
    
    for _ in range(2):
        player_cards.append(picking_cards(cards))
        computer_cards.append(picking_cards(cards))
    
    while not end_game:
        
        player_score = calculation(player_cards)
        computer_score = calculation(computer_cards)
        print(f"Player deck: {player_cards}. Player score: {player_score}.")
        print(f"Computer deck: {computer_cards[0]}.")
        
        if player_score == 0 or computer_score == 0 or player_score > 21:
            end_game = True
        else:
            hit = input(f"Do you want to hit? 'y', 'n' ")
    
            if hit == "y":
                player_cards.append(picking_cards(cards))
            else:
                end_game = True
    
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(picking_cards(cards))
            computer_score = calculation(computer_cards)
              
        comparing = compare(player_score, computer_score)
        print(f"Player deck: {player_cards}. Player score: {player_score}.")
        print(f"Computer deck: {computer_cards}. Computer deck: {computer_score}.")
        print(comparing)


while input("Do you want to play the game? 'y' 'n'") == "y":
    play_game()        
