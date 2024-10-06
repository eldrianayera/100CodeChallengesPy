with open('./Day 24/input/Letters/starting_letter.txt') as letter :
    letter = letter.read()
    print(letter)

with open('./Day 24/input/Names/invited_names.txt') as invited :
    invited = invited.readlines()
    print(invited)

for _ in invited :
    name = _.strip()
    with open(f'./Day 24/output/ReadyToSend/invitation_letter_{name}.txt',mode='w') as invitation :
        invitation.write(letter.replace('[name]',name))
     
