
tele_program = ['comedy', 'films', 'food', 'animal']
num_1 = 0
print('List programs:')
for program in tele_program:
    num_1 += 1
    print(f'{num_1}. {program.title()}')
question = str.title(input('Enter Tv Program: '))
tv_index = int(input('Enter Tv position: '))
tele_program.insert(tv_index - 1, question)
num_2 = 0
print('New list programs:')
for program in tele_program:
    num_2 += 1
    print(f'{num_2}. {program.title()}')
