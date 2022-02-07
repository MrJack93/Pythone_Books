
print('1 - Square')
print('2 - Triangle')
print()
num = int(input('Enter \'1\' or \'2\':'))
if num == 1:
    length_square = int(input('Enter the length of the side of the square: '))
    answer = length_square * length_square
    print('Answer:', answer)
elif num == 2:
    length_triangle = int(input('Enter triangle length:'))
    height_triangle = int(input('Enter triangle height:'))
    answer = (length_triangle * height_triangle) / 2
    print('Answer:', int(answer))
else:
    print('Error')
