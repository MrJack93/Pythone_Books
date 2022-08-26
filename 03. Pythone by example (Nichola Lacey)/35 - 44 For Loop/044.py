invitation = int(input('How many people invited to party? '))

if 10 > invitation > 0:
    for loop in range(invitation):
        name = input('Enter name: ')
        print(f'{name} has be invited to party!')
elif invitation >= 10:
    print('Too many people')
else:
    print("Error input")
