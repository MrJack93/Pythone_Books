num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
total = num_1 + num_2
answer = input('Do you want sum a number?(y/n) ')
while answer != 'n':
    num_3 = int(input('Enter number: '))
    total += num_3
    answer = input('Do you want sum a number?(y/n) ')
print(total)
