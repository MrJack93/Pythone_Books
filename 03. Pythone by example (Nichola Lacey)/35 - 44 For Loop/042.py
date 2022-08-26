
total = 0

for loop in range(5):
    in_num = int(input("Enter number: "))
    answer = str(input('Sum the number?(y/n) '))
    if answer == 'y':
        total += in_num

print(total)
