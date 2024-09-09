print('Welcome to Pizza Deliveries!')
size = input('What size ? S, M, L ? : ')
pepperoni = input('Do you want pepperoni ? Y or N : ')
extra_cheese = input("do you want extra cheese ? Y or N : ")

bill = 0

if size == 'S' :
    bill = 15
elif size == 'M' :
    bill = 20
elif size == 'L' :
    bill = 25
else :
    print('size not valid')

if pepperoni == 'Y' :
    if size == 'S' :
        bill += 2
    else : 
        bill += 3
elif pepperoni == 'N':
    bill = bill
else :
    print('size not valid')

if extra_cheese == 'Y' :
    bill += 1
else :
    bill = bill

print(f'Your final bill is : ${bill}')

