def find_highest() :
    biggest_bid =  0
    for bidder in bid_data :
        if bid_data[bidder] > biggest_bid :
            biggest_bid = bid_data[bidder]

    print(f'The winner is {bidder} with bid = ${biggest_bid}')


bid_data = {}
continue_bid = True

while continue_bid :
    name = input('What is your name ?')
    bid = int(input('How much you wanna bid ?'))
    next_bid = input('Is there next bidder , Y/N ?')
    bid_data[name] = bid
    if next_bid == "N" :
        continue_bid = False
        find_highest()
    else :
        print('\n'*20)