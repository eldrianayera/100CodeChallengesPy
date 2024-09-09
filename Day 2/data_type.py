# Data type in python


print(type('123'))
print(type(123))
print(type(False))
print(type(123_456.72))

# rounding 

print(round(234.33332))
print(round(234.53332,4))

# increment

score = 0
score *= 1
print(score)

# Bill calculator

print('Welcome to the bill calculator')
total = float(input('What was the total bill ?\n'))
tip_percent = float(input('How much tip would you like to give?\n'))
tip = total * (tip_percent / 100 )
persons = float(input('How many people to split bill?\n'))
print(f"Each person should pay {round((total + tip)/persons,2)}")