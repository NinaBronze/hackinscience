from is_prime import *

for i in range(10000, 10051):
    if is_prime(i):
        if i == 10039:
            print(i)
        else:
            print(i, end=", ")
