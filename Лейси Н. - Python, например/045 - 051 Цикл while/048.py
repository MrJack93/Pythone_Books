
sum = 1
answer = 'y'
while answer == 'y':
    name = input('Enter the name of the person you want to invite to the party: ')
    print(f'{name.title()} has invited')
    answer = input('Would you like to add a person: ')
    if answer == 'y':
        sum += 1
    else:
        print(f'You invete to party: {sum} person')
