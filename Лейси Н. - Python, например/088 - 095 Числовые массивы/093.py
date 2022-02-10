from array import *

nums = array('i', [])
for i in range(0, 5):
    num_in = int(input("Enter number: "))
    nums.append(num_in)
nums = sorted(nums)

print(nums)
num_del = int(input('Enter delete number: '))
nums_2 = nums
nums_2.remove(num_del)
print(nums_2)
