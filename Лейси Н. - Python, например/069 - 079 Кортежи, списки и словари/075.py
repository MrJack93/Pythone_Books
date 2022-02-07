
num_list = [321, 457, 234, 342, 423]
for i in num_list:
    print(i)
num_in = int(input('Enter number: '))
if num_in in num_list:
    print(f'Your number index is {num_list.index(num_in)}')
else:
    print('That is not in the list')
