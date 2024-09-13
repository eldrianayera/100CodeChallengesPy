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
        guess = input('Make a guess : ')

play()

