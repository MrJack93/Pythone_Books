
nums = []
total = 0
for num in range(3):
    total += 1
    num_in = int(input(f'Enter number {total}: '))
    nums.append(num_in)
print(f'Your list of nums: {nums}')
question = str.title(input('Leave the last entered number in the list (y/n)? : '))
if question == 'N':
    del nums[-1]
print(f'Your new list of nums: {nums}')
