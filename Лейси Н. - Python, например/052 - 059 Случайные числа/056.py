
import random

num_random = random.randint(1, 10)
print(num_random)
num_in = 0
while num_in != num_random:
    num_in = int(input('Enter number: '))
