import random
import gameData
data = gameData.data


def play() :
    score = 0
    game_over = True
    A = random.choice(data)
    while game_over :
        print('WELCOME TO HIGHER OR LOWER !')
        B = random.choice(data)
        print(f'Compare A : {A['name']} , {A['description']} , from {A['country']}')
        print(f'Compare B : {B['name']} , {B['description']} , from {B['country']}')
        guess = input('Who has more followers ? "A" or "B" ?\n').lower()
        if A['follower_count'] > B['follower_count'] :
            answer = 'a'
            next = A
        else :
            answer = 'b'
            next = B
        if guess == answer :
            score += 1
            A = next
            print('\n'*10 , f'Your answer is correct , score = {score}')
        else :
            print('Wrong answer , Final score : ' , score)
            game_over = False
            play()



play()

