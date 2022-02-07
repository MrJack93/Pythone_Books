
num_people = int(input('How many people do you want to invite to the party? '))

if num_people < 10:
    for i in range(0, num_people):
        name = input('Enter name: ')
        print(f'{name.title()} has been invited ')
else:
    print('Too many people')
