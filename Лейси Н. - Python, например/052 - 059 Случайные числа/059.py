
import random

color = random.choice(['alb', 'negru', 'albastru', 'rosu', 'verde'])
print(color)
color_input = input('Introdu culoarea: ')
if color_input == color:
    print('super ai ghicit')
else:
    while color != color_input:
        print(f'Culoare se incepe cu litera {color[0]}')
        color_input = input('Mai incearca: ')
        if color_input == color:
            print('super ai ghicit')
