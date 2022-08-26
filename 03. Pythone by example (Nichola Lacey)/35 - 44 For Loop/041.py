name = input("Enter a name: ")
num = int(input("Enter a number < 10: "))

if 10 >= num > 0:
    for i in range(num):
        print(name)
elif num > 10:
    print('Too high')
else:
    print('Error Message')
