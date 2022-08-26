total = 0
answer = 'y'

while answer != 'n':
    name = input('Enter name to invited: ')
    print(f'{name} has been invited')
    total += 1
    answer = input('Do you want to invited more people?(y/n) ')
print(f'The total is: {total}')
