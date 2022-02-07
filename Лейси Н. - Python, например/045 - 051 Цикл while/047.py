
num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
sum = num_1 + num_2
answer = 'y'
while answer == 'y':
    answer = input('Would you like to add another number: ')
    if answer == 'y':
        num_3 = int(input('Enter third number: '))
        sum += num_3
print(f'Te total is {sum}')
