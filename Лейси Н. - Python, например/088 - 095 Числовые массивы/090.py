from array import *

nums = array('i', [])

while len(nums) != 5:
    num_in = int(input('Enter a number between 10 and 20: '))
    if 10 <= num_in <= 20:
        nums.append(num_in)
    else:
        print('Outside range')

print('Thank you')

for i in nums:
    print(i)





