import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# Pick a random item from a list
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices)
print(f"Random choice: {random_choice}")

# Shuffle a list
random.shuffle(choices)
print(f"Shuffled list: {choices}")

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")
