print('1) Square\n'
      '2) Triangle\n')

options = int(input('Select your options: '))

if options == 1:
    sqr_len = int(input('Enter length of square: '))
    ans = sqr_len * sqr_len
    print(f'Aria of square is: {ans}')
elif options == 2:
    triangle_leg = int(input('Enter length of a side of a triangle: '))
    triangle_hei = int(input('Enter height a triangle: '))
    ans = (triangle_leg / 2) * triangle_hei
    print(f'Aria of triangle is: {ans}')
else:
    print("Error selection")
