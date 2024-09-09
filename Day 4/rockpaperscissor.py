import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock,paper,scissors]


input = int(input('type 1 for Rock , 2 for Paper , 3 for Scissors !'))
player_input = list[input - 1]
print(f"You\n{player_input}")
computer_input = random.choice(list)
print(f"Computer\n{computer_input}")
result = ""

if player_input == rock and computer_input == scissors :
    result = "You win"
elif player_input == rock and computer_input == paper : 
    result = "You lose"
elif  player_input == rock and computer_input == rock :
    result = "draw"


if player_input == paper and computer_input == rock :
    result = "You win"
elif player_input == paper and computer_input == scissors : 
    result = "You lose"
elif  player_input == paper and computer_input == paper :
    result = "draw"

if player_input == scissors and computer_input == paper :
    result = "You win"
elif player_input == scissors and computer_input == rock : 
    result = "You lose"
elif  player_input == scissors and computer_input == scissors :
    result = "draw"

print(result)
    

    
