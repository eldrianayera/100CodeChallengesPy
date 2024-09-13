import random

def deal_card() :
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return  random.choice(cards)

def calculate_score(hand)  :
    return sum(hand)


def play() :
    user_card = []
    com_card = []
    user_score = 0
    com_score = 0
    for x in range(2) :
        user_card.append(deal_card())
        com_card.append(deal_card())
    user_score = calculate_score(user_card)
    com_score = calculate_score(com_card)
    print(f'Your hand is {user_card} , current score : {user_score}\nComputers first card is {com_card[0]}')
    game_on = True
    while game_on :
        is_deal = input('Do you want to deal a new card ? y or n')
        if is_deal = 'y' :
            user_card.append(deal_card())
            game_on = False
        else :
            game_on = False

    while

play()








