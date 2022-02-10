
name = str.title(input('Enter your name: '))
print(len(name))
surname = str.title(input('Enter surname: '))
print(len(surname))
name_surname = name + ' ' + surname
print(f'Your full name is {name_surname}')
print(f'That has, {len(name_surname)}, characters it')
