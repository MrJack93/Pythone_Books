
total = 0
for i in range(0, 5):
    num = int(input('Enter number: '))
    question = str(input('Sum number? '))
    if question == 'yes':
        total += num
print(total)
