from array import *
import random

nums_1 = array('i', [])
nums_2 = array('i', [])

for i in range(1, 6):
    nums_1.append(random.randint(1, 100))

while len(nums_2) != 3:
    nums_in = int(input('Enter number: '))
    nums_2.append(nums_in)

nums_1.extend(nums_2)
nums_1 = sorted(nums_1)

for num in nums_1:
    print(num)
