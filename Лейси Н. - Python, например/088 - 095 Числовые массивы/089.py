from array import *
import random

nums = array('i', [])

for num_random in range(0, 5):
    nums.append(random.randint(1, 100))

for output in nums:
    print(output)
