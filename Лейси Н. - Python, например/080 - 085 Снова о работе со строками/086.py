
password = input('Enter your password: ')
password_repeat = input('Repeat password: ')

if password == password_repeat.upper() or password.lower() == password:
    print('They must be in the same case')
elif password == password_repeat:
    print('Thank you')
else:
    print('Incorrect')
