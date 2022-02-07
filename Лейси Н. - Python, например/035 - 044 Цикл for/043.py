
question = input('In which direction you want to count (forward or backward)? ')
if question == 'forward':
    num = int(input('Enter number: '))
    for i in range(1, num + 1, 1):
        print(i)
elif question == 'backward':
    num = int(input('Enter number < 20: '))
    for i in range(20, num - 1, -1):
        print(i)
else:
    print('Error message')
