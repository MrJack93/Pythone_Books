
import random

luck = random.choice(['h', 't'])
input('h or t: ')
if luck == 'h':
    print('You win')
else:
    print('Bad luck')
    print(luck)
