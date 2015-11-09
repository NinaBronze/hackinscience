from is_prime import *

for i in range(10000, 10051):
    if is_prime(i):
        i = str(i)
        print(i + ", ", end="")
