comp_num = 50
num = 0
count = 0
while comp_num != num:
    num = int(input('Enter a number: '))
    count += 1
    if num > 50:
        print(f'Enter a number < {num}')
    elif num < 50:
        print(f'Enter a number > {num}')
    else:
        print(f'Well done you took {count} attempts')
