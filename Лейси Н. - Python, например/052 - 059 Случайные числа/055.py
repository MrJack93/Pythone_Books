
import random

num = random.randint(1, 5)
num2 = int(input('Enter a number: '))
if num == num2:
    print('Well done')
elif num2 > num:
    print('your number >')
    num2 = int(input('Enter a number: '))
    if num == num2:
        print('Corect')
    else:
        print('You lose')
elif num2 < num:
    print('your number <')
    num2 = int(input('Enter a number: '))
    if num == num2:
        print('Corect')
    else:
        print('You lose')
