import random
word_list = ["aardvark", "baboon", "camel"]
blanks = ""
choosen_word = random.choice(word_list)
for char in range(0, len(choosen_word)) :
    blanks += "_ "

life = 5
correct_letters = []
print(correct_letters)
while life > 0 :
    if '_' not in blanks :
        break
    else :
        print(choosen_word)
        print(blanks)
        blanks = ""
        print(f'Life = {life}')
        guess = input('Guess a letter !\n').lower()
        for letter in choosen_word :
            if letter == guess :
                blanks += f"{guess} "
                correct_letters.append(guess)
            elif letter in correct_letters :
                blanks += f"{letter} "
            else :
                blanks += '_ '
        
        if guess in choosen_word :
            continue
        else :
            life -= 1

print(blanks)
print('Game Over')

    
