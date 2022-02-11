from array import *

nums = array('d', [12.89, 18.88, 28.98, 55.55, 78.91])
print(nums)

num_in = int(input('Enter number between 2 and 5: '))

while num_in not in range(2, 5):
    print('Error number')
    num_in = int(input('Try again(number between 2 and 5): '))

new_nums = array('d', [])

for i in nums:
    i /= num_in
    new_nums.append(i.__round__(2))

print(new_nums)


