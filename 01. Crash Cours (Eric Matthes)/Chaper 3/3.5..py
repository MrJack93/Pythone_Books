invited_list = ['Nicolai', 'Vasile', 'Vadim', 'Andrei', 'Slavic', 'Victor']

for i in invited_list:
    print(f'\'{i}\' Your invite to party!')

no_present = 'Vasile'
print(f'\n{no_present} can\'t come to party!\n')

invited_list[1] = 'Aurica'

for i in invited_list:
    print(f'\'{i}\' Your invite to party!')
