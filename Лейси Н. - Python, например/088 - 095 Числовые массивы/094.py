from array import *

nums = array('i', [4, 234, 42, 43, 656, 7575])

for i in nums:
    print(i)

num_in = int(input('Enter a number in the array: '))
while num_in not in nums:
    num_in = int(input('Try again: '))

print(f'The num position in the array is: {nums.index(num_in) + 1}')


