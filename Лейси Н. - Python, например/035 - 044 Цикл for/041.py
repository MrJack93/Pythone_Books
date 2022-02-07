
name = input("Enter name: ")
num = int(input('Enter number: '))

if num < 10:
    for i in range(num):
        print(name.title())
else:
    for i in range(3):
        print('Too high')
