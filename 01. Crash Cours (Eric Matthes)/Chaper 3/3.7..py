invited_list = ['Nicolai', 'Vasile', 'Vadim', 'Andrei', 'Slavic', 'Victor']

invited_list.insert(0, 'Valeria')
invited_list.insert(4, 'Alisa')
invited_list.append('Alina')
print(invited_list)

while len(invited_list) != 2:
    pop_invited = invited_list.pop()
    print(f'{pop_invited}, I\'m sorry about canceling the invitation!')
print()
for name in invited_list:
    print(f'{name} invitation remains valid!')

while len(invited_list) != 0:
    del invited_list[0]

print(invited_list)