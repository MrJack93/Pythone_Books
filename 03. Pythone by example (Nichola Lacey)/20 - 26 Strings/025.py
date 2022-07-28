
name = input('Enter your name: ')
if len(name) < 5:
    surname = input('Enter your surname: ')
    full_name = name + ' ' + surname
    print(full_name.upper())
else:
    print(name.lower())
