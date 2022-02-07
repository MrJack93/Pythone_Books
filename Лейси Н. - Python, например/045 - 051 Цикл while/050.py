
num = int(input('Enter number: '))
while num < 10 or num > 20:
    if num < 10:
        print('Too low')
    elif num > 20:
        print('Too high')
    num = int(input('Enter number: '))
print('Thank you')
