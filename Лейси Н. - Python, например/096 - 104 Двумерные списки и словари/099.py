
simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(simple_array)

row = int(input('Enter row: '))
print(simple_array[row])

column = int(input('Enter column: '))
print(simple_array[row][column])

answer = str.upper(input('Do you want to change the number (Y or N): '))

if answer == 'Y':
    new_num = int(input('Enter new number: '))
    simple_array[row][column] = new_num

print(simple_array)
