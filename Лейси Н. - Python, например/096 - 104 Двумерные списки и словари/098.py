
simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(simple_array)
row = int(input('Enter row: '))
print(simple_array[row])
num_in = int(input('Enter new number: '))
simple_array[row].append(num_in)
print(simple_array[row])

