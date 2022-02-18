import random
import csv
name = str.title(input('Enter your name: '))
score = 0
question_l = []
answer_l = []
for i in range(1, 3):
    num_random_1 = random.randint(1, 10)
    num_random_2 = random.randint(1, 10)
    question = f'{num_random_1} + {num_random_2} = '
    question_l.append(f'{num_random_1} + {num_random_2}')
    answer = (int(input(question)))
    answer_l.append(answer)
    answer_correct = num_random_2 + num_random_1
    if answer == answer_correct:
        score += 1
file = open('Stars.csv', 'a')
new_record = f'{name}, {question_l}, {answer_l}, {score} \n'
file.write(str(new_record))
file.close()
