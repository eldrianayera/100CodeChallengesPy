
def add(num1 , num2) :
    return num1 + num2
def sub(num1 , num2) :
    return num1 - num2
def mul(num1 , num2) :
    return num1 * num2
def div(num1 , num2) :
    return num1 / num2



operators = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

print(operators["/"](4,5))

continue_calc = True

num1 = float(input('Enter your first number : \n'))

while continue_calc :
    num2 = float(input('Enter your second number : \n'))
    operator = input('Enter your operator :\n+\n-\n*\n/\n')
    result = (operators[operator](num1,num2))
    print(num1 , operator , num2 , '=' , result)
    num1 = result
    is_continue = input(f'Do you want to continue with {num1} ? Y/N ?\n')
    if is_continue == 'N' :
         continue_calc = False