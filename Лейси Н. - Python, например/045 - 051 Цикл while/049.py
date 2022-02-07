
comp_num = 50
num = 0
total = 0
while comp_num != num:
    num = int(input("Enter number: "))
    if num > comp_num:
        print('Number >')
        total += 1
    elif num == comp_num:
        print(f'Well done, you took {total} attempts')
        break
    else:
        print('Number <')
        total +=1
