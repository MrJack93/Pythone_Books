
num = 10
while num > 0:
    print(f'«There are {num} green bottles hanging on the wall, {num} green bottles hanging on the  wall, and if 1 '
          f'green bottle should accidentally fall»')
    bottles = int(input('how many green bottles will be hanging on the wall? '))
    if num - 1 == bottles:
        num -= 1
        print(f'There will be {num} green bottles hanging on the wall')
    else:
        print('No, try again')
print('There are no more green bottles hanging on the wall')
