from is_prime import *

sum = 0

for i in range(0, 1001):
    if is_prime(i) == True:
        sum = sum + i
print(sum)
