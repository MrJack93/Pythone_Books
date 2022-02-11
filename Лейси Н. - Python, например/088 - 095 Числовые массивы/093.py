from array import *

nums = array('i', [])
nums_2 = array('i', [])

for i in range(1, 6):
    num_in = int(input(f"Enter number '{i}': "))
    nums.append(num_in)

nums = array('i', sorted(nums))
print(f'Your sorted array - {nums}')

num_del = int(input('Enter delete number: '))
while num_del not in nums:
    num_del = int(input('That is not a value in the array, try again: '))

nums.remove(num_del)
nums_2.append(num_del)

print(nums)
print(nums_2)
