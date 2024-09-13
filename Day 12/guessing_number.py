#Guessing number
import random


def play() :
    life = 0
    print('Welcome to the Number Guessing Game\nI am thinking of a number between 1 - 100.')
    answer = random.randint(1,101)
    difficulty = input('Enter a difficulty , "easy" or "hard"')
    if difficulty == 'easy' :
        life = 10
    else :
        life = 5
    while life > 0 :
        print(f'You have {life} attempts remaining to guess the number')
        guess = int(input('Make a guess : '))
        if guess == answer :
            print(f'You guess the right number : {guess}')
            break
        else :
            life -= 1
            if guess > answer :
                print('Too high\nTry again.')
            else :
                print('Too low\nTry again.')

play()

