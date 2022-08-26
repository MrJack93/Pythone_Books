bottles = 10

while bottles != 0:
    print(f'There are {bottles} green bottles hanging on the wall,\n'
          f'{bottles} green bottles hanging wall, and if if 1 green\n'
          f'bottle should accidentally fall.\n')
    bottles -= 1
    answer = int(input('How many green bottles will be hanging on the wall? '))
    if bottles == answer:
        print(f'There will be {bottles} hanging on the wall?')
    else:
        while answer != bottles:
            answer = int(input('Try again: '))
print('Ther are no more bottles hanging on the wall')
