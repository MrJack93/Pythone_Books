
from array import *

nums = array('i', [])

for n in range(1, 6):
    nums.append(int(input(f'Enter number - {n}: ')))

nums = sorted(nums)
nums.reverse()

print(nums)


