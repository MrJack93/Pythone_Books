from array import *

nums = array('i', [1, 2, 3, 48, 48, 15, 47])
print(f'This is your array: {nums}')
nums_in = int(input('Enter one of the array numbers: '))
nums_count = nums.count(nums_in)
print(f'The number {nums_in} occurs {nums_count} times in this array ')
