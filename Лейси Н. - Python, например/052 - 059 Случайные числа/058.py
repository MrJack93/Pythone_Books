
import random

score = 0
for i in range(1, 6):
    num_random_1 = random.randint(1, 10)
    num_random_2 = random.randint(1, 10)
    print(f'{i}. {num_random_1} + {num_random_2} = ')
    answer = int(input('Enter answer: '))
    answer_correct = num_random_2 + num_random_1
    if answer == answer_correct:
        score += 1
print(f'Score total: {score}')
